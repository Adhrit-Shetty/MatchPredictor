#!/usr/local/bin/python3
"""
    Emulating characteristics and behaviour
    of a generic Defense player.
"""

class Defense():
    def __init__(self, id, rating, key_interceptions, clearances, tackles_won, ball_retrieval, fouls_conceded, penalty_conversion):
        self.id = id
        self.rating = rating
        self.key_interceptions = key_interceptions
        self.clearances = clearances 
        self.tackles_won = tackles_won
        self.ball_retrieval = ball_retrieval
        self.fouls_conceded = fouls_conceded 
        self.penalty_conversion = penalty_conversion
    
    def __str__(self):
        return '\nPlayer {} (Defense) :'.format(self.id) + \
        '\nKey Interceptions = {}'.format(self.key_interceptions) + \
        '\nClearances = {}'.format(self.clearances) + \
        '\nTackles Won = {}'.format(self.tackles_won) + \
        '\nBall Retrieval = {}'.format(self.ball_retrieval) + \
        '\nFouls Conceded = {}'.format(self.fouls_conceded) + \
        '\nPenalty Conversion = {}'.format(self.penalty_conversion)