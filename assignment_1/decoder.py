def path_find(mdp, state):
    if state.index in mdp.end:
        return "Solved"
    best_actions = []
    best_value = nxt_value(state, state.optimal_action.index, mdp)
    for action in state.actions:
        if best_value == nxt_value(state, action.index, mdp):
            best_actions.append(action.index)
    if len(best_actions) == 1:
        direction(best_actions[0])
        return path_find(mdp, nxt_value(state, best_actions[0], mdp))
    else:
        while True:
            possible_values = []
            for action in best_actions:
                nxt_state = nxt_value(state, action, mdp)
                future_value = max_val(nxt_state, mdp)
                possible_values.append(future_value)
            if len(set(possible_values)) != 1:
                best_possible_value = max(possible_values)
                best_action = best_actions[possible_values.index(best_possible_value)]
                direction(best_action)
                return path_find(mdp, nxt_value(state, best_action, mdp))


def max_val(state, mdp):
    possible_values = []
    for i in range(3):
        possible_values.append(nxt_value(state, i, mdp).value)
    return max(possible_values)

def direction(action):
    if action == 0:
        print("N")
    elif action == 1:
        print("S")
    elif action == 2:
        print("E")
    else:
        print("W")


def nxt_value(state, action_ind, mdp):
    nxt_state = state.actions[action_ind].nxt_states[0]
    return mdp.state_set[nxt_state]
