import flask
import datetime
import custom_forms
from sqlalchemy.orm import Session
from DBStuff import find_data, add_data, filter_data, engine, data_manipulations, update_data, secret_stuff

app = flask.Flask(__name__)
app.secret_key = secret_stuff.app_key

@app.route('/', methods=('GET', 'POST'))
def hello_world():
    return flask.redirect('/leaderboard')

@app.route('/tttime/<id>')
def tttime(id):
    with Session(engine) as session:
        tttime = find_data.get_tttime_by_id(session, id)
        track_name = find_data.get_level_name(session, tttime.TTTime.level)
        time = data_manipulations.convert_seconds(tttime.TTTime.time)
        lap1 = data_manipulations.convert_seconds(tttime.TTTime.lap1)
        lap2 = data_manipulations.convert_seconds(tttime.TTTime.lap2)
        lap3 = data_manipulations.convert_seconds(tttime.TTTime.lap3)
        proof = tttime.TTTime.proof
    return flask.render_template('tttime.html',
                                 track_name=track_name,
                                 time=time,
                                 lap1=lap1,
                                 lap2=lap2,
                                 lap3=lap3,
                                 proof=proof)

@app.route('/submitgame', methods=('GET', 'POST'))
def submitgame():
    form = custom_forms.SelectForm()
    with Session(engine) as session:
        choices = []
        for item in find_data.get_games_list(session):
            choices.append(item.Game.name)
    form.field.choices = choices
    form.field.label = "Game"
    if flask.request.method == 'POST' and form.validate():
        with Session(engine) as session:
            game_id = find_data.get_game_ids(session, form.field.data)[0].Game.id
            return flask.redirect(f"/submitsection?game={game_id}")
    return flask.render_template('selectgame.html', form=form)

@app.route('/submitsection', methods=('GET', 'POST'))
def submitsection():
    gameparam = flask.request.args.get('game')
    if not gameparam:
        return "GET OUTTA HERE YOU DONT GOT A GAME"
    form = custom_forms.SelectForm()
    with Session(engine) as session:
        choices = ["All"]
        for item in find_data.get_section_list_by_game(session, gameparam):
            choices.append(item)
    form.field.choices = choices
    form.field.label = "Section"
    if flask.request.method == 'POST' and form.validate():
        if form.field.data != "All":
            with Session(engine) as session:
                section_id = find_data.get_section_ids(session, form.field.data)[0].Section.id
                return flask.redirect(f"/submit?game={gameparam}&section={section_id}")
        else:
            return flask.redirect(f"/submit?game={gameparam}")
    return flask.render_template('selectgame.html', form=form)

@app.route('/leaderboard')
def leaderboard():
    run_list = []
    with Session(engine) as session:
        run_list = filter_data.get_all_high_scores(session)
    table_contents = '<tr><th>TRACK</th><th>PLAYER</th><th>TIME</th></tr>'
    for item in run_list:
        with Session(engine) as session:
            track = find_data.get_level_name(session, item.TTTime.level)
            player = find_data.get_user_display_name(session, item.TTTime.user)
            time_value = data_manipulations.convert_seconds(item.TTTime.time)
            level_id = item.TTTime.id
            time = time_value
            add_string = f"<tr><td>{track}</td><td>{player}</td><td><a href='/tttime/{level_id}'>{time_value}</a></td><tr>"
            table_contents += add_string
    return flask.render_template('leaderboard.html', table=flask.Markup(table_contents))

@app.route('/user/edit', methods=('GET', 'POST'))
def user_edit():
    form = custom_forms.UserEdit()
    if flask.request.method == 'POST' and form.validate():
        with Session(engine) as session:
            userid = find_data.get_user_ids(session, str(form.username.data))[0]
            if userid:
                user_id = userid.User.id
                if find_data.compare_password(session, user_id, form.secret_code.data):
                    if form.new_name.data and form.new_name.data != '':
                        update_data.update_user_display_name(session, user_id, form.new_name.data)
                    if form.new_pass1.data == form.new_pass2.data and form.new_pass1.data != '':
                        update_data.update_user_password(session, user_id, form.new_pass1.data)
        return flask.redirect("/")
    return flask.render_template('useredit.html', form=form)

@app.route('/user/<id>')
def user_pbs(id):
    run_list = []
    with Session(engine) as session:
        run_list = filter_data.get_all_high_scores(session)
    table_contents = '<tr><th>TRACK</th><th>PLAYER</th><th>TIME</th></tr>'
    for item in run_list:
        with Session(engine) as session:
            track = find_data.get_level_name(session, item.TTTime.level)
            player = find_data.get_user_name(session, item.TTTime.user)
            time_value = data_manipulations.convert_seconds(item.TTTime.time)
            level_id = item.TTTime.id
            time = time_value
            add_string = f"<tr><td>{track}</td><td>{player}</td><td><a href='/tttime/{level_id}'>{time_value}</a></td><tr>"
            table_contents += add_string
    return flask.render_template('leaderboard.html', table=flask.Markup(table_contents))


@app.route('/submit', methods=('GET', 'POST'))
def submit():
    form = custom_forms.TimeSubmit()
    gameparam = flask.request.args.get('game')
    sectionparam = flask.request.args.get('section')
    if gameparam and sectionparam:
        with Session(engine) as session:
            choices = find_data.get_level_list_by_section(session, sectionparam)
    elif gameparam:
        with Session(engine) as session:
            choices = find_data.get_level_list_by_game(session, gameparam)
    else:
        choices = [1, 2, 3, 4]
    form.track.choices = choices
    if flask.request.method == 'POST' and form.validate():
        with Session(engine) as session:
            userids = find_data.get_user_ids(session, str(form.username.data))[0]
            if userids:
                user_id = userids.User.id
                if find_data.compare_password(session, user_id, form.secret_code.data):
                    level_id = find_data.get_level_ids(session, form.track.data)[0].Level.id
                    time = data_manipulations.convert_long_time(form.time.data)
                    lap1 = data_manipulations.convert_long_time(form.lap1.data)
                    lap2 = data_manipulations.convert_long_time(form.lap2.data)
                    lap3 = data_manipulations.convert_long_time(form.lap3.data)
                    proof = form.proof.data
                    timestamp = datetime.datetime.now()
                    add_data.add_tttime(session, level_id, user_id, time, lap1, lap2, lap3, proof, timestamp)
                else:
                    return "BAD SECRET CODE OOPS"
            else:
                return "THAT USERNAME DOESNT EXIST?????"
        return flask.redirect('/leaderboard')
    return flask.render_template('submit.html', form=form)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
