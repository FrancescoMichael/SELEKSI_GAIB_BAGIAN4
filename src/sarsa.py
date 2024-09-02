import numpy as np

class SARSA:
    def __init__(self, n_states, n_actions, learning_rate, discount_factor, exploration):
        self.n_states = n_states
        self.n_actions = n_actions
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration = exploration
        self.qtable = np.zeros((n_states, n_actions))

    def pick_action(self, state): #epsilon greedy
        if np.random.rand() < self.exploration: #exploration
            return np.random.randint(0, self.n_actions)
        else: #exploitation
            return np.argmax(self.qtable[state])
        
    def update_qtable(self, curr_state, action, reward, next_state, next_action):
        # q(s, a) = q(s, a) + a(r + gamma * q(s', a') - q(s, a))
        self.qtable[curr_state, action] += self.learning_rate * (reward + (self.discount_factor * self.qtable[next_state, next_action]) - self.qtable[curr_state, action])

    def train(self, epochs, env):
        for _ in range(epochs):
            curr_state = env.reset()
            total_points = 0
            action = self.pick_action(curr_state)
            while not env.is_terminal(total_points):
                next_state, reward = env.step(curr_state, action)
                total_points += reward
                next_action = self.pick_action(next_state)
                self.update_qtable(curr_state, action, reward, next_state, next_action)
                curr_state = next_state
                action = next_action
    
    def get_path(self, env):
        curr_state = env.start_state
        path = [curr_state]
        total_points = 0
        while not env.is_terminal(total_points):
            action = np.argmax(self.qtable[curr_state])
            next_state, reward = env.step(curr_state, action)
            total_points += reward
            path.append(next_state)
            if next_state == env.hole_state or next_state == env.goal_state:
                path.append(env.reset_state)
                curr_state = env.reset_state
            else:
                curr_state = next_state
            
            if total_points >= env.winning_score or total_points <= env.losing_score:
                break
        return path, total_points
    
    def show_qtable(self):
        print(self.qtable)