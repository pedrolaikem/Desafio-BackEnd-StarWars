from sqlalchemy import create_engine
from model import Base, Vehicles
from sqlalchemy.orm import Session
from scripts.planets import *
from scripts.people import *
from scripts.films import *
from scripts.ships import *
from scripts.species import *
from scripts.vehicles import *

engine = create_engine("sqlite:///SW.db", echo=True)
Base.metadata.create_all(bind=engine)

insertPlanet()
insertPeople()
insertFilms()
insertSpecies()
insertVehicles()
insertShips()




