from sqlalchemy.orm import Session
from DBStuff import Schema, engine, find_data
from datetime import datetime

with Session(engine) as session:
    mariokart = find_data.get_game_ids(session, 'Mario Kart 8 Deluxe')[0].Game
    fc = Schema.Section(name='Flower Cup', game=mariokart.id)
    session.add(fc)
    session.commit()
    mc = Schema.Level(name='Mario Circuit', section=fc.id)
    th = Schema.Level(name='Toad Harbor', section=fc.id)
    tm = Schema.Level(name='Twisted Mansion', section=fc.id)
    sgf = Schema.Level(name='Shy Guy Falls', section=fc.id)
    addlist = [mc, th, tm, sgf]
    for item in addlist:
        session.add(item)
    session.commit()
