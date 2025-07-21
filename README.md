# 🗺️ Locatr: A Coordinate-to-Region Mapping system

A mapping system that lets users define named geographic regions (as polygons) and can then determine which regions a coordinate falls.

## [See Locatr Code Repo](https://github.com/SneezyG/Locatr)

---

## 🚀 Key Features

- **Define Regions**: Users can create named regions by submitting a list of latitude/longitude coordinates forming a polygon.
- **Point Lookup**: Given a coordinate, the API returns all regions that contain that point.
- **Geospatial Accuracy**: Utilizes robust spatial functions for precise point-in-polygon querying.
- **Fast Spatial Queries**: Backed by PostGIS with spatial indexing for high performance.

---

## 📍 Use Cases

- **Land Management**: Map farmland or property boundaries and locate them via GPS.
- **Geofencing**: Trigger actions based on whether a device enters a defined region.
- **Surveying**: Tag, group, or catalog spatial features by custom regions.
- **Logistics**: Route optimization or delivery validation within service zones.
- **IoT & Tracking**: Assign assets or sensors to predefined geographic areas.

---

## 🧠 Architecture

- **FastAPI**: Lightweight Python web framework for the API layer.
- **PostgreSQL + PostGIS**: Primary database with spatial extensions for storing and querying geospatial data.
- **SQLAlchemy + GeoAlchemy2**: ORM layer for interacting with PostgreSQL and PostGIS.
- **Shapely**: Used to validate and manipulate geometric shapes in Python before storage or processing.

---

## ⚙️ Technology Stack

| Layer       | Technology              |
|-------------|--------------------------|
| API         | FastAPI                  |
| Database    | PostgreSQL + PostGIS     |
| ORM         | SQLAlchemy + GeoAlchemy2 |
| Geometry    | Shapely                  |
| Environment | Python 3.11+             |

---

## 🔌 API Endpoints

### `POST /regions`
Create a new region with a name and polygon coordinates.

### `GET /regions/contains?lat=...&lon=...`
Query which regions (if any) contain the given point.

---

## 📦 Spatial Logic

- **Polygon Storage**: Regions are stored as `POLYGON` geometry types in PostGIS with SRID `4326`.
- **Point-In-Polygon Check**: Performed using PostGIS `ST_Contains()` function.
- **Validation**: Polygon validity is checked using Shapely before database insertion.

---

## 🛡️ Notes

- Designed for extensibility with support for authentication, user ownership, region updates, or multi-polygon support.
- All spatial data assumes WGS 84 coordinate system (EPSG:4326).

---

