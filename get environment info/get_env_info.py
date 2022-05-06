import networkx as nx
import matplotlib.pyplot as plt
from env import *

def draw(Initial_state):
    action_list = make_action_list(Initial_state)
    state_list = get_neighbor_states(Initial_state, action_list)

    G = nx.Graph()
    terminal_states = 0
    i = 0

    G.add_node(i)
    G.nodes[i]['state'] = Initial_state
    G.nodes[i]['neighbor_states'] = get_neighbor_states(Initial_state, action_list)
    G.nodes[i]['terminal_state'] = check_game_over(Initial_state)
    G.nodes[i]['neighbor_nodes'] = set()
    if G.nodes[i]['terminal_state'] == True:
        terminal_states += 1

    # 모든 node를 생성하고 edge 연결
    while True:
        # 현재 nodes[i]의 neighbor_node의 모든 state를 대상으로 함
        for j in range(len(G.nodes[i]['neighbor_states'])):
            same_exist = False
            # G 그래프의 모든 node의 state와 현재 node[i]['state']를 비교해 새로운 node의 생성 여부 결정
            for k in range(len(G.nodes)):
                tmp_node_num = len(G.nodes)
                # neighbor_state와 같은 state가 다른 node중에 있는지 모든 node를 대상으로 확인
                if G.nodes[i]['neighbor_states'][j] == G.nodes[tmp_node_num-k-1]['state']:
                    # 같은 state를 가진 node가 있음
                    same_exist = True
                    # edge만 연결해줌
                    G.add_edge(i, tmp_node_num-k-1)
                    G.nodes[i]['neighbor_nodes'].add(tmp_node_num-k-1)
                    G.nodes[tmp_node_num-k-1]['neighbor_nodes'].add(i)
                    break

            # 같은 state가 없다면 새로운 node와 state, 연결된 edge를 생성
            if same_exist == False:
                # node 생성
                G.add_node(len(G.nodes))
                # edge 생성
                # 위에서 node를 생성하는 순간 len(G.node)가 1이 늘어났으므로 아래에서 부터 -1을 붙혀줘야함
                G.add_edge(i, len(G.nodes)-1)

                G.nodes[i]['neighbor_nodes'].add(len(G.nodes) - 1)
                # 속성 입력
                G.nodes[len(G.nodes)-1]['state'] = G.nodes[i]['neighbor_states'][j]
                G.nodes[len(G.nodes)-1]['neighbor_states'] = get_neighbor_states(G.nodes[len(G.nodes)-1]['state'], action_list)
                G.nodes[len(G.nodes)-1]['terminal_state'] = check_game_over(G.nodes[len(G.nodes)-1]['state'])
                G.nodes[len(G.nodes)-1]['neighbor_nodes'] = set()
                G.nodes[len(G.nodes)-1]['neighbor_nodes'].add(i)

        i += 1

        if G.nodes[i]['terminal_state'] == True:
            terminal_states += 1

        # 만약 더이상 확인 할 node가 없다면
        if len(G.nodes) == i+1:
            break

    print(f"전체 state의 개수: {len(G.nodes)}")
    print(f"terminal state의 개수: {terminal_states}")
    print(f"terminal states의 비율: {terminal_states/len(G.nodes)}")
    print()

    # 그래프 그리기
    # nx.draw(G, node_size=10)
    # plt.show()

    # 각 노드의 최적해를 구하기 위한 bfs
    def get_optimal_size(node_num):
        queue = [[node_num, 0]]
        visited = [node_num]
        while queue:
            [node, size] = queue.pop(0)
            if G.nodes[node]['terminal_state']:
                return size

            for n in G.nodes[node]['neighbor_nodes']:
                if n not in visited:
                    queue.append([n, size+1])
                    visited.append(n)

        return None

    opt_size_dict = {}

    # 그래프의 각 노드의 최적해를 구함함
    for node_num in range(len(G.nodes)):
        opt_size = get_optimal_size(node_num)
        if opt_size == None:
            print("None이 나옴")
        if opt_size not in opt_size_dict:
            opt_size_dict[opt_size] = 1
        else:
            opt_size_dict[opt_size] += 1


    print('각 최적해 별 노드의 개수')
    print(opt_size_dict) # 0인 경우 terminal state의 개수

    return len(G.nodes), terminal_states




