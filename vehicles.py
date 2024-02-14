from sqlalchemy import create_engine
from model import Base, Vehicles
from sqlalchemy.orm import Session
from datetime import datetime
import requests

engine = create_engine("sqlite:///SW.db", echo=True)
Base.metadata.create_all(bind=engine)

def insertVehicles():
    url = 'https://swapi.dev/api/vehicles/'
    r = requests.get(url)
    with Session(engine) as session:
        while url:
            r = requests.get(url)
            if r.status_code == 200:
                data = r.json()
                url = data.get('next')
                vehicles_data = data['results']
                for vehicle_data in vehicles_data:
                    name = vehicle_data['name']
                    model = vehicle_data['model']
                    vehicle_class = vehicle_data['vehicle_class']
                    manufacturer = vehicle_data['manufacturer']
                    length = vehicle_data['length']
                    cost_in_credits = vehicle_data['cost_in_credits']
                    crew = vehicle_data['crew']
                    passengers = vehicle_data['passengers']
                    max_atmosphering_speed = vehicle_data['max_atmosphering_speed']
                    cargo_capacity = vehicle_data['cargo_capacity']
                    consumables = vehicle_data['consumables']
                    url2 = vehicle_data['url']
                    vehicle = Vehicles(
                        name=name,
                        model=model,
                        vehicle_class=vehicle_class,
                        manufacturer=manufacturer,
                        length=length,
                        cost_in_credits=cost_in_credits,
                        crew=crew,
                        passengers=passengers,
                        max_atmosphering_speed=max_atmosphering_speed,
                        cargo_capacity=cargo_capacity,
                        consumables=consumables,
                        url=url2
                    )
                    session.add(vehicle)
            else:
                print(f'Erro ao acessar a url: {url}')
                break
        session.commit()