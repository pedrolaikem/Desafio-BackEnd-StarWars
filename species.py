from sqlalchemy import create_engine
from model import Base, Species
from sqlalchemy.orm import Session
from datetime import datetime
import requests

engine = create_engine("sqlite:///SW.db", echo=True)
Base.metadata.create_all(bind=engine)

def insertSpecies():
    url = 'https://swapi.dev/api/species/'
    r = requests.get(url)
    with Session(engine) as session:
        while url:
            r = requests.get(url)
            if r.status_code == 200:
                data = r.json()
                url = data.get('next')
                species_data = data['results']
                for specie_data in species_data:
                    name = specie_data['name']
                    classification = specie_data['classification']
                    designation = specie_data['designation']
                    average_height = specie_data['average_height']
                    average_lifespan = specie_data['average_lifespan']
                    eye_colors = specie_data['eye_colors']
                    hair_colors = specie_data['hair_colors']
                    skin_colors = specie_data['skin_colors']
                    language = specie_data['language']
                    homeworld = specie_data['homeworld'] if 'homeworld' in specie_data and specie_data['homeworld'] is not None else 'Não encontrado'
                    
                    url2 = specie_data['url']
                    created = datetime.strptime(specie_data['created'], '%Y-%m-%dT%H:%M:%S.%fZ')
                    edited = datetime.strptime(specie_data['edited'], '%Y-%m-%dT%H:%M:%S.%fZ')
                    species = Species(
                        name=name,
                        classification=classification,
                        designation=designation,
                        average_height=average_height,
                        average_lifespan=average_lifespan,
                        eye_colors=eye_colors,
                        hair_colors=hair_colors,
                        skin_colors=skin_colors,
                        language=language,
                        homeworld=homeworld,
                        url=url2,
                        created=created,
                        edited=edited
                    )
                    session.add(species)
            else:
                print(f'Erro ao acessar a url: {url}')
                break
        
        session.commit()