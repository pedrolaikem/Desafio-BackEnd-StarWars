from sqlalchemy import create_engine
from model import Base, Films
from sqlalchemy.orm import Session
from datetime import datetime
import requests

engine = create_engine("sqlite:///SW.db", echo=True)
Base.metadata.create_all(bind=engine)

def insertFilms():
    url = 'https://swapi.dev/api/films/'
    r = requests.get(url)
    with Session(engine) as session:
        r = requests.get(url)
        data = r.json()
        url = data.get('next')
        films_data = data['results']
        for film_data in films_data:
            title = film_data['title']
            created = datetime.strptime(film_data['created'], '%Y-%m-%dT%H:%M:%S.%fZ')
            edited = datetime.strptime(film_data['edited'], '%Y-%m-%dT%H:%M:%S.%fZ')
            director = film_data['director']
            episode_id = film_data['episode_id']
            opening_crawl = film_data['opening_crawl']
            producer = film_data['producer']
            release_date = datetime.strptime(film_data['release_date'], '%Y-%m-%d')
            url = film_data['url']
            film = Films(
                    title=title,
                    created=created,
                    director=director,
                    edited=edited,
                    episode_id=episode_id,
                    opening_crawl=opening_crawl,
                    producer=producer,
                    release_date=release_date,
                    url=url
                    )
            session.add(film)
        session.commit()