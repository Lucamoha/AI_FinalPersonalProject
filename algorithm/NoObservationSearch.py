from algorithm.utils import *
from collections import deque

def NoObservation(StartStateList: list[str], DesStateList: list[str]):
    def isGoal(state: str):
        return state in DesStateList

    def nextState(state: str, action):
        dx, dy = action
        index = state.index('0')
        x, y = divmod(index, 3)
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_index = new_x * 3 + new_y
            state_list = list(state)
            state_list[index], state_list[new_index] = state_list[new_index], state_list[index]
            return ''.join(state_list)
        return None

    visited = set(StartStateList)
    queue = deque([(state, [state]) for state in StartStateList])

    steps = 0
    while queue and steps < limitStep:
        current_level = list(queue)
        queue.clear()

        for move in moves:
            for current_state, path in current_level:
                if isGoal(current_state):
                    return path

                new_state = nextState(current_state, move)
                if new_state and new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, path + [new_state]))

        steps += 1

    return []
