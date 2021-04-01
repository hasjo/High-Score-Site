from DBStuff import Schema, engine, find_data
from sqlalchemy import select

def get_high_scores_by_game_id(session, game_id):
    level_ids = find_data.get_level_ids_by_game(session, game_id)
    fastest_runs = []
    for level_id in level_ids:
        times = find_data.get_tttime_by_level(session, level_id)
        if times:
            fastest_runs.append(times[0])
    return fastest_runs

def get_high_scores_by_section_id(session, section_id):
    level_ids = find_data.get_level_ids_by_section(session, section_id)
    fastest_runs = []
    for level_id in level_ids:
        times = find_data.get_tttime_by_level(session, level_id)
        if times:
            fastest_runs.append(times[0])
    return fastest_runs

def get_high_scores_by_user_id(session, user_id):
    pass

def get_all_high_scores(session):
    level_ids = find_data.get_all_levels(session)
    fastest_runs = []
    for level_id in level_ids:
        times = find_data.get_tttime_by_level(session, level_id.Level.id)
        if times:
            fastest_runs.append(times[0])
    return fastest_runs
