class Environment:
    def __init__(self, n_states = 10, start_state = 2, hole_state = 0, goal_state = 9, reset_state = 3, winning_score = 500, losing_score = -200):
        self.n_states = n_states
        self.start_state = start_state
        self.hole_state = hole_state
        self.goal_state = goal_state
        self.reset_state = reset_state
        self.winning_score = winning_score
        self.losing_score = losing_score
    
    def reset(self):
        return self.start_state

    def is_terminal(self, total_points):
        return total_points >= self.winning_score or total_points <= self.losing_score
    
    def take_action(self, state, action):
        if action == 0: #left
            return max(0, state - 1)
        else: #right
            return min(self.n_states - 1, state + 1)

    def get_reward(self, state):
        if state == self.hole_state:
            return -100
        elif state == self.goal_state:
            return 100
        else:
            return -1

    def step(self, state, action):
        next_state = self.take_action(state, action)
        reward = self.get_reward(next_state)
        return next_state, reward