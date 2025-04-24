from algorithm.utils import *
from collections import deque

def PartiallyObservation(StartStateList: list[str], DesStateList: list[str]):
    def getObservation(belief):
        return [state for state in belief if state[:3] == '123']

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
    queue = deque([(StartStateList, [])])

    steps = 0
    while queue and steps < limitStep:
        current_belief, path = queue.popleft()

        for state in current_belief:
            if isGoal(state):
                return path + [state]

        for move in moves:
            new_belief = []
            for state in current_belief:
                next_state = nextState(state, move)
                if next_state:
                    new_belief.append(next_state)

            # Lọc theo quan sát
            new_belief = getObservation(new_belief)

            # Lọc trùng và visited
            filtered_belief = [s for s in new_belief if s not in visited]
            if filtered_belief:
                visited.update(filtered_belief)
                queue.append((filtered_belief, path + [filtered_belief[0]]))

        steps += 1

    return []
