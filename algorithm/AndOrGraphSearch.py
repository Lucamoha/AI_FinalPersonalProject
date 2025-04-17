from algorithm.utils import *

def AndOrGraphSearch(start: str, des: str, max_depth: int = 100):
    def or_search(state, path, depth):
        if state == des:
            return [state]

        if state in path or depth >= max_depth:
            return 'failure'

        index = state.index('0')
        x, y = divmod(index, 3)

        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_index = new_x * 3 + new_y
                new_state = list(state)
                new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
                new_state_str = ''.join(new_state)

                if new_state_str in path:
                    continue

                results = [new_state_str]
                plan = and_search(results, path + [state], depth + 1)
                if plan != 'failure':
                    return [state] + plan

        return 'failure'

    def and_search(states, path, depth):
        full_plan = []
        for s in states:
            subplan = or_search(s, path, depth)
            if subplan == 'failure':
                return 'failure'
            
            if full_plan and subplan[0] == full_plan[-1]:
                full_plan += subplan[1:]
            else:
                full_plan += subplan
        return full_plan

    try:
        plan = or_search(start, [], 0)
        return plan if plan != 'failure' else []
    except Exception as e:
        return []

