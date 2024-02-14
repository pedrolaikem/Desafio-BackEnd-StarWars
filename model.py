
# HTTP/1.0 200 OK
# Content-Type: application/json
# {
#     "birth_year": "19 BBY",
#     "eye_color": "Blue",
#     "films": [
#         "https://swapi.dev/api/films/1/",
#         ...
#     ],
#     "gender": "Male",
#     "hair_color": "Blond",
#     "height": "172",
#     "homeworld": "https://swapi.dev/api/planets/1/",
#     "mass": "77",
#     "name": "Luke Skywalker",
#     "skin_color": "Fair",
#     "created": "2014-12-09T13:50:51.644000Z",
#     "edited": "2014-12-10T13:52:43.172000Z",
#     "species": [
#         "https://swapi.dev/api/species/1/"
#     ],
#     "starships": [
#         "https://swapi.dev/api/starships/12/",
#         ...
#     ],
#     "url": "https://swapi.dev/api/people/1/",
#     "vehicles": [
#         "https://swapi.dev/api/vehicles/14/"
#         ...
#     ]
# }






from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Integer
from datetime import datetime
from sqlalchemy import DateTime
from sqlalchemy import Text
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Base(DeclarativeBase):
    pass

class People(Base):
    __tablename__ = "people"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    eye_color: Mapped[str] = mapped_column(String(10))
    birth_year: Mapped[str] = mapped_column(String(10))
    gender: Mapped[str] = mapped_column(String(10))
    hair_color: Mapped[str] = mapped_column(String(10))
    height: Mapped[int] = mapped_column(Integer)
    homeworld: Mapped[str] = mapped_column(String(10))
    mass: Mapped[int] = mapped_column(Integer)
    skin_color: Mapped[str] = mapped_column(String(10))
    created: Mapped[datetime] = mapped_column(DateTime)
    edited: Mapped[datetime] = mapped_column(DateTime)
    url: Mapped[str] = mapped_column(String(100))

class Films(Base):
    __tablename__ = "films"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(20))
    created: Mapped[datetime] = mapped_column(DateTime)
    director: Mapped[str] = mapped_column(String(20))
    edited: Mapped[datetime] = mapped_column(DateTime)
    episode_id: Mapped[int] = mapped_column(Integer)
    opening_crawl: Mapped[str]  = mapped_column(Text)
    producer: Mapped[str] = mapped_column(String(20))
    release_date: Mapped[datetime] = mapped_column(DateTime)
    url: Mapped[str] = mapped_column(String(100))

class Starships(Base):
    __tablename__ = "starships"
    name: Mapped[str] = mapped_column(String(20))
    id: Mapped[int] = mapped_column(primary_key=True)
    MGLT: Mapped[str] = mapped_column(String(20))
    cargo_capacity: Mapped[int] = mapped_column(Integer)
    cost_in_credits: Mapped[int] = mapped_column(Integer)
    created: Mapped[datetime] = mapped_column(DateTime)
    crew: Mapped[int] = mapped_column(Integer)
    edited: Mapped[datetime] = mapped_column(DateTime)
    hyperdrive_rating: Mapped[int] = mapped_column(Integer)
    length: Mapped[str] = mapped_column(String(100))
    manufacturer: Mapped[str] = mapped_column(String(100))
    max_atmosphering_speed: Mapped[str] = mapped_column(String(100))
    model: Mapped[str] = mapped_column(String(20))
    passengers: Mapped[int] = mapped_column(Integer)
    starship_class: Mapped[str] = mapped_column(String(20))
    url: Mapped[str] = mapped_column(String(100))


class Vehicles(Base):
    __tablename__ = "vehicles"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20))
    model: Mapped[str] = mapped_column(String(20))
    vehicle_class: Mapped[str] = mapped_column(String(20))
    manufacturer: Mapped[str] = mapped_column(String(100))
    length: Mapped[str] = mapped_column(String(100))
    cost_in_credits: Mapped[str] = mapped_column(String(100))
    crew: Mapped[str] = mapped_column(String(20))
    passengers: Mapped[int] = mapped_column(Integer)
    max_atmosphering_speed: Mapped[str] = mapped_column(String(100))
    cargo_capacity: Mapped[int] = mapped_column(Integer)
    consumables: Mapped[str] = mapped_column(String(20))
    url: Mapped[str] = mapped_column(String(100))
    


class Species(Base):
    __tablename__ = "species"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20))
    classification: Mapped[str] = mapped_column(String(20))
    designation: Mapped[str] = mapped_column(String(20))
    average_height: Mapped[str] = mapped_column(String(20))
    average_lifespan: Mapped[str] = mapped_column(String(20))
    homeworld: Mapped[str] = mapped_column(String(20))
    eye_colors: Mapped[str] = mapped_column(String(20))
    hair_colors: Mapped[str] = mapped_column(String(20))
    skin_colors: Mapped[str] = mapped_column(String(20))
    language: Mapped[str] = mapped_column(String(20))
    url: Mapped[str] = mapped_column(String(100))
    created: Mapped[datetime] = mapped_column(DateTime)
    edited: Mapped[datetime] = mapped_column(DateTime)


    

class Planets(Base):
    __tablename__ = "planets"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20))
    diameter: Mapped[str] = mapped_column(String(20))
    rotation_period: Mapped[str] = mapped_column(String(20))
    orbital_period: Mapped[str] = mapped_column(String(20))
    gravity: Mapped[str] = mapped_column(String(20))
    population: Mapped[str] = mapped_column(String(20))
    climate: Mapped[str] = mapped_column(String(20))
    terrain: Mapped[str] = mapped_column(String(20))
    surface_water: Mapped[str] = mapped_column(String(20))
    url: Mapped[str] = mapped_column(String(100))
    created: Mapped[datetime] = mapped_column(DateTime)
    edited: Mapped[datetime] = mapped_column(DateTime)
    








