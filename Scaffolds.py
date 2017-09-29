from random import randint
from Players import Forward, Defender, Midfielder, Goalkeeper

class Team(): 
    def __init__(self, id):
        i, self.forwards, self.midfielders, self.defenders,self.goalkeeper = 1, [], [], [], None
        self.id = id
        for m in range(3):
            self.forwards.append(Forward(i, randint(60, 100)))
            i += 1
        for m in range(4):
            self.midfielders.append(Midfielder(i, randint(60, 100)))
            i += 1
        for m in range(3):
            self.defenders.append(Defender(i, randint(60, 100)))
            i += 1
        self.goalkeeper = Goalkeeper(i, randint(60, 100))
        
    def __str__(self):
        return '\nTeam {} :'.format(self.id) + \
        '\n\n~ Forwards ~ ' + '\n'.join([f.__str__() for f in self.forwards]) + \
        '\n\n~ Midfielders ~ ' + '\n'.join([m.__str__() for m in self.midfielders]) + \
        '\n\n~ Defenders ~ ' + '\n'.join([d.__str__() for d in self.defenders]) + \
        '\n\n~ Goalkeeper ~' + '\n' + self.goalkeeper.__str__()

def Match():
    def __init__(self, id, home, away, weather, toss, winner, score):
        self.id = id
        self.home = home
        self.away = away 
        self.weather = weather
        self.toss = toss 
        self.winner = winner 
        self.score = score

    def __str__(self):
        return '\nMatch {} :'.format(self.id) + \
        '\nHome team = {}'.format(self.home) + \
        '\nAway team = {}'.format(self.away) + \
        '\nWeather team = {}'.format(self.weather) + \
        '\nToss winner = {}'.format(self.toss) + \
        '\nGame winner = {}'.format(self.winner) + \
        '\nScore = {}'.format(self.score)