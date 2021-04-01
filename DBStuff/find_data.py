from DBStuff import Schema
from sqlalchemy import select

def get_user_ids(session, username):
    statement = select(Schema.User).filter_by(name=username)
    result = session.execute(statement).all()
    return result

def get_user_by_id(session, user_id):
    statement = select(Schema.User).filter_by(id=user_id)
    result = session.execute(statement).all()[0]
    return result

def get_user_name(session, user_id):
    statement = select(Schema.User).filter_by(id=user_id)
    result = session.execute(statement).all()[0].User.name
    return result

def get_user_display_name(session, user_id):
    statement = select(Schema.User).filter_by(id=user_id)
    result = session.execute(statement).all()[0].User.display_name
    return result

def get_game_ids(session, game):
    statement = select(Schema.Game).filter_by(name=game)
    result = session.execute(statement).all()
    return result

def get_game_name(session, game_id):
    statement = select(Schema.Game).filter_by(id=game_id)
    result = session.execute(statement).all()[0].Game.name
    return result

def get_section_ids(session, section):
    statement = select(Schema.Section).filter_by(name=section)
    result = session.execute(statement).all()
    return result

def get_level_ids(session, level):
    statement = select(Schema.Level).filter_by(name=level)
    result = session.execute(statement).all()
    return result

def get_all_levels(session):
    statement = select(Schema.Level)
    result = session.execute(statement).all()
    return result

def get_level_name(session, level_id):
    statement = select(Schema.Level).filter_by(id=level_id)
    result = session.execute(statement).all()[0].Level.name
    return result

def get_tttime_by_level(session, level_id):
    statement = select(Schema.TTTime).filter_by(level=level_id).order_by(Schema.TTTime.time)
    result = session.execute(statement).all()
    return result

def get_tttime_by_id(session, tttime_id):
    statement = select(Schema.TTTime).filter_by(id=tttime_id)
    result = session.execute(statement).all()[0]
    return result

def get_tttime_by_user(session, user_id):
    statement = select(Schema.TTTime).filter_by(user=user_id)
    result = session.execute(statement).all()
    return result

def get_user_best_tttime_by_level(session, user_id, level_id):
    statement = select(Schema.TTTime).filter_by(user=user_id, level=level_id)
    result = session.execute(statement).all()
    return result

def get_games_list(session):
    statement = select(Schema.Game)
    result = session.execute(statement).all()
    return result

def get_section_list_by_game(session, game_id):
    sectionstatement = select(Schema.Section).filter_by(game=game_id)
    sectionresult = session.execute(sectionstatement).all()
    sectionlist = []
    for result in sectionresult:
        sectionlist.append(result.Section.name)
    return sectionlist

def get_level_list_by_game(session, game_id):
    sectionstatement = select(Schema.Section).filter_by(game=game_id)
    sectionresult = session.execute(sectionstatement).all()
    sectionlist = []
    for result in sectionresult:
        sectionlist.append(result.Section.id)
    levellist = []
    for sectionid in sectionlist:
        get_level_list_by_section(session, sectionid)
        levelstatement = select(Schema.Level).filter_by(section=sectionid)
        levelresult = session.execute(levelstatement).all()
        for level in levelresult:
            levellist.append(level.Level.name)
    return levellist

def get_level_ids_by_game(session, game_id):
    sectionstatement = select(Schema.Section).filter_by(game=game_id)
    sectionresult = session.execute(sectionstatement).all()
    sectionlist = []
    for result in sectionresult:
        sectionlist.append(result.Section.id)
    levellist = []
    for sectionid in sectionlist:
        get_level_list_by_section(session, sectionid)
        levelstatement = select(Schema.Level).filter_by(section=sectionid)
        levelresult = session.execute(levelstatement).all()
        for level in levelresult:
            levellist.append(level.Level.id)
    return levellist

def get_level_ids_by_section(session, section_id):
    levellist = []
    get_level_list_by_section(session, section_id)
    levelstatement = select(Schema.Level).filter_by(section=section_id)
    levelresult = session.execute(levelstatement).all()
    for level in levelresult:
        levellist.append(level.Level.id)
    return levellist

def get_level_list_by_section(session, section_id):
    levelstatement = select(Schema.Level).filter_by(section=section_id)
    levelresult = session.execute(levelstatement).all()
    levellist = []
    for level in levelresult:
        levellist.append(level.Level.name)
    return levellist

def get_password_by_user_id(session, user_id):
    passwordstatement = select(Schema.Password).filter_by(user=user_id)
    results = session.execute(passwordstatement).all()
    return results

def compare_password(session, user_id, compare):
    passwordstatement = select(Schema.Password).filter_by(user=user_id)
    results = session.execute(passwordstatement).all()
    match = False
    for result in results:
        if compare == result.Password.password:
            match = True
    return match
