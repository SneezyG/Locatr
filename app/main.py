from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import database, schemas, crud

app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/regions", response_model=schemas.RegionResponse)
def create_region(region: schemas.RegionCreate, db: Session = Depends(get_db)):
    try:
        db_region = crud.create_region(db, region)
        return db_region
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/regions/contains", response_model=list[schemas.RegionResponse])
def check_point(lat: float, lon: float, db: Session = Depends(get_db)):
    regions = crud.find_region_by_point(db, lat, lon)
    return [{"id": str(r.id), "name": r.name} for r in regions]
