import numpy as np
from random import random, randint, shuffle, choice
import matplotlib.pyplot as plt

height_world = 7
length_world = 10
num_states = height_world * length_world
num_actions = 4
# pos_agent = np.array([0, 0])
wind_array = np.array([0, 0, 0, 1, 1, 1, 2, 2, 1, 0])
north = np.array([0, -1])
south = np.array([0, 1])
west = np.array([-1, 0])
east = np.array([1, 0])
north_east = north + east
south_east = south + east
north_west = north + west
south_west = north + east
alpha = 0.5
e = 0.1
start = np.array([0, 3])
end = np.array([7, 3])
reward = -1
terminal_reward = 0
gamma = 1


# north, south, west, east correspond to 0, 1, 2, 3


def nxt_state(pos, action, stochasticity = False):
    if action == 0:
        action = north
    elif action == 1:
        action = south
    elif action == 2:
        action = west
    elif action == 3:
        action = east
    elif action == 4:
        action = north_east
    elif action == 5:
        action = south_east
    elif action == 6:
        action = north_west
    elif action == 7:
        action = south_west
    pos_nxt = pos + action
    if pos_nxt[0] < 0 or pos_nxt[0] > length_world - 1:
        return pos
    if pos_nxt[1] < 0 or pos_nxt[1] > height_world - 1:
        return pos
    pos_nxt[1] -= wind_array[pos[0]]
    if stochasticity:
        random_list = [-1, 0, 1]
        pos_nxt[1] += choice(random_list)
    if pos_nxt[1] < 0 or pos_nxt[1] > height_world - 1:
        pos_nxt[1] = 0
        return pos_nxt
    return pos_nxt


def final_policy(state_action_matrix):
    return np.argmax(state_action_matrix, axis=1)


def state_index(state):
    return length_world * state[1] + state[0]


def probability(e):
    if random() < e:
        return "explore"
    else:
        return "greedy"


def reward_func(state):
    if state[0] == end[0] and state[1] == end[1]:
        return terminal_reward
    else:
        return reward


def greedy_action_select(row, value):
    all_max = []
    max_value = max(row)
    for i in range(len(row)):
        if row[i] == max_value:
            all_max.append(i)
    shuffle(all_max)
    return all_max[0]


def e_greedy_policy(state, state_action_matrix, e=0):
    if probability(e) == "greedy":
        index = state_index(state)
        row = list(state_action_matrix[index])
        max_value = max(row)
        return greedy_action_select(row, max_value)
    else:
        return randint(0, num_actions - 1)


def expected_value(state, state_action_matrix, actions):
    exp_val = 0
    for action in range(actions):
        if action == e_greedy_policy(state, state_action_matrix):
            exp_val += (1 - e) * (state_action_matrix[state_index(state)][action])
        else:
            return (e / (actions)) * (state_action_matrix[state_index(state)][action])
    return exp_val


def sarsa(alpha, e, max_iter):
    state_action_matrix = np.zeros((num_states, num_actions))
    episode_data = []
    time_data = []
    episode_num = 0
    time_step_num = 0
    for _ in range(max_iter):
        pos_agent = start
        action = e_greedy_policy(pos_agent, state_action_matrix, e)
        episode_num += 1
        while pos_agent[0] != end[0] or pos_agent[1] != end[1]:
            time_step_num += 1
            episode_data.append(episode_num)
            time_data.append(time_step_num)
            agent_reward = reward_func(pos_agent)
            pos_agent_new = nxt_state(pos_agent, action)
            action_new = e_greedy_policy(pos_agent_new, state_action_matrix, e)
            new_q_value = state_action_matrix[state_index(pos_agent_new)][action_new]
            old_q_value = state_action_matrix[state_index(pos_agent)][action]
            state_action_matrix[state_index(pos_agent)][action] += alpha * (
                    agent_reward + gamma * new_q_value - old_q_value)
            pos_agent = pos_agent_new
            action = action_new

    plt.plot(time_data, episode_data)
    plt.xlabel("Time Steps")
    plt.ylabel("Episodes")
    plt.title("sarsa")
    plt.show()
    return state_action_matrix


def q_learning(alpha, e, max_iter):
    state_action_matrix = np.zeros((num_states, num_actions))
    episode_data = []
    time_data = []
    episode_num = 0
    time_step_num = 0
    for _ in range(max_iter):
        pos_agent = start
        episode_num += 1
        while pos_agent[0] != end[0] or pos_agent[1] != end[1]:
            action = e_greedy_policy(pos_agent, state_action_matrix, e)
            time_step_num += 1
            episode_data.append(episode_num)
            time_data.append(time_step_num)
            agent_reward = reward_func(pos_agent)
            pos_agent_new = nxt_state(pos_agent, action, True)
            action_new = e_greedy_policy(pos_agent_new, state_action_matrix)
            new_q_value = state_action_matrix[state_index(pos_agent_new)][action_new]
            old_q_value = state_action_matrix[state_index(pos_agent)][action]
            state_action_matrix[state_index(pos_agent)][action] += alpha * (
                    agent_reward + gamma * new_q_value - old_q_value)
            pos_agent = pos_agent_new

    plt.plot(time_data, episode_data)
    plt.xlabel("Time Steps")
    plt.ylabel("Episodes")
    plt.title("q-learning")
    plt.plot(time_data, episode_data)
    plt.show()
    return state_action_matrix


def expected_sarsa(alpha, e, max_iter):
    state_action_matrix = np.zeros((num_states, num_actions))
    episode_data = []
    time_data = []
    episode_num = 0
    time_step_num = 0
    for _ in range(max_iter):
        pos_agent = start
        episode_num += 1
        while pos_agent[0] != end[0] or pos_agent[1] != end[1]:
            action = e_greedy_policy(pos_agent, state_action_matrix, e)
            time_step_num += 1
            episode_data.append(episode_num)
            time_data.append(time_step_num)
            agent_reward = reward_func(pos_agent)
            pos_agent_new = nxt_state(pos_agent, action)
            # action_new = e_greedy_policy(pos_agent_new, state_action_matrix)
            old_q_value = state_action_matrix[state_index(pos_agent)][action]
            state_action_matrix[state_index(pos_agent)][action] += alpha * (
                    agent_reward + gamma * expected_value(pos_agent_new, state_action_matrix, num_actions) - old_q_value)
            pos_agent = pos_agent_new

    plt.plot(time_data, episode_data)
    plt.xlabel("Time Steps")
    plt.ylabel("Episodes")
    plt.title("expected sarsa")
    plt.show()
    return state_action_matrix


matrix1 = q_learning(alpha, e, 200)
matrix2 = sarsa(alpha, e, 200)
matrix3 = expected_sarsa(alpha, e, 200)
# Username: 2onXJuYzzf

# Database name: 2onXJuYzzf

# Password: 3WviU2nTp7

# Server: remotemysql.com

# Port: 3306