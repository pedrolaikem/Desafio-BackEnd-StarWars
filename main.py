from sqlalchemy import create_engine
from model import Base, Vehicles
from sqlalchemy.orm import Session
from planets import *
from people import *
from films import *
from ships import *
from species import *
from vehicles import *

engine = create_engine("sqlite:///SW.db", echo=True)
Base.metadata.create_all(bind=engine)

insertPlanet()
insertPeople()
insertFilms()
insertSpecies()
insertVehicles()
insertShips()




