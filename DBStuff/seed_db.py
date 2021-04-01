from sqlalchemy.orm import Session
import Schema
from datetime import datetime
from engine import engine

with Session(engine) as session:
    jordan = Schema.User(name='jordan', display_name='Jordan')
    session.add(jordan)
    session.commit()
    password = Schema.Password(password='jordan', user=jordan.id)
    session.add(password)
    session.commit()
    mariokart = Schema.Game(name='Mario Kart 8 Deluxe')
    session.add(mariokart)
    session.commit()
    mc = Schema.Section(name='Mushroom Cup', game=mariokart.id)
    session.add(mc)
    session.commit()
    mks = Schema.Level(name='Mario Kart Stadium', section=mc.id)
    wp = Schema.Level(name='Water Park', section=mc.id)
    ssc = Schema.Level(name='Sweet Sweet Canyon', section=mc.id)
    tr = Schema.Level(name='Thwomp Ruins', section=mc.id)
    addlist = [mks, wp, ssc, tr]
    for item in addlist:
        session.add(item)
    session.commit()
