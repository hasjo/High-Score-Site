from DBStuff import engine, filter_data
from sqlalchemy.orm import Session

with Session(engine) as session:
    print(filter_data.get_high_scores_by_game_id(session, 1))
