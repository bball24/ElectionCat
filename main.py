from flask import Flask, request, render_template, redirect
import frontend
import backend
app = Flask(__name__)

global settings
settings = frontend.load_settings()
global voting_open
voting_open = False
global show_results
show_results = False


@app.route('/')
def hello():
    global voting_open
    if show_results:
        print(str(backend.get_vote_results()))
        results = backend.get_vote_results()
        new_results = {}
        for position in list(results.keys()):
            name = []
            votes = "0"
            for candidate in list(results[position].keys()):
                if int(results[position][candidate]) == int(votes):
                    new_results[position].append(candidate)
                    votes = results[position][candidate]
                elif int(results[position][candidate]) > int(votes):
                    new_results[position] = [candidate]
                    votes = results[position][candidate]
        print(str(new_results))
        return render_template("results.htm", org_logo=settings["organization_logo"], vote_results=new_results)
    return render_template('home.htm', org_logo=settings["organization_logo"], voting_open=voting_open)

@app.route('/m')
def m_hello():
    global voting_open
    if show_results:
        results = backend.get_vote_results()
        new_results = {}
        for position in list(results.keys()):
            name = []
            votes = "0"
            for candidate in list(results[position].keys()):
                if int(results[position][candidate]) == int(votes):
                    new_results[position].append(candidate)
                    votes = results[position][candidate]
                elif int(results[position][candidate]) > int(votes):
                    new_results[position] = [candidate]
                    votes = results[position][candidate]
        return render_template("m_results.htm", org_logo=settings["organization_logo"], vote_results=new_results)
    return render_template('m_home.htm', org_logo=settings["organization_logo"], voting_open=voting_open)


@app.route('/reload')
def reset():
    global settings
    settings = frontend.load_settings()
    print(settings)
    return render_template('reload.htm')


@app.route('/login')
def login():
    if voting_open:
        return render_template('login.htm')
    else:
        return redirect("/", code=302)

@app.route('/m_login')
def m_login():
    if voting_open:
        return render_template('m_login.htm')
    else:
        return redirect("/", code=302)

@app.route('/positions', methods=['GET'])
def route_positions():
    return redirect("/", code=302)


@app.route('/positions', methods=['POST'])
def get_positions():
    userID = request.form['userID']
    if show_results:
        return render_template("results.htm", vote_results=backend.get_vote_results())
    users = backend.get_users()
    if str(userID) not in users:
        return render_template("invalid_login.htm")
    positions = backend.get_positions()
    user_position_votes = backend.get_user_votes_positions(userID)
    return render_template('positions.htm', org_logo=settings["organization_logo"], userID=userID, positions=positions, position_votes=user_position_votes)

@app.route('/m_positions', methods=['GET'])
def m_route_positions():
    return redirect("/m", code=302)


@app.route('/m_positions', methods=['POST'])
def m_get_positions():
    userID = request.form['userID']
    if show_results:
        return render_template("m_results.htm", vote_results=backend.get_vote_results())
    users = backend.get_users()
    if str(userID) not in users:
        return render_template("m_invalid_login.htm")
    positions = backend.get_positions()
    user_position_votes = backend.get_user_votes_positions(userID)
    return render_template('m_positions.htm', org_logo=settings["organization_logo"], userID=userID, positions=positions, position_votes=user_position_votes)


@app.route('/candidates', methods=['GET'])
def route_candidates():
    return redirect("/", code=302)


@app.route('/candidates', methods=['POST'])
def get_candidates():
    requested_position = request.form['position']
    requested_position = requested_position

    userID = request.form['userID']
    candidates = backend.get_candidate_information()
    user_candidate_position_vote = backend.get_user_votes_candidate_position(userID, requested_position)

    if requested_position not in candidates.keys():
        return render_template('error.htm')
    return render_template('candidates.htm', org_logo=settings["organization_logo"], userID=userID, position=requested_position, candidates=candidates[requested_position], current_vote=user_candidate_position_vote)


@app.route('/m_candidates', methods=['GET'])
def m_route_candidates():
    return redirect("/m", code=302)


@app.route('/m_candidates', methods=['POST'])
def m_get_candidates():
    requested_position = request.form['position']
    requested_position = requested_position

    userID = request.form['userID']
    candidates = backend.get_candidate_information()
    user_candidate_position_vote = backend.get_user_votes_candidate_position(userID, requested_position)

    if requested_position not in candidates.keys():
        return render_template('error.htm')
    return render_template('m_candidates.htm', org_logo=settings["organization_logo"], userID=userID, position=requested_position, candidates=candidates[requested_position], current_vote=user_candidate_position_vote)

@app.route('/vote', methods=['GET'])
def route_vote():
    return redirect("/", code=302)

@app.route('/vote', methods=['POST'])
def place_vote():
    userID = request.form['userID']
    position = request.form['position']
    candidate = request.form['candidate']

    backend.place_vote(userID, position, candidate)
    return render_template('vote_success.htm', org_logo=settings["organization_logo"], userID=userID)

@app.route('/m_vote', methods=['GET'])
def m_route_vote():
    return redirect("/m", code=302)

@app.route('/m_vote', methods=['POST'])
def m_place_vote():
    userID = request.form['userID']
    position = request.form['position']
    candidate = request.form['candidate']

    backend.place_vote(userID, position, candidate)
    return render_template('m_vote_success.htm', org_logo=settings["organization_logo"], userID=userID)


@app.route("/stop")
def end():
    return render_template("end.htm", org_logo=settings["organization_logo"])


@app.route('/start', methods=['GET'])
def start():
    return render_template('start.htm', org_logo=settings["organization_logo"])


@app.route('/start_voting', methods=['GET'])
def route_start_voting():
    return redirect("/", code=302)


@app.route('/start_voting', methods=['POST'])
def start_voting():
    admin_key = request.form['admin_key']
    if admin_key == settings["admin_key"]:
        global voting_open
        voting_open = True
        global show_results
        show_results = False
        with open("databases/votes.json", "w") as votes_file:
            votes_file.write('{"": {}}')
        return render_template('election_started.htm', org_logo=settings["organization_logo"])
    else:
        return render_template('invalid_login.htm', org_logo=settings["organization_logo"])

@app.route('/end_voting', methods=['GET'])
def route_end_election():
    return redirect("/", code=302)


@app.route('/end_voting', methods=['POST'])
def end_election():
    admin_key = request.form['admin_key']
    if not frontend.check_admin_key(admin_key, settings):
        return render_template('invalid_login.htm')
    vote_results = backend.get_vote_results()
    global voting_open
    voting_open = False
    global show_results
    show_results = True
    return render_template('election_complete.htm', org_logo=settings["organization_logo"], results=vote_results)


if __name__ == '__main__':
    app.run()
