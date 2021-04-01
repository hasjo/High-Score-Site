from DBStuff import Schema, engine, find_data
from sqlalchemy.orm import Session

with Session(engine) as session:
    for row in find_data.get_games_list(session):
        print(row.Game.name, row.Game.id)
