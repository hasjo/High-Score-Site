from sqlalchemy.orm import Session
import Schema
from datetime import datetime
from engine import engine
import random

with Session(engine) as session:
    person1 = Schema.User(name='person1', display_name='Person1!')
    addlist = [person1]
    for item in addlist:
        session.add(item)
    session.commit()
    for user in addlist:
        user_base = user.name
        user_number = str(random.randint(0,999)).zfill(3)
        user_pass = user_base + user_number
        password = Schema.Password(password=user_pass, user=user.id)
        session.add(password)
        session.commit()
