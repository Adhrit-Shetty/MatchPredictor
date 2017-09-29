#!/usr/local/bin/python3
"""
    Emulating characteristics and behaviour
    of a generic Goalkeeper.
"""

from .Player import Player

class Goalkeeper(Player):
    def __init__(self, id, rating):
        super().__init__(id, rating)
        self.clean_sheets = 0
        self.saves_to_attempts = 0
        self.penalty_stopping = 0
        self.penalty_conversion = 0
    
    def __str__(self):
        return '\nPlayer {} (Goalkeeper) [{}]:'.format(self.id, self.rating) + \
        '\nClean Sheets = {}'.format(self.clean_sheets) + \
        '\nSaves to Attempt = {}'.format(self.saves_to_attempts) + \
        '\nPenalty Stopping = {}'.format(self.penalty_stopping) + \
        '\nPenalty Conversion = {}'.format(self.penalty_conversion)