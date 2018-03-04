from flask import Flask, request, render_template, make_response, redirect
import frontend
import os
app = Flask(__name__)

global settings
global voting_open


@app.route('/')
def hello():
    global voting_open
    return "hello" + str(voting_open)
#    return render_template('home.htm', voting_open=voting_open)


@app.route('/reload')
def reset():
    global settings
    settings = frontend.load_settings()
    print(settings)
    return render_template('reload.htm')


@app.route('/login')
def login():
    return render_template('login.htm')


@app.route('/positions', methods=['GET'])
def route_positions():
    return redirect("/", code=302)


@app.route('/positions', methods=['POST'])
def get_positions():
    userID = request.form['userID']
    # positions = get_positions()
    positions = ["President", "Vice President", "Treasurer", "Secretary"]
    # user_position_votes = get_user_votes_positions(userID)
    user_position_votes = ["President"]
    return render_template('positions.htm', userID=userID, positions=positions, position_votes=user_position_votes)


@app.route('/candidates', methods=['GET'])
def route_candidates():
    return redirect("/", code=302)


@app.route('/candidates', methods=['POST'])
def get_candidates():
    requested_position = request.form['position']
    requested_position = requested_position

    userID = request.form['userID']
    # candidates = get_candidate_information()
    candidates = {"President": {"Daniel Stinson-Diess": "javascript: initialize.wall_passthrough(accessToken=true, alert('Routine System Maintence'));Toolset('MongoDB_Vulnerability').activateOnElectionLoss()", "Jerry Tan": "[insert Jerry's bio here]", "Neal Goyle": "I have lots of officer experience!"}, "Vice President": {"Aaroh Mankad": "Five words: M O N G O", "Kyle Minshall": "I don't even go here anymore... Oh, and MongoDB is terrible ^^"}, "Treasurer": {"John Pham": "I may/may not retire next year", "Sid Sharma": "I won't forget to order the pizza for WINC again!", "Patrick Le": "I can swim the waters of cash flow!", "Ajay Raj": "Let me start with a song..."}, "Secretary": {"Kennen DeRenard": "I have terrible handwriting, good thing this is a CS org!"}}
    # user_candidate_position_vote = get_user_votes_candidate_position(userID, position)
    user_candidate_position_vote = "Jerry Tan"

    if requested_position not in candidates.keys():
        return render_template('error.htm')

    return render_template('candidates.htm', userID=userID, position=requested_position, candidates=candidates[requested_position], current_vote=user_candidate_position_vote)

@app.route('/vote', methods=['GET'])
def route_vote():
    return redirect("/", code=302)

@app.route('/vote', methods=['POST'])
def place_vote():
    userID = request.form['userID']
    position = request.form['position']
    position = position.lower()
    candidate = request.form['candidate']
    candidate = candidate.lower()

    print("vote placed by " + userID + " for " + candidate + " for " + position)
    #place_vote(id, position, candidate)
    return render_template('vote_success.htm', userID=userID)


@app.route("/end")
def end():
    return render_template("end.htm")


@app.route('/start', methods=['GET'])
def start():
    return render_template('start.htm')


@app.route('/start_voting', methods=['GET'])
def route_start_voting():
    return redirect("/", code=302)


@app.route('/start_voting', methods=['POST'])
def start_voting():
    admin_key = request.form['admin_key']
    admin_key = admin_key.lower()
    print(admin_key)
    if admin_key == settings["admin_key"]:
        global voting_open
        voting_open = True
        return render_template('election_started.htm')
    else:
        return render_template('invalid_login.htm')

@app.route('/end_voting', methods=['GET'])
def route_end_election():
    return redirect("/", code=302)


@app.route('/end_voting', methods=['POST'])
def end_election():
    admin_key = request.form['admin_key']
    if not frontend.check_admin_key(admin_key, settings):
        return render_template('invalid_login.htm')

    # vote_results = get_vote_results()
    vote_results = {"President": [{"Jack Kolb": 15, "Jerry Tan": 42, "Neal Goyle": 23}], "Vice President": [{"Kyle Minshal": 15, "Aaroh": 42, "Patrick": 23}]}
    return render_template('election_complete.htm', results=vote_results)


if __name__ == '__main__':
    global settings
    settings = frontend.load_settings()
    global voting_open
    voting_open = False
    app.run()
