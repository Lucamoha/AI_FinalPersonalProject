moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
limitStep = 10000

def countInversions(state: str) -> int:
    """
    Đếm số nghịch đảo trong một trạng thái.
    Nghịch đảo là khi một số lớn hơn đứng trước một số nhỏ hơn (không tính số 0).
    """
    inversions = 0
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            if state[i] != '0' and state[j] != '0' and state[i] > state[j]:
                inversions += 1
    return inversions

def isSolvable(state: str, des: str = "123456780") -> bool:
    """
    Kiểm tra xem một trạng thái có thể giải được hay không bằng cách so sánh với trạng thái đích.
    Trạng thái đầu và đích phải có cùng tính chất về số nghịch đảo (cùng chẵn hoặc cùng lẻ).
    """
    return countInversions(state) % 2 == countInversions(des) % 2

def randomState(num: int = 10):
    import random
    
    states = []
    for _ in range(num):
        state = list('012345678')
        random.shuffle(state)
        state = ''.join(state)
        states.append(state)
    
    return states

def randomStateWithFixed(position: int, value: str, num: int = 10):
    """
    Tạo các trạng thái ngẫu nhiên với các số cố định ở vị trí chỉ định.
    """
    import random
    
    if position < 0 or position > 8 or position + len(value) > 9:
        raise ValueError("Vị trí không hợp lệ hoặc chuỗi giá trị quá dài")
    
    states = []
    remaining_digits = ''.join(d for d in '012345678' if d not in value)
    
    for _ in range(num):
        remaining_list = list(remaining_digits)
        random.shuffle(remaining_list)
        
        state_list = remaining_list[:position] + list(value) + remaining_list[position:]
        state = ''.join(state_list[:9])
        
        states.append(state)
    
    return states

def mahattan(i: int, start: str, des: str):
    x1, y1 = divmod(start.index(str(i)), 3)
    x2, y2 = divmod(des.index(str(i)), 3)
    return abs(x1 - x2) + abs(y1 - y2)


def heuristic(state: str, des: str):
    return sum(mahattan(int(c), state, des) for c in state if c != '0')