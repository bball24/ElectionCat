import json


# list of users
def get_users():
    users = []
    with open("databases/idlist.json") as id_list_file:
        users = json.load(id_list_file)
    return users

# list of positions
def get_positions():
    positions = []
    with open('databases/candidates.json') as candidates_file:
       data = json.load(candidates_file)
       positions = list(data.keys())
    return positions


def get_votes():
    votes = {}
    with open('databases/votes.json') as votes_file:
       votes = json.load(votes_file)
    return votes

# list of positions the user has voted for
def get_user_votes_positions(userID):
    userID = str(userID)
    positions = []
    with open('databases/votes.json') as votes_file:
       data = json.load(votes_file)
       positions = list(data[userID].keys())
    return positions

# names/bios of all the candidates
def get_candidate_information():
    candidates = {}
    with open('databases/candidates.json') as candidates_file:
       candidates = json.load(candidates_file)
    return candidates

# name of person the user voted for a position
def get_user_votes_candidate_position(userID, position):
    userID = str(userID)
    with open('databases/votes.json') as votes_file:
        data = json.load(votes_file)
        if userID not in list(data.keys()):
            return "none"

        if position in list(data[userID].keys()):
            positions = data[userID][position]
        else:
            return "none"
    return positions

# add new vote to the dictionary
def place_vote(userID, position, candidate):
    print(userID)
    print(position)
    print(candidate)
    userID = str(userID)
    with open('databases/votes.json') as votes_file:
       data = json.load(votes_file)
       data[userID][position] = candidate

    with open('databases/votes.json', "w") as votes_file:
       json.dump(data, votes_file)
    return

# get the vote results
def get_vote_results():
    results = {}
    votes = get_votes()
    for user in list(votes.keys()):
        for position in list(votes[user].keys()):
            if position not in list(results.keys()):
                results[position] = {}
            if votes[user][position] not in list(results[position].keys()):
                results[position][votes[user][position]] = 1
            else:
                results[position][votes[user][position]] = str(int(results[position][votes[user][position]]) + 1)
    return results