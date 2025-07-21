from typing import List
from pydantic import BaseModel

class Coordinate(BaseModel):
    lat: float
    lon: float

class RegionCreate(BaseModel):
    name: str
    coordinates: List[Coordinate]

class RegionResponse(BaseModel):
    id: str
    name: str
