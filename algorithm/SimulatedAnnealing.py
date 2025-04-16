from algorithm.utils import *
import random
import math

def SimulatedAnnealing(start: str, des: str, max_iterations=10000, initial_temp=100.0, cooling_rate=0.995):
    current = start
    current_cost = heuristic(current, des)
    solution_path = [current]
    temperature = initial_temp

    for iteration in range(max_iterations):
        if current == des:
            return solution_path

        index = current.index('0')
        x, y = divmod(index, 3)
        neighbors = []

        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_index = new_x * 3 + new_y
                new_state = list(current)
                new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
                neighbors.append(''.join(new_state))

        if not neighbors:
            break

        next_state = random.choice(neighbors)
        next_cost = heuristic(next_state, des)
        delta = next_cost - current_cost

        if delta < 0 or random.random() < math.exp(-delta / temperature):
            current = next_state
            current_cost = next_cost
            solution_path.append(current)

        temperature *= cooling_rate

    return []