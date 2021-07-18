class MDP:
    def __init__(self, state_num, action_num, state_set, start, end, continuing, dis_fac):
        self.state_num = state_num
        self.action_num = action_num
        self.state_set = state_set
        self.start = start
        self.end = end
        self.continuing = continuing
        self.dis_fac = dis_fac


class State:
    def __init__(self, index, max_actions, value=0):
        self.index = index
        self.max_actions = max_actions
        self.actions = []
        self.optimal_action = None
        self.value = 0
        for i in range(max_actions):
            action = Action(i)
            action.nxt_states = []
            action.rewards = []
            action.prob = []
            self.actions.append(action)


class Action:
    def __init__(self, index):
        self.index = index
        self.nxt_states = []
        self.rewards = []
        self.prob = []
        self.action_func = []

    def set_action_func(self):
        self.action_func = list(zip(self.nxt_states, self.rewards, self.prob))


def state_set(trans_inf, state_num, action_num):
    counter = 0
    result = []
    for i in range(state_num):
        state = State(i, action_num)
        while i == trans_inf[counter][0]:
            current_inf = (trans_inf[counter])
            state.actions[int(current_inf[1])].nxt_states.append(current_inf[2])
            state.actions[int(current_inf[1])].rewards.append(current_inf[3])
            state.actions[int(current_inf[1])].prob.append(current_inf[4])
            state.actions[int(current_inf[1])].set_action_func()
            counter += 1
            if counter >= len(trans_inf):
                break
        result.append(state)
    return result


def data_reader(address):
    data = open(address, "r")
    state_num = data.readline()
    state_num = int(state_num[10:])
    action_num = data.readline()
    action_num = int(action_num[11:])
    state_inf = []
    start = data.readline()
    start = int(start[-2])
    end = data.readline()
    end = list(map(int, list(end[4:].split())))
    all_transitions = False
    continuing = True
    while not all_transitions:
        trans_inf = data.readline()
        if trans_inf[0] != "m":
            trans_inf = list(map(float, list(trans_inf[11:].split())))
            state_inf.append(trans_inf)
        else:
            trans_inf = trans_inf[8:]
            if trans_inf[0] == "e":
                continuing = False
            all_transitions = True
    dis_fac = data.readline()
    dis_fac = float(dis_fac[10:])
    data.close()
    result = MDP(state_num, action_num, state_set(state_inf, state_num, action_num), start, end, continuing, dis_fac)
    return result


