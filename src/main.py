from environment import Environment
from qlearning import QLearning
from sarsa import SARSA

# Environment
env = Environment()

# Q-Leaning
print("Q-Learning:")
qlearning = QLearning(n_states = 10, n_actions = 2, learning_rate = 0.8, discount_factor = 0.9, exploration = 0.5)
qlearning.train(epochs = 1000, env = env)
qlearning_path, qlearning_total_scores = qlearning.get_path(env)
qlearning.show_qtable()
print(f"Path: {qlearning_path}")
print(f"Total scores: {qlearning_total_scores}\n")

# SARSA
print("SARSA:")
sarsa = SARSA(n_states = 10, n_actions = 2, learning_rate = 0.8, discount_factor = 0.9, exploration = 0.5)
sarsa.train(epochs = 1000, env = env)
sarsa_path, sarsa_total_scores = sarsa.get_path(env)
sarsa.show_qtable()
print(f"Path: {sarsa_path}")
print(f"Total scores: {sarsa_total_scores}")