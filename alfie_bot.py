import random


class AlfieBot:
    max_rounds = 2500
    max_points = 1000
    max_dynamite = 100

    opponent_dynamite_heuristic = 1.1
    self_dynamite_heuristic = 0.7 # spread out self dynamite

    def __init__(self):
        self.dynamite = AlfieBot.max_dynamite

    def make_move(self, gamestate):
        rounds_passed = self.get_number_rounds(gamestate)

        opponent_dynamite_used = self.calculate_opponent_dynamite(gamestate)
        opponent_dynamite_left = AlfieBot.max_dynamite - opponent_dynamite_used

        self_points = self.get_self_points(gamestate)
        opponent_points = self.get_opponent_points(gamestate)

        max_rounds_remaining = AlfieBot.max_rounds - self.get_number_rounds(gamestate)
        min_rounds_remaining = self.get_minimum_rounds_left(gamestate)

        dynamite_chance_opponent = (opponent_dynamite_left / min_rounds_remaining) \
                                    * AlfieBot.opponent_dynamite_heuristic
        dynamite_chance_self = (self.dynamite / min_rounds_remaining) * AlfieBot.self_dynamite_heuristic

        random_value = random.random()

        if min_rounds_remaining <= self.dynamite:
            return 'D' # Use them!
        elif min_rounds_remaining <= opponent_dynamite_left:
            return 'W' # Stop them!

        if random_value < dynamite_chance_opponent * AlfieBot.opponent_dynamite_heuristic:
            return 'W'
        elif random_value < dynamite_chance_opponent + dynamite_chance_self and self.dynamite > 0:
            self.dynamite -= 1
            return 'D'
        else:
            return self.random_rps()

    def get_number_rounds(self, gamestate):
        return len(gamestate['rounds'])

    def get_opponent_points(self, gamestate):
        return self.get_points(gamestate, 'p2')

    def get_self_points(self, gamestate):
        return self.get_points(gamestate, 'p1')

    def get_points(self, gamestate, player):
        count = 0
        point_total = 1
        for round in gamestate['rounds']:
            winner = self.get_winner(round)
            if winner is None:
                point_total += 1
            else:
                if winner == player:
                    count += point_total
                point_total = 1
        return count

    def get_winner(self, round):
        p1_move = round['p1']
        p2_move = round['p2']

        if p1_move == p2_move:
            return None
        elif p1_move == 'R':
            if p2_move == 'D' or p2_move == 'P':  # Paper and dynamite beat rock
                return 'p2'
            else:
                return 'p1'  # Everything else loses to rock
        elif p1_move == 'P':
            if p2_move == 'D' or p2_move == 'S':  # Scissors and dynamite beat paper
                return 'p2'
            else:
                return 'p1'
        elif p1_move == 'S':
            if p2_move == 'D' or p2_move == 'R':  # Rock and dynamite beat scissors
                return 'p2'
            else:
                return 'p1'
        elif p1_move == 'W':
            if p2_move == 'D':
                return 'p1'
            else:
                return 'p2'
        elif p1_move == 'D':
            if p2_move == 'W':
                return 'p2'
            else:
                return 'p1'

    def calculate_opponent_dynamite(self, gamestate):
        count = 0
        for round in gamestate['rounds']:
            if round['p2'].upper() == 'D':
                count += 1
        return count

    def get_minimum_rounds_left(self, gamestate):
        p1_points = self.get_self_points(gamestate)
        p2_points = self.get_opponent_points(gamestate)

        rounds = gamestate['rounds']

        additional_points = 0
        for i in range(len(rounds) - 1, 0, -1):
            if self.get_winner(rounds[i]) is None:
                additional_points += 1
            else:
                break

        return max(1, AlfieBot.max_points - additional_points - max(p1_points, p2_points))

    def random_rps(self):
        return random.choice(['R', 'P', 'S'])
