from DBStuff import Schema, engine, find_data
from sqlalchemy import select

def update_user_display_name(session, user_id, new_display_name):
    edit_user = find_data.get_user_by_id(session, user_id)
    edit_user.User.display_name = new_display_name
    session.commit()

def update_user_password(session, user_id, new_password):
    password = find_data.get_password_by_user_id(session, user_id)[0].Password
    password.password = new_password
    session.commit()
