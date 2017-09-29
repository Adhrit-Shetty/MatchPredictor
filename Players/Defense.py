#!/usr/local/bin/python3
"""
    Emulating characteristics and behaviour
    of a generic Defense player.
"""

from .Player import Player

class Defense(Player):
    def __init__(self, id, rating):
        super().__init__(id, rating)
        self.key_interceptions = 0
        self.clearances = 0 
        self.tackles_won = 0
        self.ball_retrieval = 0
        self.fouls_conceded = 0 
        self.penalty_conversion = 0
    
    def __str__(self):
        return '\nPlayer {} (Defense) [{}]:'.format(self.id, self.rating) + \
        '\nKey Interceptions = {}'.format(self.key_interceptions) + \
        '\nClearances = {}'.format(self.clearances) + \
        '\nTackles Won = {}'.format(self.tackles_won) + \
        '\nBall Retrieval = {}'.format(self.ball_retrieval) + \
        '\nFouls Conceded = {}'.format(self.fouls_conceded) + \
        '\nPenalty Conversion = {}'.format(self.penalty_conversion)