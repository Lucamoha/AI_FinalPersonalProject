from algorithm.utils import *

def SAHC(start: str, des: str): # Steepest Ascent-Hill Climbing
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

    if min(nh) < h:
        next_state = SAHC(neighbors[nh.index(min(nh))], des)
        if next_state:
            return [current] + next_state

    return []