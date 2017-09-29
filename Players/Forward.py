#!/usr/local/bin/python3
"""
    Emulating characteristics and behaviour
    of a generic Forward.
"""

from .Player import Player

class Forward(Player):
    def __init__(self, id, rating):
        super().__init__(id, rating)
        self.chance_conversion = 0 
        self.defense = 0
        self.aggression = 0 
        self.penalty_conversion = 0
    
    def __str__(self):
        return '\nPlayer {} (Forward) [{}]:'.format(self.id, self.rating) + \
        '\nChance Conversion = {}'.format(self.chance_conversion) + \
        '\nDefense = {}'.format(self.defense) + \
        '\nAggression = {}'.format(self.aggression) + \
        '\nPenalty Conversion = {}'.format(self.penalty_conversion)