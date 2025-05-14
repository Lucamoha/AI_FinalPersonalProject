def _is_valid(state: str):
    if not all(0 <= int(i) <= 8 for i in state):
        return False
    if len(set(state)) != 9:
        return False
    return True

def _Recursive_Backtracking(state: str, domains: set, des: str):
    if state == des:
        return [state]
    
    for Var in domains:
        for index in range(len(state)):
            if state[index] == '0':
                new_state = state[:index] + str(Var) + state[index + 1:]
                domains.discard(Var)
                result = _Recursive_Backtracking(new_state, domains, des)
                if result:
                    return [state] + result
                domains.add(Var)
    
    return []

def Backtracking(start: str, des: str):
    if not _is_valid(des):
        return []
    
    domains = {1, 2, 3, 4, 5, 6, 7, 8}
    des = des
    state = '000000000'

    return _Recursive_Backtracking(state, domains, des)