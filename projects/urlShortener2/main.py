# main.py

from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, String, Integer, MetaData, Table
from databases import Database
from typing import List

app = FastAPI()

# Database Configuration
DATABASE_URL = "mssql+pyodbc://sa:your-password@sql-server/testdb?driver=ODBC+Driver+17+for+SQL+Server"
database = Database(DATABASE_URL)

metadata = MetaData()

url_mappings = Table(
    "url_mappings",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("short_url", String, index=True),
    Column("original_url", String),
)

metadata.create_all(bind=create_engine(DATABASE_URL))

# JWT Configuration
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"

# OAuth2PasswordBearer for authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Function to verify token
def verify_token(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise credentials_exception


# Token creation function
def create_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)


class URLItem(BaseModel):
    original_url: str


class Token(BaseModel):
    access_token: str
    token_type: str


# Endpoint for token creation (authentication)
@app.post("/token", response_model=Token)
async def login_for_access_token():
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    # In a real-world scenario, you would validate the credentials against a user database
    fake_user = {"username": "testuser", "password": "testpassword"}

    token_data = {"sub": fake_user["username"]}
    return {"access_token": create_token(token_data), "token_type": "bearer"}


# CRUD Endpoints
@app.post("/shorten", response_model=str)
async def create_short_url(url_item: URLItem, token: str = Depends(verify_token)):
    short_url = hash(url_item.original_url)  # You might want a better hashing method

    async with database.transaction():
        query = url_mappings.insert().values(short_url=str(short_url), original_url=url_item.original_url)
        await database.execute(query)

    return str(short_url)


@app.get("/expand/{short_url}", response_model=URLItem)
async def expand_short_url(short_url: str, token: str = Depends(verify_token)):
    query = url_mappings.select().where(url_mappings.c.short_url == short_url)
    result = await database.fetch_one(query)

    if result is None:
        raise HTTPException(status_code=404, detail="Short URL not found")

    return {"original_url": result['original_url']}


@app.get("/urls", response_model=List[URLItem])
async def get_all_urls(token: str = Depends(verify_token)):
    query = url_mappings.select()
    results = await database.fetch_all(query)

    return results


@app.delete("/delete/{short_url}", response_model=str)
async def delete_short_url(short_url: str, token: str = Depends(verify_token)):
    async with database.transaction():
        query = url_mappings.delete().where(url_mappings.c.short_url == short_url)
        result = await database.execute(query)

    if result == 0:
        raise HTTPException(status_code=404, detail="Short URL not found")

    return "Short URL deleted"


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
