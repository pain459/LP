from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/create_event/")
def create_event(event: str, detail: str, status: str, db: Session = Depends(get_db)):
    db_event = models.StatusEvent(event=event, detail=detail, status=status)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

@app.get("/get_events/")
def get_events(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(models.StatusEvent).offset(skip).limit(limit).all()
