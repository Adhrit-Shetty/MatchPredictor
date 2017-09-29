#!/usr/local/bin/python3
"""
    Emulating characteristics and behaviour of a generic and specific Players.
"""

class Player():
    """
        Emulating characteristics and behaviour of a generic Player.
    """
    def __init__(self, id, rating):
        self.id = id
        self.rating = rating

class Goalkeeper(Player):
    """
        Emulating characteristics and behaviour of a Goalkeeper.
    """
    def __init__(self, id, rating):
        super().__init__(id, rating)
        self.saves_to_attempts = 0
        self.penalty_stopping = 0
        self.aggression = 0
        self.penalty_conversion = 0
    
    def __str__(self):
        return '\nPlayer {} (Goalkeeper) [{}]:'.format(self.id, self.rating) + \
        '\nSaves to Attempt = {}'.format(self.saves_to_attempts) + \
        '\nPenalty Stopping = {}'.format(self.penalty_stopping) + \
        '\nAggression = {}'.format(self.aggression) + \
        '\nPenalty Conversion = {}'.format(self.penalty_conversion)

class Defender(Player):
    """
        Emulating characteristics and behaviour of a Defender.
    """
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

class Midfielder(Player):
    """
        Emulating characteristics and behaviour of a Midfielder.
    """
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

class Forward(Player):
    """
        Emulating characteristics and behaviour of a Forward.
    """
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
