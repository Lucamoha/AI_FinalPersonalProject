from algorithm.utils import *


def idaStar(start: str, des: str):
    def search(path, g, bound):
        state = path[-1]
        f = g + heuristic(state, des)
        if f > bound:
            return f
        if state == des:
            return path
        min_bound = float('inf')
        index = state.index('0')
        x, y = divmod(index, 3)
        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_index = new_x * 3 + new_y
                new_state = list(state)
                new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
                new_state_str = ''.join(new_state)
                if new_state_str not in path:
                    path.append(new_state_str)
                    t = search(path, g + 1, bound)
                    if isinstance(t, list):
                        return t
                    if t < min_bound:
                        min_bound = t
                    path.pop()
        return min_bound

    bound = heuristic(start, des)
    path = [start]
    while True:
        t = search(path, 0, bound)
        if isinstance(t, list):
            return t
        if t == float('inf'):
            return []
        bound = t