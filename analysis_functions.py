#BUG: `wins += bool(game['players'][party[0]]['win'])`
# this is bungus code, but not sure how to fix yet
# want this to add one if the party won the game, and zero ow
def did_player_win(game,player):
    
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

def get_key_value(dicts, key):
""" Returns a list containing values corresponding to `key`
    for each dictionary in `dicts`
"""
key_values = []
for dictionary in dicts:
    key_values.append(dictionary.get(key))
return key_values