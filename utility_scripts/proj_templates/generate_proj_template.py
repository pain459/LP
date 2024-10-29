import os

def create_project_structure(project_name):
    # Define project directory structure
    dirs = [
        f"{project_name}/app",
        f"{project_name}/app/api",
        f"{project_name}/app/models",
        f"{project_name}/app/schemas",
        f"{project_name}/app/crud",
        f"{project_name}/app/database",
    ]

    files = {
        f"{project_name}/main.py": main_content(),
        f"{project_name}/app/api/api_v1.py": api_v1_content(),
        f"{project_name}/app/models/item.py": model_content(),
        f"{project_name}/app/schemas/item.py": schema_content(),
        f"{project_name}/app/crud/item.py": crud_content(),
        f"{project_name}/app/database/database.py": db_content(),
        f"{project_name}/requirements.txt": requirements_content(),
    }

    # Create directories
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)

    # Create files with content
    for file_path, content in files.items():
        with open(file_path, 'w') as f:
            f.write(content)
    
    print(f"{project_name} structure created successfully.")

def main_content():
    return '''\
from fastapi import FastAPI
from app.api.api_v1 import router as api_router

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the CRUD API!"}

app.include_router(api_router)
'''

def api_v1_content():
    return '''\
from fastapi import APIRouter
from app.api import items

router = APIRouter()
router.include_router(items.router, prefix="/items", tags=["items"])
'''

def model_content():
    return '''\
from sqlalchemy import Column, Integer, String
from app.database.database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
'''

def schema_content():
    return '''\
from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str
    description: str

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True
'''

def crud_content():
    return '''\
from sqlalchemy.orm import Session
from app.models.item import Item
from app.schemas.item import ItemCreate

def get_item(db: Session, item_id: int):
    return db.query(Item).filter(Item.id == item_id).first()

def get_items(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Item).offset(skip).limit(limit).all()

def create_item(db: Session, item: ItemCreate):
    db_item = Item(name=item.name, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_item(db: Session, item_id: int):
    db_item = get_item(db, item_id)
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item
'''

def db_content():
    return '''\
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
'''

def requirements_content():
    return '''\
fastapi
sqlalchemy
pydantic
uvicorn[standard]
'''

if __name__ == "__main__":
    project_name = input("Enter your project name: ")
    create_project_structure(project_name)
