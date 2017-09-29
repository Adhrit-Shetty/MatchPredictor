#!/usr/local/bin/python3
"""
    Emulating characteristics and behaviour
    of a generic Offense player.
"""

from .Player import Player

class Offense(Player):
    def __init__(self, id, rating):
        super().__init__(id, rating)
        self.chance_creation = 0
        self.chance_conversion = 0 
        self.key_passes = 0
        self.offensive_defense = 0
        self.fouls_conceded = 0 
        self.penalty_conversion = 0
    
    def __str__(self):
        return '\nPlayer {} (Offense) [{}]:'.format(self.id, self.rating) + \
        '\nChance Creation = {}'.format(self.chance_creation) + \
        '\nChance Conversion = {}'.format(self.chance_conversion) + \
        '\nKey Passes = {}'.format(self.key_passes) + \
        '\nOffensive Defense = {}'.format(self.offensive_defense) + \
        '\nFouls Conceded = {}'.format(self.fouls_conceded) + \
        '\nPenalty Conversion = {}'.format(self.penalty_conversion)