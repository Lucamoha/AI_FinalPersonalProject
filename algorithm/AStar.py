from algorithm.utils import *
import heapq

def aStar(start: str, des: str):
    visited = set()
    parent = {}
    g = {start: 0}  # g(n): Chi phí từ start đến state
    pq = [(heuristic(start, des), start)]
    parent[start] = None

    while pq:
        _, state = heapq.heappop(pq)

        if state == des:
            solution = []
            while state is not None:
                solution.append(state)
                state = parent[state]
            return solution[::-1]

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

                new_g = g[state] + 1  # Chi phí từ start đến new_state
                h = heuristic(new_state_str, des)
                f = new_g + h

                if new_state_str not in visited or new_g < g.get(new_state_str, float('inf')):
                    g[new_state_str] = new_g
                    heapq.heappush(pq, (f, new_state_str))
                    parent[new_state_str] = state
    
    return []