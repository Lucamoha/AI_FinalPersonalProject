import random
import json

with open('algorithm\\Constraint.json', 'r', encoding='utf-8') as file:
    constraint = json.load(file)

def _randomState():
    return ''.join([str(random.randint(0, 8)) for _ in range(9)])

def _is_valid(state: str):
    if not all(constraint["domains"][f"{i + 1}"]["min"] <= int(state[i]) <= constraint["domains"][f"{i + 1}"]["max"] for i in range(len(state))):
        return False
    if constraint["unique"] and len(set(state)) != 9:
        return False
    return True

def testSearch(start: str, des: str):
    path = []
    visited = set()
    
    state = _randomState()
    path.append(state)
    visited.add(state)

    while not _is_valid(state):
        state = _randomState()
        if state not in visited:
            visited.add(state)
            path.append(state)
    return path