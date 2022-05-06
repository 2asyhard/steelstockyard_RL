from get_env_info import draw
import datetime

initial_states = [[[0,0,0],[1,1,1],[2,2,2]],
                 [[0,0,0],[1,2,3],[1,2,3]],
                 [[0,0,0],[1,2,3],[4,1,3]],
                 [[0,0,0],[1,2,3],[4,5,1]],
                 [[0,0,0],[1,2,3],[4,5,6]]]

graph_infos = dict()


for initial_state in initial_states:
    print('-' * 100)
    start_time = datetime.datetime.now()
    for row in initial_state:
        print(row)
    print()
    total_states, terminal_states = draw(initial_state)
    print()
    print(f"소요시간: {datetime.datetime.now()-start_time}")
    graph_infos[total_states] = terminal_states/total_states

print('='*100)
for key, item in graph_infos.items():
    print(f"전체 state의 개수: {key} / terminal state의 비율: {item}")