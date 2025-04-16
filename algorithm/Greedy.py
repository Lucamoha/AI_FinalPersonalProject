from algorithm.utils import *
import heapq

def greedy(start: str, des: str):
    visited = set()
    parent = {}
    pq = [(heuristic(start, des), start)]
    visited.add(start)
    parent[start] = None

    while pq:
        _, state = heapq.heappop(pq)
        if state == des:
            solution = []
            while state is not None:
                solution.append(state)
                state = parent[state]
            return solution[::-1]

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
                    visited.add(new_state_str)
                    h = heuristic(new_state_str, des)
                    heapq.heappush(pq, (h, new_state_str))
                    parent[new_state_str] = state
    
    return []