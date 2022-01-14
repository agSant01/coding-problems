"""
initial_state = [ 
        [2,1,1],    # row 1 
        [1,1,0],    # row 2
        [0,1,1]     # row 3
                    .... row n
    ]
"""
from typing import List, Tuple


"""
1. Get input data as a matrix of potatoes
2. Convert to a graph like structure
3. If there exists a node without neighbors and it is not rotten, 
    Then return -1
    Else continue
4. if none of the neiboring nodes are "contaminated" return -1
5. then....
"""


def getNeighbors(index_x, index_y) -> List[Tuple[int, int]]:
    return []


def is_rottable(input_data: List[List[int]]) -> int:
    iteration_required = -1
    _inner_input_data = input_data.copy()

    my_graph = dict()
    stack = []

    for i in range(len(_inner_input_data)):
        for j in range(len(_inner_input_data[0])):
            my_graph.update({(i, j): getNeighbors(i, j)})

            # initialize stack with all nodes
            stack.append((i, j))

    no_rotten_potato = True
    for node_indeces, neighbour_list in my_graph.items():
        # base case: found alone potatoe that is clean
        if len(neighbour_list) == 0 and _inner_input_data[node_indeces[0]][node_indeces[1]] == 1:
            return iteration_required

        # base case: look for a rotten potato
        if _inner_input_data[node_indeces[0]][node_indeces[1]] == 2:
            no_rotten_potato = False

    # if no roten potatoe, return -1
    if no_rotten_potato:
        return iteration_required

    visted_nodes_stack = []

    while len(stack) != 0:
        current_node = stack.pop()

        if _inner_input_data[current_node[0]][current_node[1]] == 2:
            # do something
            neighbour_list = my_graph.get(current_node)

            for neighbour_indeces in neighbour_list:
                value = _inner_input_data[neighbour_indeces[0]
                                          ][neighbour_indeces[1]]
                if value != 2:
                    _inner_input_data[neighbour_indeces[0]
                                      ][neighbour_indeces[1]] *= 2

        elif _inner_input_data[current_node[0]][current_node[1]] == 1:
            stack.append(current_node)

        iteration_required += 1

    return iteration_required
