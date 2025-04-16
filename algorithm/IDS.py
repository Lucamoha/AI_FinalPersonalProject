from algorithm.utils import *

def dls(state, depth, visited, parent, des):
    if depth == 0:
        return state == des
    if state in visited:
        return False

    visited.add(state)

    index = state.index('0')
    x, y = divmod(index, 3)
    for dx, dy in moves:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_index = new_x * 3 + new_y
            new_state = list(state)
            new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
            new_state_str = ''.join(new_state)

            if new_state_str not in visited:
                parent[new_state_str] = state
                if dls(new_state_str, depth - 1, visited, parent, des):
                    return True

    return False


def ids(start: str, des: str):
    depth = 0
    while True:
        visited = set()
        parent = {start: None}
        if dls(start, depth, visited, parent, des):
            solution = []
            state = des
            while state is not None:
                solution.append(state)
                state = parent.get(state)
            return solution[::-1]
        depth += 1