#!/usr/local/bin/python3
"""
    Emulating characteristics and behaviour
    of a generic Midfielder.
"""

from .Player import Player

class Midfielder(Player):
    def __init__(self, id, rating):
        super().__init__(id, rating)
        self.chance_creation = 0
        self.defense = 0
        self.aggression = 0 
        self.penalty_conversion = 0
    
    def __str__(self):
        return '\nPlayer {} (Midfielder) [{}]:'.format(self.id, self.rating) + \
        '\nChance Creation = {}'.format(self.chance_creation) + \
        '\nDefense = {}'.format(self.defense) + \
        '\nAggression = {}'.format(self.aggression) + \
        '\nPenalty Conversion = {}'.format(self.penalty_conversion)