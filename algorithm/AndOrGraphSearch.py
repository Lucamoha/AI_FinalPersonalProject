from algorithm.utils import *

def AndOrGraphSearch(start: str, des: str):
    def or_search(state, path):
        if state == des:
            return [state]

        if state in path:
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

                results = [new_state_str]
                plan = and_search(results, path + [state])
                if plan != 'failure':
                    return [state] + plan

        return 'failure'

    def and_search(states, path):
        full_plan = []
        for s in states:
            subplan = or_search(s, path)
            if subplan == 'failure':
                return 'failure'
            
            if full_plan and subplan[0] == full_plan[-1]:
                full_plan += subplan[1:]
            else:
                full_plan += subplan
        return full_plan

    try:
        plan = or_search(start, [])
        return plan if plan != 'failure' else []
    except:
        return []

