from algorithm.utils import *
import random

def Genetic(start: str, des: str, population_size=100, max_generations=500):
    def fitness(state):
        return sum(1 for i in range(9) if state[i] == des[i])

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

    population = [start]
    parent_map = {start: None}
    visited = set([start])

    for _ in range(population_size - 1):
        candidate = start
        path = [candidate]
        for _ in range(random.randint(5, 20)):  
            neighbors = get_neighbors(candidate)
            candidate = random.choice(neighbors)
            if candidate not in visited:
                visited.add(candidate)
                parent_map[candidate] = path[-1]
                path.append(candidate)
        population.append(candidate)

    for gen in range(max_generations):
        population = sorted(population, key=fitness, reverse=True)

        if des in population:
            path = []
            current = des
            while current is not None:
                path.append(current)
                current = parent_map.get(current)
            return path[::-1]

        survivors = population[:population_size // 4]
        new_population = []

        while len(new_population) < population_size:
            p = random.choice(survivors)
            path = [p]

            for _ in range(random.randint(3, 10)):
                neighbors = get_neighbors(path[-1])
                next_state = random.choice(neighbors)
                if next_state not in parent_map:
                    parent_map[next_state] = path[-1]
                    visited.add(next_state)
                path.append(next_state)

            new_population.append(path[-1])

        population = new_population

    return []