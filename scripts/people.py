from sqlalchemy import create_engine
from model import Base, People
from sqlalchemy.orm import Session
from datetime import datetime
import requests

engine = create_engine("sqlite:///SW.db", echo=True)
Base.metadata.create_all(bind=engine)

def insertPeople():
    url = 'https://swapi.dev/api/people/'
    r = requests.get(url)
    with Session(engine) as session:
        
        while url:
            r = requests.get(url)

            if r.status_code == 200:
                data = r.json()
                url = data.get('next')
                people = data['results']
                for person in people:
                    name = person['name']
                    eyeColor = person['eye_color']
                    birth = person['birth_year']
                    gender = person['gender']
                    hair = person['hair_color']
                    height = person['height']
                    homeworld = person['homeworld']
                    mass = person['mass']
                    skinColor = person['skin_color']
                    created = datetime.strptime(person['created'], '%Y-%m-%dT%H:%M:%S.%fZ')
                    edited = datetime.strptime(person['edited'], '%Y-%m-%dT%H:%M:%S.%fZ')
                    url2 = person['url']
                    people = People(name = name, 
                                    eye_color= eyeColor, 
                                    birth_year = birth,
                                    gender = gender,
                                    hair_color = hair,
                                    height = height,
                                    homeworld = homeworld,
                                    mass = mass,
                                    skin_color = skinColor,
                                    created = created,
                                    edited = edited,
                                    url = url2
                                    )
                                    
                    session.add(people)
            else:
                print(f'Erro ao acessar a url: {url}')
                break
        session.commit()