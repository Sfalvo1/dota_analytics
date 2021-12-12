def write_json(data,path):
    """ takes `data` as a json and writes it to string `path`"""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f,indent = 4)
        f.close()
def get_game(match_id):
    """ Save game match json from dota API  """
    url = 'https://api.opendota.com/api/matches/'+str(match_id)
    r = requests.get(url).json()
    return r
def get_recent(player):
    """ Get the recent games for `player` """
    url = 'https://api.opendota.com/api/players/'+str(player)+'/recentMatches'
    r = requests.get(url).json()
    return r
def get_ids(player):
    """ Get a summary of all games for `player` """
    url = 'https://api.opendota.com/api/players/'+str(player)+'/matches/'
    r = requests.get(url).json()
    return r
def get_aspect(games, aspect, match_id = False):
    """ Returns a list containing aspect for each game """
    aspects = []
    if match_ids == True:
        for game in games:
            try:
                aspects.append((game['match_id'], game[str(aspect)]))
            except:
                aspects.append(None)
    else:
      for game in games:
          try:
              aspects.append(game[str(aspect)])
          except:
              aspects.append(None)
    return aspects

#BUG: `wins += bool(game['players'][party[0]]['win'])`
# this is bungus code, but not sure how to fix yet
# want this to add one if the party won the game, and zero ow
def party_win_rate(games, party):
    def is_party_in_game(game, party):
        game_players =[]
        for player in game['players']:
            try:
                game_players.append(str(player['account_id']))
            except:
                pass
        in_game = True
        for party_player in party:
            temp_bool = (party_player in game_players)
            in_game =  in_game & temp_bool
        return in_game
    total_games = 0
    wins = 0
    for game in games:
        if is_party_in_game(game, party):
            total_games += 1
            i = 0
            # got stuck here
            # its hard to access specific information for a particular
            # player, need to write some func or restructure data...
            # Why surround this in a bool cast?
            wins += bool(game['players'][party[0]]['win'])
    return wins / total_games

