import numpy as np
from copy import deepcopy

# Environment for steel stockyard
# 가능한 action을 구함
def make_action_list(state):
    action_list = []  # action의 종류
    for i in range(len(state[0])):
        for j in range(len(state[0])):
            if i != j:  # 강재를 빼는 stack과 넣는 stack이 달라야 함, 리스트의 크기는 num_stack*(num_stack)이 됨
                action_list.append([1, i, j])  # stack i 에서 stack j로 강재를 옮김

    return action_list

# 가능한 action을 구함[1 or 0, from stack, to stack]를 출력
def get_valid_moves(state, action_list):
    valid_moves = deepcopy(action_list)
    stack_size = []
    # 각 stack의 강재 갯수 확인
    for i in range(len(state[0])):
        tmp_stack_size = 0
        for j in range(len(state)):
            if state[j][i] != 0:
                tmp_stack_size += 1
        stack_size.append(tmp_stack_size)

    for i in range(len(stack_size)):
        for j in range(len(valid_moves)):
            # 만약 i번째 stack에 강재가 0개이고, j번째 action의 강재를 빼는 stack이 i번째 stack이라면
            # 해당 action은 불가능한 action으로 설정
            if stack_size[i] == 0 and valid_moves[j][1] == i:
                valid_moves[j][0] = 0
            # 만약 i번째 stack에 강재가 max_stack개이고, j번째 action의 강재를 쌓는 stack이 i번째 stack이라면
            # 해당 action은 부가능한 action으로 설정
            if stack_size[i] == len(state) and valid_moves[j][2] == i:
                valid_moves[j][0] = 0

    return valid_moves

# 가능한 action
def get_valid_action_index(valid_moves):
    valid_action_index = []
    for i in range(len(valid_moves)):
        if valid_moves[i][0] == 1:
            valid_action_index.append(i)

    return valid_action_index

# 강재를 옮기는 함수
def play_action(state, action_index, action_list):
    # action은 (1*2) array, action[0]은 뺄 강재가 있는 stack의 번호/action[1]은 강재를 쌓을 stack의 번호

    rot_action_list = np.rot90(action_list, 3)
    new_action_list = []
    new_action_list.append(rot_action_list[1])
    new_action_list.append(rot_action_list[2])
    new_action_list = np.rot90(new_action_list, 1)
    action = new_action_list[action_index]

    target_plate = 0
    out_zone_tier = -1  # 강재를 빼는 stack의 층 수(이동 작업 전)
    in_zone_tier = -1  # 강재가 들어가는 stack의 층 수(이동 작업 후), stack의 max로 꽉 차있으면 -1

    for i in range(len(state)):  # 빼는 강재의 높이(index로) 구하기
        if state[i][action[0]] != 0:
            out_zone_tier = i
            break

    for i in range(1, len(state) + 1):  # 강재를 쌓는 stack의 강재가 쌓일 높이(index로) 구하기
        if state[-i][action[1]] == 0:  # 강재가 max로 차 있지 않은다면 아래 문구 실행
            in_zone_tier = len(state) - i  # index 구하기
            break

    if in_zone_tier == -1 or out_zone_tier == -1:
        pass
    else:
        for i in range(len(state)):  # 강재를 빼는 작업
            if state[i][action[0]] != 0:
                target_plate = state[i][action[0]]
                state[i][action[0]] = 0
                break

        for i in range(1, len(state) + 1):  # 강재를 쌓는 작업
            if state[-i][action[1]] == 0:
                in_zone_tier = len(state) - i  # 강재가 쌓인 index 구하기
                state[-i][action[1]] = target_plate
                break

    return state

# 한번의 action을 통해 생성 가능한 state 구하기
def get_neighbor_states(state, action_list):
    neighbor_states = []
    valid_moves = get_valid_moves(state, action_list)
    valid_action_index = get_valid_action_index(valid_moves)

    for i in range(len(valid_action_index)):
        tmpstate = deepcopy(state)
        tmpstate = deepcopy(play_action(tmpstate, valid_action_index[i], action_list))
        neighbor_states.append(tmpstate)

    return neighbor_states

# terminal state 여부 확인
def check_game_over(state):
    column = len(state[0])
    row = len(state)

    for i in range(column):
        for j in range(row - 1):  # j는 4층까지 있지만 비교는 1,2/2,3/3,4 층을 비교하므로 3개만 필요
            if state[j][i] > state[j + 1][i]:
                return False # 선별 미완료 시 반환 값

    return True