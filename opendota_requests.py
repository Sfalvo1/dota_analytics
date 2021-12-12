def write_json(data,path):
    """ takes `data` as a json and writes it to string `path`"""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f,indent = 4)
        f.close()
def request_game(match_id):
    """ Save game match json from dota API  """
    url = 'https://api.opendota.com/api/matches/'+str(match_id)
    r = requests.get(url).json()
    return r
def request_recents(player):
    """ Get the recent games for `player` """
    url = 'https://api.opendota.com/api/players/'+str(player)+'/recentMatches'
    r = requests.get(url).json()
    return r
def request_match_ids(player):
    """ Get a summary of all games for `player` """
    url = 'https://api.opendota.com/api/players/'+str(player)+'/matches/'
    r = requests.get(url).json()
    return r

