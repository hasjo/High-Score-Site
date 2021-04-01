from sqlalchemy import create_engine
from DBStuff import secret_stuff

engine = create_engine(f"postgresql+psycopg2://postgres:{secret_stuff.dbpass}@localhost:5432/postgres",
                       echo=False,
                       future=True)
