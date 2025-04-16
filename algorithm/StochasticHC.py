from algorithm.utils import *
import random

def StochasticHC(start: str, des: str): # Stochastic Hill Climbing
    current = start
    if current == des:
        return [current]
    
    h = heuristic(current, des)
    neighbors = []
    index = current.index('0')
    x, y = divmod(index, 3)
    for dx, dy in moves:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_index = new_x * 3 + new_y
            new_state = list(current)
            new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
            new_state_str = ''.join(new_state)
            neighbors.append(new_state_str)

    nh = []
    for state in neighbors:
        nh.append(heuristic(state, des))

    better_neighbors = []
    for i in range(len(neighbors)):
        if nh[i] < h:
            better_neighbors.append(neighbors[i])

    while better_neighbors:
        next_state = random.choice(better_neighbors)
        better_neighbors.remove(next_state)
        result = StochasticHC(next_state, des)
        if result:
            return [current] + result

    return []