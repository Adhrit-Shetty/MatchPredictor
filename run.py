#!/usr/local/bin/python3
"""
    Logic script to simulate matches and prediction
"""

from random import randint, choice
from operator import attrgetter, itemgetter
from Players import Forward, Defender, Midfielder, Goalkeeper

id_key = attrgetter('id')

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

    def choose_player(self, keyword):
        chosen = {
            'forward': self.forwards,
            'midfielder': self.midfielders,
            'defender': self.defenders,
        }[keyword]
        return choice(range(min(chosen, key=id_key).id, max(chosen, key=id_key).id + 1))

    def get_player(self, id):
        if id in range(1, 3+1):
            return self.forwards[id-1]
        elif id in range(4, 7+1):
            return self.midfielders[id-4]
        elif id in range(8, 10+1):
            return self.defenders[id-8]
        else:
            return self.goalkeeper

def player_type(obj):
    if type(obj) == Forward:
        return 'Forward'
    elif type(obj) == Defender:
        return 'Defender'
    elif type(obj) == Midfielder:
        return 'Midfielder'
    else:
        return 'Goalkeeper'

def conflict(player_1, player_2):
    types = set([player_type(player_1), player_type(player_2)])
    if types == set(['Midfielder', 'Midfielder']):
        print('MM')
    elif types == set(['Forward', 'Defender']):
        print('FD')
    elif types ==  set(['Forward', 'Goalkeeper']):
        print('FG')

if __name__ == "__main__":
    team_1, team_2  = Team(1), Team(2)
    # current_team, opposing_team = team_1, team_2
    print(conflict(team_1.goalkeeper, team_1.forwards[0]))
    # for i in range(10):
        # opposing_player = 11 - current_player
        # if conflict(current_team.get_player(current_player), opposing_team.get_player(opposing_player)):