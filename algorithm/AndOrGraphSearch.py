from algorithm.utils import *

def AndOrGraphSearch(start: str, des: str, max_depth=30):
    def get_neighbors(state):
        neighbors = []
        index = state.index('0')
        x, y = divmod(index, 3)
        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_index = new_x * 3 + new_y
                new_state = list(state)
                new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
                neighbors.append(''.join(new_state))
        return neighbors

    def OrSearch(state, path, depth):
        if state == des:
            return path + [state]

        if state in path or depth > max_depth:
            return None

        for neighbor in get_neighbors(state):
            result = AndSearch([neighbor], path + [state], depth + 1)
            if result is not None:
                return result
        return None

    def AndSearch(states, path, depth):
        full_path = path
        for state in states:
            result = OrSearch(state, full_path, depth)
            if result is None:
                return None
            full_path = result
        return full_path

    result = OrSearch(start, [], 0)
    return result if result else []
