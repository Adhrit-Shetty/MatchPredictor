#!/usr/local/bin/python3
"""
    Logic script to simulate matches and prediction
"""

from random import randint, choice, random
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

def choose_player(team, keyword=None, id=None):
    type, obj, result = '', None, 2
    if id is None:
        print('Is none')
        chosen = {
            'forward': team.forwards,
            'midfielder': team.midfielders,
            'defender': team.defenders,
        }[keyword]
        id, result = choice(range(min(chosen, key=id_key).id, max(chosen, key=id_key).id + 1)), 3
    if id in range(1, 3+1):
        type, obj = 'forward', team.forwards[id-1]
    elif id in range(4, 7+1):
        type, obj = 'midfielder', team.midfielders[id-4]
    elif id in range(8, 10+1):
        type, obj = 'defender', team.defenders[id-8]
    else:
        type, obj = 'goalkeeper', team.goalkeeper
    if result == 3:
        return id, type, obj
    elif result == 2:
        return type, obj

def next_line_of_action(type):
    if type == 'defender':
        return 'midfielder'
    elif type == 'midfielder':
        return 'forward'

def action_complete(player_1_type, player_1, player_2_type, player_2):
    x1, x2, attr1, attr2, types = 0, 0, '', '', set([player_1_type, player_2_type])
    if types == set(['midfielder', 'midfielder']):
        print('MM')
        attr1, attr2 = 'chance_creation', 'defense'
    elif types == set(['forward', 'defender']):
        print('FD')
        if player_1_type == 'forward':
            attr1, attr2 = 'chance_conversion', 'interceptions'
        else:
            attr1, attr2 = 'interceptions', 'chance_conversion'
    elif types ==  set(['forward', 'goalkeeper']):
        print('FG')
        attr1, attr2 = 'chance_conversion', 'saves_to_attempts'
    print('{} {} | {} {}'.format(attr1, attr2, attrgetter(attr1)(player_1), attrgetter(attr2)(player_2)))
    x1 = 0.7*attrgetter(attr1)(player_1)+ 0.2*random() #+0.1*Team Advantage
    x2 = 0.7*attrgetter(attr2)(player_2) + 0.2*random() #+0.1*Team Advantage
    print('[{} {}]'.format(x1, x2))
    if x1 > x2:
        return True
    return False

def foul(player_1, player_2):
    x1 = 0.4*player_1.aggression + 0.6*random()
    x2 = 0.4*player_2.aggression + 0.6*random()
    print('{} {}'.format(x1, x2))
    if x2 > x1 and x2 > 0.5:
        return True # Player_2 overpowers Player_1
    return False # Player_2 cannot overpower Player_1

if __name__ == "__main__":
    team_1, team_2  = Team(1), Team(2)
    current_team, opposing_team = team_1, team_2
    current_player_id, current_player_type, current_player = choose_player(current_team, keyword='defender')
    # print(action_complete(team_1.forwards[0], team_1.goalkeeper))
    for i in range(10):
        print('in')
        opposing_player_id = 11 - current_player_id
        opposing_player_type, opposing_player = choose_player(opposing_team, id=opposing_player_id)
        foul_committed = foul(current_player, opposing_player)
        print('FOUL - {}'.format(foul_committed))
        if opposing_player_type == 'goalkeeper' or not foul_committed:
            print('Either keep or no foul')
            # Checking if current player with possession completes action against opposing player
            action_possible = action_complete(current_player_type ,current_player, opposing_player_type, opposing_player)
            if action_possible:
                if current_player_type == 'forward':
                    opposing_player_type, opposing_player = choose_player(opposing_team, id=11) # Goalkeeper
                    foul_committed_keeper = foul(current_player, opposing_player)
                    if foul_committed_keeper:
                        print('Goalkeeper fouled')
                    else:
                        goal_possible = action_complete(current_player_type ,current_player, opposing_player_type, opposing_player)
                        if goal_possible:
                            print('Golaazooo')
                        else:
                            print('Goal saved')
                        # Swap
                        temp = current_team
                        current_team = opposing_team
                        opposing_team = temp
                        current_player_obj = choose_player(current_team, keyword='defender')
                        current_player_id, current_player_type, current_player = current_player_obj
                        continue
                else:
                    print('Pass completed to next line')
                    current_player_obj = choose_player(current_team, keyword=next_line_of_action(current_player_type))
                    current_player_id, current_player_type, current_player = current_player_obj
                    print(current_player_obj)
        elif foul_committed:
            pass
        if i == 4:
            break