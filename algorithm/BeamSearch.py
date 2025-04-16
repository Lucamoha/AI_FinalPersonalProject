from algorithm.utils import *
from heapq import heappush, heappop

def BeamSearch(start: str, des: str, beam_width=3):
    queue = [(heuristic(start, des), [start])]
    visited = set()

    while queue:
        new_queue = []
        count = 0

        while queue and count < beam_width:
            _, path = heappop(queue)
            state = path[-1]

            if state == des:
                return path

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
                        new_path = path + [new_state_str]
                        heappush(new_queue, (heuristic(new_state_str, des), new_path))
            count += 1

        queue = sorted(new_queue)[:beam_width]

    return []