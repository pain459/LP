from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from models import StatusEvent, Base
from database import SessionLocal, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/create_event/")
def create_event(event: str, detail: str, status: str, db: Session = Depends(get_db)):
    db_event = StatusEvent(event=event, detail=detail, status=status)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event
