from algorithm.utils import *
import random

def SHC(start: str, des: str): # Simple Hill Climbing
    path = []
    current = start

    while True:
        path.append(current)

        if current == des:
            return path
        
        if len(path) > limitStep:
            return []
        
        neighbors = []
        index = current.index('0')
        x, y = divmod(index, 3)
        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_index = new_x * 3 + new_y
                new_state = list(current)
                new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
                new_state_str = ''.join(new_state)
                neighbors.append(new_state_str)

        h = heuristic(current, des)
        for state in neighbors:
            if heuristic(state, des) < h:
                current = state
                break