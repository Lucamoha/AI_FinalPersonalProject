
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
limitStep = 10000


def mahattan(i: int, start: str, des: str):
    x1, y1 = divmod(start.index(str(i)), 3)
    x2, y2 = divmod(des.index(str(i)), 3)
    return abs(x1 - x2) + abs(y1 - y2)


def heuristic(state: str, des: str):
    return sum(mahattan(int(c), state, des) for c in state if c != '0')