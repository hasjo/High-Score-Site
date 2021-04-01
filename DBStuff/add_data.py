from DBStuff import Schema, engine
from sqlalchemy.orm import Session
from sqlalchemy import text

def add_list(session, addlist):
    for item in addlist:
        session.add(item)

def add_game(session, name):
    newgame = Schema.Game(name=name)
    session.add(newgame)
    session.commit()
    return newgame

def add_user(session, username):
    newuser = Schema.User(name=name)
    session.add(newuser)
    session.commit()
    return newuser

def add_section(session, name, game_id):
    newsection = Schema.Section(name=name, game=game_id)
    session.add(newsection)
    session.commit()
    return newsection

def add_level(session, name, section_id):
    newlevel = Schema.Level(name=name, section=section_id)
    session.add(newlevel)
    session.commit()
    return newlevel

def add_tttime(session, level_id, user_id, time, lap1, lap2, lap3, proof, timestamp):
    newtime = Schema.TTTime(level=level_id,
                            user=user_id,
                            time=time,
                            lap1=lap1,
                            lap2=lap2,
                            lap3=lap3,
                            proof=proof,
                            timestamp=timestamp)
    session.add(newtime)
    session.commit()
