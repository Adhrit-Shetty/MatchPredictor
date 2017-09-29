#!/usr/local/bin/python3
"""
    Emulating characteristics and behaviour
    of a generic Goalkeeper.
"""

class Goalkeeper():
    def __init__(self, id, clean_sheets, saves_to_attempts, penalty_stopping, penalty_conversion):
        self.id = id
        self.clean_sheets = clean_sheets
        self.saves_to_attempts = saves_to_attempts 
        self.penalty_stopping = penalty_stopping
        self.penalty_conversion = penalty_conversion
    
    def __str__(self):
        return '\nPlayer {} (Goalkeeper) :'.format(self.id) + \
        '\nClean Sheets = {}'.format(self.clean_sheets) + \
        '\nSaves to Attempt = {}'.format(self.saves_to_attempts) + \
        '\nPenalty Stopping = {}'.format(self.penalty_stopping) + \
        '\nPenalty Conversion = {}'.format(self.penalty_conversion)