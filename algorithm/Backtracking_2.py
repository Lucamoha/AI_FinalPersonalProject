import json

with open('algorithm\\Constraint.json', 'r', encoding='utf-8') as file:
    constraint = json.load(file)

def _is_valid(state: str):
    if not all(constraint["domains"][f"{i + 1}"]["min"] <= int(state[i]) <= constraint["domains"][f"{i + 1}"]["max"] for i in range(len(state))):
        return False
    if constraint["unique"] and len(set(state)) != 9:
        return False
    return True

def _Recursive_Backtracking(state: str):
    if _is_valid(state):
        return [state]
    
    for index in range(len(state)):
        if state[index] == '0':
            domains = range(constraint["domains"][f"{index + 1}"]["min"], constraint["domains"][f"{index + 1}"]["max"] + 1)
            for k in domains:
                if constraint["unique"] and str(k) in state:
                    continue
                new_state = state[:index] + str(k) + state[index + 1:]
                result = _Recursive_Backtracking(new_state)
                if result:
                    return [state] + result
            break
    
    return []

def Backtracking(start: str, des: str):
    return _Recursive_Backtracking('000000000')