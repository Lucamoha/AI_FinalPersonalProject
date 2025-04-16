from algorithm.utils import *

def dfs(start: str, des: str):
    stack = [(start, [])]
    visited = set()

    while stack:
        state, path = stack.pop()
        if len(path) > limitStep:
            break
        if state == des:
            return path + [state]

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
                    stack.append((new_state_str, path + [state]))

    return []