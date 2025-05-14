import random

def _randomState():
    return ''.join([str(random.randint(0, 8)) for _ in range(9)])

def _is_valid(state: str):
    if not all(0 <= int(i) <= 8 for i in state):
        return False
    if len(set(state)) != 9:
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