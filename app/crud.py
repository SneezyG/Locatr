from shapely.geometry import Polygon, Point
from geoalchemy2.shape import from_shape, to_shape
from sqlalchemy.orm import Session
from . import models, schemas

def create_region(db: Session, region: schemas.RegionCreate):
    coords = [(c.lon, c.lat) for c in region.coordinates]
    polygon = Polygon(coords)

    if not polygon.is_valid:
        raise ValueError("Invalid polygon")

    db_region = models.Region(
        name=region.name,
        geom=from_shape(polygon, srid=4326)
    )
    db.add(db_region)
    db.commit()
    db.refresh(db_region)
    return db_region

def find_region_by_point(db: Session, lat: float, lon: float):
    point = from_shape(Point(lon, lat), srid=4326)
    return db.query(models.Region).filter(models.Region.geom.ST_Contains(point)).all()
