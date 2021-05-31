import numpy as np
import copy

class Environment:
    def __init__(self, num_stack=4, max_stack=4):
        self.num_stack = num_stack
        self.max_stack = max_stack
        self.actions = self.num_stack*(self.num_stack-1)
        self.s_test = np.array([[0, 0, 0, 0], [3, 3, 0, 2], [3, 2, 1, 1], [1, 2, 3, 2]], dtype=int)
        self.s0 = self._random_state()
        self.s = copy.deepcopy(self.s0)
        self.stopped = 0
        self._make_action_list()


    def _make_action_list(self):
        '''
        generate action list
        '''
        self.action_list = []
        for i in range(self.num_stack):
            for j in range(self.num_stack):
                if i != j:
                    self.action_list.append([i, j])


    def _random_state(self):
        '''
        generate random initial state for episode
        :return: random state
        '''
        while True:
            num_of_plates = np.random.randint(10, 13)
            type_of_plates = np.random.randint(4, 7)
            plates = []
            for _ in range(num_of_plates):
                plate_num = np.random.randint(1, type_of_plates)
                plates.append(plate_num)
            s = np.zeros([self.max_stack, self.num_stack], dtype=int)

            for i in range(self.num_stack):
                for j in range(self.max_stack):
                    if len(plates) != 0:
                        s[-i-1, -j-1] = plates[-1]
                        plates.pop()
            done, _ = self.is_rearrange_finish(s)
            if not done:
                break

        return s


    def reset(self):
        '''
        reset
        :return:
        '''

        self.s = copy.deepcopy(self._random_state())
        #self.s = copy.deepcopy(self.s0)
        return self.s


    def step(self, action):
        s = self.s
        s1 = self._move_plate(s, self.action_list[action])

        self.success = False
        d, r = self.is_rearrange_finish(s1)
        if d:
            self.success = True

        return s1, r, d,


    def is_rearrange_finish(self, state):
        reward = 0
        for i in range(self.num_stack):
            for j in range(self.max_stack-1):
                if state[j,i] > state[j+1,i]:
                    return False, reward
        reward = 100
        return True, reward


    def _move_plate(self, state, action):
        target_plate = 0
        out_zone_tier = -1
        in_zone_tier = -1
        new_state = copy.deepcopy(state)
        for i in range(self.max_stack):
            if state[i, action[0]] != 0:
                out_zone_tier = i
                break

        for i in range(1, self.max_stack + 1):
            if state[-i, action[1]] == 0:
                in_zone_tier = self.max_stack - i
                break

        if in_zone_tier == -1 or out_zone_tier == -1:
            #reward -= 1
            return new_state
        else:
            for i in range(self.max_stack):
                if new_state[i, action[0]] != 0:
                    target_plate = new_state[i, action[0]]
                    new_state[i, action[0]] = 0
                    break

            for i in range(1, self.max_stack+1):
                if new_state[-i, action[1]] == 0:
                    in_zone_tier = self.max_stack - i
                    new_state[-i, action[1]] = target_plate
                    break

            return new_state


    def impossible_actions(self):
        possible_actions = []
        empty = []
        full = []
        impossible_actions = []
        for i in range(self.num_stack):
            if self.s[:, i].max() == 0:
                empty.append(i)
            elif self.s[0, i] != 0:
                full.append(i)
        for i in range(self.actions):
            if not self.action_list[i][0] in empty and not self.action_list[i][1] in full:
                possible_actions.append(i)
            else:
                impossible_actions.append(i)
        return impossible_actions
