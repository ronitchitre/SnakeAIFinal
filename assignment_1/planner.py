# SoC Assignment 1
# MDP Solver

import planner_class
import argparse
parser = argparse.ArgumentParser()
from math import inf


def value_func(state_ind, mdp):
    for i in mdp.state_set:
        if i.index == state_ind:
            return i.value
    print(state_ind)


def bellman_equation(state, action_index, mdp):
    total = 0
    for action in state.actions:
        if action.index == action_index:
            for nxt_state, reward, prob in action.action_func:
                try:
                    total += prob * (reward + mdp.dis_fac * value_func(nxt_state, mdp))
                except:
                    # print(prob, reward, mdp.dis_fac, value_func(nxt_state, mdp))
                    print("yay")
    return total


def value_iteration(mdp):
    ERR = 1000.0
    while not abs(ERR) <= 0.0000000000000001:
        for state in mdp.state_set:
            cur_max = -1*inf
            optimal_action = None
            # value = state.value
            old_value = state.value
            for action in state.actions:
                value = bellman_equation(state, action.index, mdp)
                if value > cur_max:
                    cur_max = value
                    optimal_action = action
            state.optimal_action = optimal_action
            state.value = cur_max
            if state.value == 0:
                pass
            else:
                ERR = min(float(abs(old_value - state.value)), ERR)
    return mdp

if __name__ == "__main__":
    parser.add_argument("--mdp", type = str)
    args = parser.parse_args()
    address = f"{args.mdp}"
    print(type(address))
    given_MDP = planner_class.data_reader(address)
    given_MDP = value_iteration(given_MDP)

    for state in given_MDP.state_set:
        print(state.value, state.optimal_action.index)