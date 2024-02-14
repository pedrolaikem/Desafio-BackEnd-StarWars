from sqlalchemy import create_engine
from model import Base, Planets
from sqlalchemy.orm import Session
from datetime import datetime
import requests

engine = create_engine("sqlite:///SW.db", echo=True)
Base.metadata.create_all(bind=engine)

def insertPlanet():
    url = 'https://swapi.dev/api/planets/'
    r = requests.get(url)
    with Session(engine) as session:
        
        while url:
            r = requests.get(url)

            if r.status_code == 200:
                data = r.json()
                url = data.get('next')
                planets_data = data['results']
                for planet_data in planets_data:
                    name = planet_data['name']
                    diameter = planet_data['diameter']
                    rotation_period = planet_data['rotation_period']
                    orbital_period = planet_data['orbital_period']
                    gravity = planet_data['gravity']
                    population = planet_data['population']
                    climate = planet_data['climate']
                    terrain = planet_data['terrain']
                    surface_water = planet_data['surface_water']
                    url2 = planet_data['url']
                    created = datetime.strptime(planet_data['created'], '%Y-%m-%dT%H:%M:%S.%fZ')
                    edited = datetime.strptime(planet_data['edited'], '%Y-%m-%dT%H:%M:%S.%fZ')
                    
                    planet = Planets(
                        name=name,
                        diameter=diameter,
                        rotation_period=rotation_period,
                        orbital_period=orbital_period,
                        gravity=gravity,
                        population=population,
                        climate=climate,
                        terrain=terrain,
                        surface_water=surface_water,
                        url=url2,
                        created=created,
                        edited=edited
                    )            
                    session.add(planet)
            else:
                print(f'Erro ao acessar a url: {url}')
                break
        session.commit()