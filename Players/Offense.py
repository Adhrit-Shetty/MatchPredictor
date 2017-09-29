#!/usr/local/bin/python3
"""
    Emulating characteristics and behaviour
    of a generic Offense player.
"""

class Offense():
    def __init__(self, id, chance_creation, chance_conversion, key_passes, offensive_defense, fouls_conceded, penalty_conversion):
        self.id = id
        self.chance_creation = chance_creation
        self.chance_conversion = chance_conversion 
        self.key_passes = key_passes
        self.offensive_defense = offensive_defense
        self.fouls_conceded = fouls_conceded 
        self.penalty_conversion = penalty_conversion
    
    def __str__(self):
        return '\nPlayer {} (Offense) :'.format(self.id) + \
        '\nChance Creation = {}'.format(self.chance_creation) + \
        '\nChance Conversion = {}'.format(self.chance_conversion) + \
        '\nKey Passes = {}'.format(self.key_passes) + \
        '\nOffensive Defense = {}'.format(self.offensive_defense) + \
        '\nFouls Conceded = {}'.format(self.fouls_conceded) + \
        '\nPenalty Conversion = {}'.format(self.penalty_conversion)