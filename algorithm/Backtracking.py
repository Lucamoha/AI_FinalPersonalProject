from algorithm.utils import *

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

def Backtracking(start: str, des: str, max_dept = 30):
    def solve(current, visited, path):
        if current == des:
            return path + [current]
        if len(path) > max_dept:
            return []
        
        neighbors = get_neighbors(current)

        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                result = solve(neighbor, visited, path + [current])
                if result:                                                                                                                          
                    return result
                visited.remove(neighbor)
        
        return []
    
    visited = set([start])
    path = [start]

    return solve(start, visited, path)