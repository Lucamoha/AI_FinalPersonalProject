import json
import copy
from collections import deque

with open('algorithm\\Constraint.json', 'r', encoding='utf-8') as file:
    constraint = json.load(file)

def ac3(domains, arcs):
    queue = deque(arcs)
    while queue:
        xi, xj = queue.popleft()
        if remove_inconsistent(xi, xj, domains):
            for xk in domains:
                if xk != xi and xk != xj:
                    queue.append((xk, xi))
    return True

def remove_inconsistent(xi, xj, domains):
    removed = False
    for x in domains[xi][:]:
        if not any(x != y for y in domains[xj]):
            domains[xi].remove(x)
            removed = True
    return removed

def create_domains_and_arcs():
    domains = {var: list(range(v["min"], v["max"] + 1)) for var, v in constraint["domains"].items()}
    arcs = [(xi, xj) for xi in domains for xj in domains if xi != xj]
    return domains, arcs

def is_complete(assignment):
    return len(assignment) == 9

def is_consistent(var, val, assignment):
    if constraint["unique"] and val in assignment.values():
        return False
    rng = constraint["domains"][var]
    return rng["min"] <= val <= rng["max"]

def select_unassigned(domains, assignment):
    return next((v for v in sorted(domains) if v not in assignment), None)

def assignment_str(assignment):
    return ''.join(str(assignment.get(str(i), 0)) for i in range(1, 10))

def backtrack(assignment, domains, path):
    path.append(assignment_str(assignment))
    if is_complete(assignment):
        return assignment

    var = select_unassigned(domains, assignment)
    for val in domains[var]:
        if is_consistent(var, val, assignment):
            new_assign = assignment.copy()
            new_assign[var] = val
            new_domains = copy.deepcopy(domains)
            new_domains[var] = [val]
            arcs = [(xk, var) for xk in new_domains if xk != var]
            if ac3(new_domains, arcs):
                result = backtrack(new_assign, new_domains, path)
                if result:
                    return result
    path.pop()
    return None

def Backtracking_AC3(start: str, des: str):
    domains, arcs = create_domains_and_arcs()
    ac3(domains, arcs)  # Rút gọn ban đầu
    path = []
    backtrack({}, domains, path)
    if path:
        return path[1:]
    return []