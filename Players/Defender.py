#!/usr/local/bin/python3
"""
    Emulating characteristics and behaviour
    of a generic Defender.
"""

from .Player import Player

class Defender(Player):
    def __init__(self, id, rating):
        super().__init__(id, rating)
        self.passing = 0
        self.interceptions = 0
        self.aggression = 0 
        self.penalty_conversion = 0
    
    def __str__(self):
        return '\nPlayer {} (Defender) [{}]:'.format(self.id, self.rating) + \
        '\nPassing = {}'.format(self.passing) + \
        '\nInterception = {}'.format(self.interceptions) + \
        '\nAggression = {}'.format(self.aggression) + \
        '\nPenalty Conversion = {}'.format(self.penalty_conversion)