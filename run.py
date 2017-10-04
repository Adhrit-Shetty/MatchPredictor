#!/usr/local/bin/python3
"""
    Logic script to simulate matches and prediction
"""

import sys
from random import randint, choice, random
from operator import attrgetter, itemgetter

from Players import Player, Forward, Defender, Midfielder, Goalkeeper
from Scaffolds import Team, TeamStatistics, MatchStatistics

id_key = attrgetter('id')

def choose_player(team, keyword=None, id=None):
    type, obj, result = '', None, 2
    if id is None:
        chosen = {
            'forward': team.forwards,
            'midfielder': team.midfielders,
            'defender': team.defenders
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
        print('Midfielder v/s Midfielder')
        attr1, attr2 = 'chance_creation', 'defense'
    elif types == set(['forward', 'defender']):
        if player_1_type == 'forward':
            print('Forward v/s Defender')
            attr1, attr2 = 'chance_conversion', 'interceptions'
        else:
            print('Defender v/s Forward')
            attr1, attr2 = 'interceptions', 'chance_conversion'
    elif types ==  set(['forward', 'goalkeeper']):
        print('Forward v/s Goalkeeper')
        attr1, attr2 = 'chance_conversion', 'saves_to_attempts'
    x1 = 0.4*attrgetter(attr1)(player_1) + 0.4*random() #+0.1*Team Advantage
    x2 = 0.4*attrgetter(attr2)(player_2) + 0.4*random() #+0.1*Team Advantage
    print('Attr = {:.02f}, {:.02f} | Comp = {:.02f}, {:.02f}'.format(attrgetter(attr1)(player_1), attrgetter(attr2)(player_2), x1, x2))
    if x1 > x2:
        return True
    return False

def foul(player_1, player_2):
    x1 = 0.4*player_1.aggression + 0.6*random()
    x2 = 0.4*player_2.aggression + 0.6*random()
    print('Foul analysis = x2({:.02f}) - x1({:.02f}) = {:.02f}'.format(x2, x1, x2-x1))
    if x2 - x1 > 0.25:
        return True # Player_2 overpowers Player_1
    return False # Player_2 cannot overpower Player_1

def penalty(forward, goalkeeper):
    x1 = 0.7*forward.penalty_conversion + 0.2*random() #+0.1*Team Advantage
    x2 = 0.7*goalkeeper.penalty_stopping + 0.2*random() #+0.1*Team Advantage
    if x1 > x2:
        return True # Golaazooo!
    return False # Goal saved!


# int teamAdvantageCalculator(current_match: match, prev_matches: match){
#   home_ct1 = home_ct2 = 0;
#   away_ct1 = away_ct2 = 0;
#   rainy_ct1 = rainy_ct2 = 0;
#   clear_ct1 = clear_ct2 = 0;
#   toss_ct1 = toss_ct2 = 0;
#   notoss_ct1 = notoss_ct2 = 0;
#   for (match in prev_matches){
#     if (match.winner == 1){
#       if (match.home == 1)
#           home_ct1 + +;
#       else
#           away_ct1 + +;
#       if (match.weather == 'rainy')
#           rainy_ct1 + +;
#       else
#           clear_ct1 + +;
#       if (match.toss == 1)
#           toss_ct1 + +;
#       else
#           notoss_ct1 + +;
#   }
#   else{
#       if (match.home == 2)
#           home_ct2 + +;
#       else
#           away_ct2 + +;
#       if (match.weather == 'rainy')
#           rainy_ct2 + +;
#       else
#           clear_ct2 + +;
#       if (match.toss == 2)
#           toss_ct2 + +;
#       else
#           notoss_ct2 + +;
#   }
#   total_matches + +;
# }
#
# sum1 = 0.5 * team1.rating;
# sum2 = 0.5 * team2.rating;
#
# if (current_match.home == 1){
#   sum1 += 0.25 * home_ct1;
#   sum2 += 0.25 * away_ct2;
# }
# else{
#   sum1 += 0.25 * away_ct1;
#   sum2 += 0.25 * home_ct2;
# }
# if (current_match.weather == 'rainy'){
#   sum1 += 0.15 * rainy_ct1;
#   sum2 += 0.15 * rainy_ct2;
# }
# else{
#   sum1 += 0.15 * clear_ct1;
#   sum2 += 0.15 * clear_ct2;
# }
# if (current_match.toss == 1){
#   sum1 += 0.1 * toss_ct1;
#   sum2 += 0.1 * notoss_ct2;
# }
# else{
#   sum1 += 0.1 * notoss_ct1;
#   sum2 += 0.1 * toss_ct2;
# }
#
# if (sum1 > sum2){
#   return 1;
# }
# else
# if (sum2 > sum1){
#   return 2;
# }
# else
#   return 0;
# return 1 means team_advantage of 1 will be 1 and 0 for zero;vice-versa if 2 returned;if 0 returned both have 0 team_advantage
#}


if __name__ == "__main__":
    print('\n\n\n\n')
    no_of_matches, no_of_plays = list(map(int, sys.argv[1:]))
    team_1, team_2 = Team(1), Team(2)
    team_1_stats, team_2_stats = TeamStatistics(1), TeamStatistics(2)
    matches = []
    for i in range(1, no_of_matches+1):
        home_team_id = randint(1,2)
        away_team_id = 1 if home_team_id == 2 else 2
        toss_winner = randint(1, 2)
        weather = 'rainy' if random() < 0.5 else 'clear'
        if toss_winner == 1:
            current_team, current_team_stats, opposing_team, opposing_team_stats = team_1, team_1_stats, team_2, team_2_stats
        else:
            current_team, current_team_stats, opposing_team, opposing_team_stats = team_2, team_2_stats, team_1, team_1_stats
        print('Current team id - {}'.format(current_team.id))
        play_count, goals = 0, {1:0, 2:0}
        current_player_id, current_player_type, current_player = choose_player(current_team, keyword='defender')
        while True:
            opposing_player_id = 11 - current_player_id
            opposing_player_type, opposing_player = choose_player(opposing_team, id=opposing_player_id)
            foul_committed = foul(current_player, opposing_player)
            print('~Foul value - {}~'.format(foul_committed))
            # Checking if defending player commits foul
            if not foul_committed:
                print('No foul committed in defending.')
                # Checking if current player with possession completes action against opposing player
                action_possible = action_complete(current_player_type ,current_player, opposing_player_type, opposing_player)
                if action_possible:
                    opposing_team_stats.update(opposing_player_id, 'tackles', False)
                    print('Action completion is possible.')
                    if current_player_type == 'forward':
                        print('Forward takes on the Goalkeeper next!')
                        opposing_player_type, opposing_player = choose_player(opposing_team, id=11) # Goalkeeper
                        foul_committed_keeper = foul(current_player, opposing_player)
                        if foul_committed_keeper:
                            print('Foul committed by Goalkeeper. Penalty!')
                            penalty_scored = penalty(current_player, opposing_player)
                            opposing_team_stats.update(11, 'tackles', 'foul')
                            if penalty_scored:
                                print('Golaazooo!')
                                goals[current_team.id] += 1
                                current_team_stats.update(current_player_id, 'penalties', True)
                                opposing_team_stats.update(11, 'penalty_saves', False)
                                print('\nScore - {}\n'.format(goals))
                            else:
                                print('Goal saved!')
                                current_team_stats.update(current_player_id, 'penalties', False)
                                opposing_team_stats.update(11, 'penalty_saves', True)
                        else:
                            print('Player shoots!')
                            goal_possible = action_complete(current_player_type, current_player, opposing_player_type, opposing_player)
                            if goal_possible:
                                print('Golaazooo!')
                                goals[current_team.id] += 1
                                current_team_stats.update(current_player_id, 'shots', True)
                                opposing_team_stats.update(11, 'saves', False)
                                print('\nScore - {}\n'.format(goals))
                            else:
                                print('Goal saved!')
                                current_team_stats.update(current_player_id, 'shots', False)
                                opposing_team_stats.update(11, 'saves', True)
                        # Possession switch
                        play_count += 1
                        current_team, opposing_team = opposing_team, current_team
                        current_team_stats, opposing_team_stats = opposing_team_stats, current_team_stats
                        current_player_obj = choose_player(current_team, keyword='defender')
                        current_player_id, current_player_type, current_player = current_player_obj
                        print('New current team id - {}'.format(current_team.id))
                        print('Play ends. Possession switch. NEXT play.\n\n\n\n')
                    else:
                        print('Pass completed to next line of action.')
                        current_team_stats.update(current_player_id, 'passes', True)
                        current_player_obj = choose_player(current_team, keyword=next_line_of_action(current_player_type))
                        current_player_id, current_player_type, current_player = current_player_obj
                        print('New Current player in line - {}'.format(current_player_type))
                else:
                    # Possession switch
                    current_team_stats.update(current_player_id, 'passes', False)
                    opposing_team_stats.update(opposing_player_id, 'tackles', True)
                    print('Lost Possession. Switching!')
                    current_team, opposing_team = opposing_team, current_team
                    current_team_stats, opposing_team_stats = opposing_team_stats, current_team_stats
                    current_player, current_player_type, current_player_id = opposing_player, opposing_player_type, opposing_player_id
                    print('New current team id - {}'.format(current_team.id))
            elif foul_committed:
                opposing_team_stats.update(opposing_player_id, 'tackles', 'foul')
                continue # Current player gets to continue after foul
            if play_count >= no_of_plays:
                break
        print('\nFinal score - {}\n'.format(goals))
        matches.append(MatchStatistics(i, home_team_id, away_team_id, weather, toss_winner, 1 if goals[1] > goals[2] else 2, goals))
        team_1.update(team_1_stats.stats)
        team_2.update(team_2_stats.stats)
    for m in matches:
        print(m)

    print(team_1)
    print(team_1_stats)
    print(team_2)
    print(team_2_stats)