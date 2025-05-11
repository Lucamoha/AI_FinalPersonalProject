from algorithm.utils import *
import numpy as np
import random
import math
import os

continue_learning = False # True nếu muốn tiếp tục học
tolerance = 0.01 # Ngưỡng dừng
alpha = 0.3  # Tốc độ học
gamma = 0.9  # Hệ số chiết khấu 
epsilon = 0.2  # Tỷ lệ khám phá
episodes = 1000 # Số vòng lặp học

if os.path.exists('algorithm/qtable.npy') or continue_learning:
    Q_table = np.load('algorithm/qtable.npy')
else:
    Q_table = np.zeros((math.factorial(9), 4))

start = ''
des = ''

def permutation_index(state: str) -> int:
    """Chuyển trạng thái thành chỉ số duy nhất"""
    state = list(state)
    index = 0
    for i in range(len(state)):
        # Đếm các phần tử nhỏ hơn state[i] nằm ở các vị trí sau nó
        count = sum(x < state[i] for x in state[i+1:])
        # Tính chỉ số dựa trên số các hoán vị còn lại
        index += count * math.factorial(len(state) - i - 1)
    return index

def take_action(state: str, action: tuple):
    """
    Thực hiện hành động trên trạng thái hiện tại và trả về trạng thái mới.
    """
    new_state = state
    index = state.index('0')
    x, y = divmod(index, 3)
    dx, dy = action
    new_x, new_y = x + dx, y + dy
    if 0 <= new_x < 3 and 0 <= new_y < 3:
        new_index = new_x * 3 + new_y
        new_state = list(state)
        new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
        new_state = ''.join(new_state)
    
    if new_state == des:
        return new_state, 10 # Thưởng khi đến đích
    else:
        return new_state, -1 # phạt

def choose_action(state: str) -> tuple:
    if random.uniform(0, 1) < epsilon:
        action = random.choice(moves)
    else:
        # Chọn hành động tốt nhất từ Q_table
        best_action = np.argmax(Q_table[permutation_index(state)])
        action = moves[best_action]
    
    return action

def return_path() -> list:
    """
    Trả về đường đi từ trạng thái hiện tại đến đích.
    """
    path = [start]
    state = start
    while state != des:
        action = np.argmax(Q_table[permutation_index(state)])
        new_state, _ = take_action(state, moves[action])
        path.append(new_state)
        state = new_state
    return path

def QLearning(_start: str, _des: str) -> list:
    global Q_table, start, des
    start = _start
    des = _des
    
    if not continue_learning:
        return return_path()

    for episode in range(episodes):
        state = start
        max_delta = 0

        for step in range(limitStep):
            action = choose_action(state)
            new_state, reward = take_action(state, action)

            idx = permutation_index(state)
            nidx = permutation_index(new_state)
            
            old_value = Q_table[idx, moves.index(action)]
            
            best_next_action = np.argmax(Q_table[nidx])
            Q_table[idx, moves.index(action)] += alpha * (reward + gamma * Q_table[nidx, best_next_action] - Q_table[idx, moves.index(action)])
            
            state = new_state

            # Tính delta tại bước hiện tại
            delta = abs(old_value - Q_table[idx, moves.index(action)])
            max_delta = max(max_delta, delta)
        
        print(f"Episode {episode + 1}/{episodes}, Max Delta: {max_delta}")
    
    np.save('qtable.npy', Q_table)
    return return_path()