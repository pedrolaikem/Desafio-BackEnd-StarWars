from sqlalchemy import create_engine
from model import Base, Starships
from sqlalchemy.orm import Session
from datetime import datetime
import requests

engine = create_engine("sqlite:///SW.db", echo=True)
Base.metadata.create_all(bind=engine)

def insertShips():
    url = 'https://swapi.dev/api/starships/'
    r = requests.get(url)
    with Session(engine) as session:  
        while url:
            r = requests.get(url)
            if r.status_code == 200:
                data = r.json()
                url = data.get('next')
                starships_data = data['results']
                for starship_data in starships_data:
                    name = starship_data['name']
                    MGLT = starship_data['MGLT']
                    cargo_capacity = starship_data['cargo_capacity']
                    cost_in_credits = starship_data['cost_in_credits']
                    created = datetime.strptime(starship_data['created'], '%Y-%m-%dT%H:%M:%S.%fZ')
                    crew = starship_data['crew']
                    edited = datetime.strptime(starship_data['edited'], '%Y-%m-%dT%H:%M:%S.%fZ')
                    hyperdrive_rating = starship_data['hyperdrive_rating']
                    length = starship_data['length']
                    manufacturer = starship_data['manufacturer']
                    max_atmosphering_speed = starship_data['max_atmosphering_speed']
                    model = starship_data['model']
                    passengers = starship_data['passengers']
                    starship_class = starship_data['starship_class']
                    url2 = starship_data['url']

                    starship = Starships(
                    name = name,
                    MGLT= MGLT,
                    cargo_capacity=cargo_capacity,
                    cost_in_credits=cost_in_credits,
                    created=created,
                    crew=crew,
                    edited=edited,
                    hyperdrive_rating=hyperdrive_rating,
                    length=length,
                    manufacturer=manufacturer,
                    max_atmosphering_speed=max_atmosphering_speed,
                    model=model,
                    passengers=passengers,
                    starship_class=starship_class,
                    url=url2     
                )
                    session.add(starship)
            else:
                print(f'Erro ao acessar a url: {url}')
                break
        session.commit()

