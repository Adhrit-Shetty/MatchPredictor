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

    def update(self, stats):
        for id, stat in stats.items():
            if id in range(1, 3+1): # Forward
                self.forwards[id-1].chance_conversion = stats[id].shots['completed'] / stats[id].shots['attempted'] if stats[id].shots['attempted'] > 0 else 0
                self.forwards[id-1].defense = stats[id].tackles['completed'] / stats[id].tackles['attempted'] if stats[id].tackles['attempted'] > 0 else 0
                self.forwards[id-1].aggression = stats[id].tackles['foul'] / stats[id].tackles['attempted'] if stats[id].tackles['attempted'] > 0 else 0
                self.forwards[id-1].penalty_conversion = stats[id].penalties['completed'] / stats[id].penalties['attempted'] if stats[id].penalties['attempted'] > 0 else 0
            elif id in range(4, 7+1): # Midfielder
                self.midfielders[id-4].chance_creation = stats[id].passes['completed'] / stats[id].passes['attempted'] if stats[id].passes['attempted'] > 0 else 0
                self.midfielders[id-4].defense = stats[id].tackles['completed'] / stats[id].tackles['attempted'] if stats[id].tackles['attempted'] > 0 else 0
                self.midfielders[id-4].aggression = stats[id].tackles['foul'] / stats[id].tackles['attempted'] if stats[id].tackles['attempted'] > 0 else 0
                self.midfielders[id-4].penalty_conversion = stats[id].penalties['completed'] / stats[id].penalties['attempted'] if stats[id].penalties['attempted'] > 0 else 0
            elif id in range(8, 10+1): # Defender
                self.defenders[id-8].passing = stats[id].passes['completed'] / stats[id].passes['attempted'] if stats[id].passes['attempted'] > 0 else 0
                self.defenders[id-8].interceptions = stats[id].tackles['completed'] / stats[id].tackles['attempted'] if stats[id].tackles['attempted'] > 0 else 0
                self.defenders[id-8].aggression = stats[id].tackles['foul'] / stats[id].tackles['attempted'] if stats[id].tackles['attempted'] > 0 else 0
                self.defenders[id-8].penalty_conversion = stats[id].penalties['completed'] / stats[id].penalties['attempted'] if stats[id].penalties['attempted'] > 0 else 0
            else: # Goalkeeper
                self.goalkeeper.saves_to_attempts = stats[id].saves['completed'] / stats[id].saves['attempted'] if stats[id].saves['attempted'] > 0 else 0
                self.goalkeeper.penalty_stopping = stats[id].penalty_saves['completed'] / stats[id].penalty_saves['attempted'] if stats[id].penalty_saves['attempted'] > 0 else 0
                self.goalkeeper.aggression = stats[id].tackles['foul'] / stats[id].tackles['attempted'] if stats[id].tackles['attempted'] > 0 else 0
                self.goalkeeper.penalty_conversion = stats[id].penalties['completed'] / stats[id].penalties['attempted'] if stats[id].penalties['attempted'] > 0 else 0

class PlayerStatistics():
    def __init__(self, pid, team_id):
        self.pid = pid
        self.team_id = team_id
        if pid in range(1, 3+1): # Forward
            self.shots = {'completed': 0, 'attempted': 0}
            self.passes = {'completed': 0, 'attempted': 0}
        elif pid in range(4, 7+1): # Midfielder
            self.passes = {'completed': 0, 'attempted': 0}
        elif pid in range(8, 10+1): # Defender
            self.passes = {'completed': 0, 'attempted': 0}
        else:
            self.saves = {'completed': 0, 'attempted': 0}
            self.penalty_saves = {'completed': 0, 'attempted': 0}
        self.tackles = {'completed': 0, 'attempted': 0, 'foul':0}
        self.penalties = {'completed': 0, 'attempted': 0}

    def __str__(self):
        if self.pid in range(1, 3+1): # Forward
            string = '\nPlayer {} (Team {} Forward):'.format(self.pid, self.team_id)
            string += '\nShots Completed v/s Shots attempted = {} v/s {}'\
                .format(self.shots['completed'], self.shots['attempted'])
            string += '\nPasses Completed v/s Passes attempted = {} v/s {}'\
                .format(self.passes['completed'], self.passes['attempted'])
        elif self.pid in range(4, 7+1): # Midfielder
            string = '\nPlayer {} (Team {} Midfielder):'.format(self.pid, self.team_id)
            string += '\nPasses Completed v/s Passes attempted = {} v/s {}'\
                .format(self.passes['completed'], self.passes['attempted'])
        elif self.pid in range(8, 10+1): # Defender
            string = '\nPlayer {} (Team {} Defender):'.format(self.pid, self.team_id)
            string += '\nPasses Completed v/s Passes attempted = {} v/s {}'\
                .format(self.passes['completed'], self.passes['attempted'])
        else:
            string = '\nPlayer {} (Team {} Goalkeeper):'.format(self.pid, self.team_id)
            string += '\nSaves Completed v/s Saves attempted = {} v/s {}'\
                .format(self.saves['completed'], self.saves['attempted'])
            string += '\nPenalty Saves Completed v/s Penalty Saves attempted = {} v/s {}'\
                .format(self.penalty_saves['completed'], self.penalty_saves['attempted'])
        string += '\nTackles Completed v/s Tackles attempted = {} v/s {} => Fouls = {}'\
                .format(self.tackles['completed'], self.tackles['attempted'], self.tackles['foul'])
        string += '\nPenalties Completed v/s Penalties attempted = {} v/s {}'\
                .format(self.penalties['completed'], self.penalties['attempted'])
        return string

    def update(self, attribute_name, completed):
        attibutes = self.__dict__
        if attribute_name in attibutes.keys():
            attribute = getattr(self, attribute_name)
            attribute['attempted'] += 1
            if completed == 'foul':
                attribute['foul'] += 1
            elif completed:
                attribute['completed'] += 1

class TeamStatistics():
    def __init__(self, id):
        self.id = id
        self.stats = {i: PlayerStatistics(i, id) for i in range(1, 11+1)}

    def __str__(self):
        return '\nTeam {}:'.format(self.id) +\
            '\n'.join([self.stats[i].__str__() for i in sorted(self.stats.keys())])

    def update(self, pid, attribute_name, completed):
        self.stats[pid].update(attribute_name, completed)

class MatchStatistics():
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
