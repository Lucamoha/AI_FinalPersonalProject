import heapq
from collections import deque
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QColor, QFont
from PyQt6.QtCore import Qt, QTimer
import time
import random
import math


start = '265087431'
des = '123456780'

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

limitStep = 10000
DELAY = 500 #ms
totalTime = 0
data = ""


class PuzzleWidget(QtWidgets.QWidget):
    def __init__(self, parent=None, scale: float = 1, state: str = start):
        super().__init__(parent)
        self.solution = []
        self.scale = scale
        self.grid_size = 3  # Kích thước 3x3
        self.cell_size = int(110 * scale)  # Kích thước mỗi ô
        self.state = state  # Chuỗi biểu diễn trạng thái

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.next_step)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)

        # Đặt màu nền chính
        self.setStyleSheet("background-color: #F6F0F0;")

        size = self.cell_size - int(10 * self.scale)  # Kích thước ô
        margin = int(5 * self.scale)  # Khoảng cách giữa các ô

        offset_x = (self.width() - (self.grid_size * size) - (self.grid_size - 1) * margin) // 2
        offset_y = (self.height() - (self.grid_size * size) - (self.grid_size - 1) * margin) // 2

        for i in range(self.grid_size):
            for j in range(self.grid_size):
                num = self.state[i * self.grid_size + j]
                x = j * (size + margin) + offset_x
                y = i * (size + margin) + offset_y

                painter.setPen(Qt.PenStyle.NoPen)

                if num == '0':
                    painter.setBrush(QtGui.QBrush(QColor("#D5C7A3"), Qt.BrushStyle.SolidPattern))
                else:
                    painter.setBrush(QtGui.QBrush(QColor("#F2E2B1"), Qt.BrushStyle.SolidPattern))

                painter.drawRect(x, y, size, size)

                # Vẽ số lên ô (trừ ô trống)
                if num != '0':
                    painter.setFont(QFont("Arial", int(size // 3), QFont.Weight.Bold))
                    painter.setPen(QtGui.QColor("#333333"))  # Chỉ đặt pen khi vẽ số

                    text_rect = QtCore.QRect(x, y, size, size)
                    painter.drawText(text_rect, Qt.AlignmentFlag.AlignCenter, num)

    def solve(self, algorithm):
        global totalTime, data
        totalTime = 0
        data = ""

        self.solution = algorithm(start, des)

        if not self.solution:
            data = "No solution!"
            return
        
        data = f"Time: {totalTime}s\nSteps: {len(self.solution) - 1}\nPath:\n"
        t = 1
        for i in self.solution:
            data += (i + ("\n-> " if t % 9 == 0 else " -> "))
            t += 1
        data = data[:-4]
        self.timer.start(DELAY)

    def next_step(self):
        """Hiển thị từng bước di chuyển"""
        if self.solution:
            self.state = self.solution.pop(0)
            self.update()
        else:
            self.timer.stop()

    def stop_solution(self):
        """Dừng giải thuật"""
        self.state = start
        self.solution = []
        self.update()
        self.timer.stop()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.PuzzleWidget = PuzzleWidget(parent=self.centralwidget)
        self.PuzzleWidget.setGeometry(QtCore.QRect(280, 5, 360, 360))
        self.PuzzleWidget.setObjectName("PuzzleWidget")

        self.StartPuzzleWidget = PuzzleWidget(parent=self.centralwidget, scale=0.4, state=start)
        self.StartPuzzleWidget.setGeometry(QtCore.QRect(20, 45, int(360 * 0.4), int(360 * 0.4)))
        self.StartPuzzleWidget.setObjectName("PuzzleWidget")
        self.DesPuzzleWidget = PuzzleWidget(parent=self.centralwidget, scale=0.4, state=des)
        self.DesPuzzleWidget.setGeometry(QtCore.QRect(20, 235, int(360 * 0.4), int(360 * 0.4)))
        self.DesPuzzleWidget.setObjectName("PuzzleWidget")

        # Tạo nút
        self.btBFS = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btBFS.setGeometry(QtCore.QRect(750, 20, 100, 30))
        self.btBFS.setObjectName("btBFS")
        self.btDFS = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btDFS.setGeometry(QtCore.QRect(870, 20, 100, 30))
        self.btDFS.setObjectName("btDFS")
        self.btUCS = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btUCS.setGeometry(QtCore.QRect(750, 70, 100, 30))
        self.btUCS.setObjectName("btUCS")
        self.btIDS = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btIDS.setGeometry(QtCore.QRect(870, 70, 100, 30))
        self.btIDS.setObjectName("btIDS")
        self.btAStar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btAStar.setGeometry(QtCore.QRect(750, 120, 100, 30))
        self.btAStar.setObjectName("btAStar")
        self.btGreedy = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btGreedy.setGeometry(QtCore.QRect(870, 120, 100, 30))
        self.btGreedy.setObjectName("btGreedy")
        self.btidaStar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btidaStar.setGeometry(QtCore.QRect(750, 170, 100, 30))
        self.btidaStar.setObjectName("btidaStar")
        self.btSimpleHC = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btSimpleHC.setGeometry(QtCore.QRect(870, 170, 100, 30))
        self.btSimpleHC.setObjectName("btSimpleHC")
        self.btSAHC = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btSAHC.setGeometry(QtCore.QRect(750, 220, 100, 30))
        self.btSAHC.setObjectName("btSAHC")
        self.btStochasticHC = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btStochasticHC.setGeometry(QtCore.QRect(870, 220, 100, 30))
        self.btStochasticHC.setObjectName("btStochasticHC")
        self.btSimulatedAnnealing = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btSimulatedAnnealing.setGeometry(QtCore.QRect(750, 270, 100, 30))
        self.btSimulatedAnnealing.setObjectName("btSimulatedAnnealing")
        self.btBeamSearch = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btBeamSearch.setGeometry(QtCore.QRect(870, 270, 100, 30))
        self.btBeamSearch.setObjectName("btBeamSearch")

        self.btStop = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btStop.setGeometry(QtCore.QRect(870, 500, 100, 30))
        self.btStop.setObjectName("btStop")
        self.btPath = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btPath.setGeometry(QtCore.QRect(750, 500, 100, 30))
        self.btPath.setObjectName("btPath")
        
        

        # Chức năng nút
        self.btBFS.clicked.connect(lambda: (self.PuzzleWidget.solve(bfs), self._update()))
        self.btDFS.clicked.connect(lambda: (self.PuzzleWidget.solve(dfs), self._update()))
        self.btUCS.clicked.connect(lambda: (self.PuzzleWidget.solve(ucs), self._update()))
        self.btIDS.clicked.connect(lambda: (self.PuzzleWidget.solve(ids), self._update()))
        self.btAStar.clicked.connect(lambda: (self.PuzzleWidget.solve(aStar), self._update()))
        self.btGreedy.clicked.connect(lambda: (self.PuzzleWidget.solve(greedy), self._update()))
        self.btidaStar.clicked.connect(lambda: (self.PuzzleWidget.solve(idaStar), self._update()))
        self.btSimpleHC.clicked.connect(lambda: (self.PuzzleWidget.solve(SHC), self._update()))
        self.btSAHC.clicked.connect(lambda: (self.PuzzleWidget.solve(SAHC), self._update()))
        self.btStochasticHC.clicked.connect(lambda: (self.PuzzleWidget.solve(StochasticHC), self._update()))
        self.btSimulatedAnnealing.clicked.connect(lambda: (self.PuzzleWidget.solve(SimulatedAnnealing), self._update()))
        self.btBeamSearch.clicked.connect(lambda: (self.PuzzleWidget.solve(BeamSearch), self._update()))
        self.btPath.clicked.connect(lambda: (luuPath(), self._update("Save to path.txt")))
        self.btStop.clicked.connect(self.PuzzleWidget.stop_solution)


        self.PathListView = QtWidgets.QListWidget(parent=self.centralwidget)
        self.PathListView.setGeometry(QtCore.QRect(20, 390, 720, 190))
        self.PathListView.setObjectName("PathListView")
        self.PathListView.setViewMode(QtWidgets.QListView.ViewMode.ListMode)  
        self.PathListView.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)  # Tắt cuộn ngang
        self.PathListView.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded) # Bật cuộn dọc nếu cần


        self.labelStart = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelStart.setGeometry(QtCore.QRect(26, 15, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelStart.setFont(font)
        self.labelStart.setObjectName("labelStart")
        self.labelDes = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelDes.setGeometry(QtCore.QRect(26, 205, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelDes.setFont(font)
        self.labelDes.setObjectName("labelDes")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Thiết lập màu cho các nút bấm
        button_style = "background-color: #F2E2B1; color: #333333;"

        self.btBFS.setStyleSheet(button_style)
        self.btDFS.setStyleSheet(button_style)
        self.btUCS.setStyleSheet(button_style)
        self.btIDS.setStyleSheet(button_style)
        self.btAStar.setStyleSheet(button_style)
        self.btGreedy.setStyleSheet(button_style)
        self.btidaStar.setStyleSheet(button_style)
        self.btStop.setStyleSheet(button_style)
        self.btPath.setStyleSheet(button_style)
        self.btSimpleHC.setStyleSheet(button_style)
        self.btStochasticHC.setStyleSheet(button_style)
        self.btSimulatedAnnealing.setStyleSheet(button_style)
        self.btBeamSearch.setStyleSheet(button_style)
        self.btSAHC.setStyleSheet(button_style)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tran Trieu Duong - 23110200"))
        self.btBFS.setText(_translate("MainWindow", "BFS"))
        self.btDFS.setText(_translate("MainWindow", "DFS"))
        self.btUCS.setText(_translate("MainWindow", "UCS"))
        self.btIDS.setText(_translate("MainWindow", "IDS"))
        self.btAStar.setText(_translate("MainWindow", "A*"))
        self.btGreedy.setText(_translate("MainWindow", "Greedy"))
        self.btidaStar.setText(_translate("MainWindow", "IDA*"))
        self.btStop.setText(_translate("MainWindow", "Stop"))
        self.btPath.setText(_translate("MainWindow", "Xuất Path"))
        self.btSimpleHC.setText(_translate("MainWindow", "SimpleHC"))
        self.btSAHC.setText(_translate("MainWindow", "SAHC"))
        self.btStochasticHC.setText(_translate("MainWindow", "StochasticHC"))
        self.btSimulatedAnnealing.setText(_translate("MainWindow", "SimAnn"))
        self.btBeamSearch.setText(_translate("MainWindow", "BeamSearch"))
        self.labelStart.setText(_translate("MainWindow", "Start"))
        self.labelDes.setText(_translate("MainWindow", "Des"))
    
    def _update(self, text = ""):
        global data

        if not text == "":
            data = text

        self.PathListView.clear()
        for line in data.split("\n"):
            self.PathListView.addItem(line)


def luuPath():
    global data
    with open("path.txt", 'w', encoding='utf-8') as f:
        f.write(data)


def bfs(start: str = start, des: str = des):
    queue = deque([(start, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()
        if len(path) > limitStep:
            break
        if state == des:
            return path + [state]

        visited.add(state)
        index = state.index('0')
        x, y = divmod(index, 3)

        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_index = new_x * 3 + new_y
                new_state = list(state)
                new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
                new_state_str = ''.join(new_state)

                if new_state_str not in visited:
                    queue.append((new_state_str, path + [state]))

    return []


def dfs(start: str = start, des: str = des):
    stack = [(start, [])]
    visited = set()

    while stack:
        state, path = stack.pop()
        if len(path) > limitStep:
            break
        if state == des:
            return path + [state]

        visited.add(state)
        index = state.index('0')
        x, y = divmod(index, 3)

        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_index = new_x * 3 + new_y
                new_state = list(state)
                new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
                new_state_str = ''.join(new_state)

                if new_state_str not in visited:
                    stack.append((new_state_str, path + [state]))

    return []


def ucs(start=start, des=des):
    visited = set()
    parent = {}
    pq = [(0, start)]
    visited.add(start)
    parent[start] = None

    while pq:
        cost, state = heapq.heappop(pq)
        if state == des:
            solution = []
            while state is not None:
                solution.append(state)
                state = parent[state]
            return solution[::-1]

        index = state.index('0')
        x, y = divmod(index, 3)
        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_index = new_x * 3 + new_y
                new_state = list(state)
                new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
                new_state_str = ''.join(new_state)

                if new_state_str not in visited:
                    visited.add(new_state_str)
                    heapq.heappush(pq, (cost + 1, new_state_str))
                    parent[new_state_str] = state
    
    return []


def dls(state, depth, visited, parent, des):
    if depth == 0:
        return state == des
    if state in visited:
        return False

    visited.add(state)

    index = state.index('0')
    x, y = divmod(index, 3)
    for dx, dy in moves:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_index = new_x * 3 + new_y
            new_state = list(state)
            new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
            new_state_str = ''.join(new_state)

            if new_state_str not in visited:
                parent[new_state_str] = state
                if dls(new_state_str, depth - 1, visited, parent, des):
                    return True

    return False


def ids(start = start, des = start):
    depth = 0
    while True:
        visited = set()
        parent = {start: None}
        if dls(start, depth, visited, parent, des):
            solution = []
            state = des
            while state is not None:
                solution.append(state)
                state = parent.get(state)
            return solution[::-1]
        depth += 1


def mahattan(i: int, start = start, des = des):
    x1, y1 = divmod(start.index(str(i)), 3)
    x2, y2 = divmod(des.index(str(i)), 3)
    return abs(x1 - x2) + abs(y1 - y2)


def heuristic(state):
    return sum(mahattan(int(c), state, des) for c in state if c != '0')


def greedy(start=start, des=des):
    visited = set()
    parent = {}
    pq = [(heuristic(start), start)]
    visited.add(start)
    parent[start] = None

    while pq:
        _, state = heapq.heappop(pq)
        if state == des:
            solution = []
            while state is not None:
                solution.append(state)
                state = parent[state]
            return solution[::-1]

        index = state.index('0')
        x, y = divmod(index, 3)
        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_index = new_x * 3 + new_y
                new_state = list(state)
                new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
                new_state_str = ''.join(new_state)

                if new_state_str not in visited:
                    visited.add(new_state_str)
                    h = heuristic(new_state_str)
                    heapq.heappush(pq, (h, new_state_str))
                    parent[new_state_str] = state
    
    return []


def aStar(start=start, des=des):
    visited = set()
    parent = {}
    g = {start: 0}  # g(n): Chi phí từ start đến state
    pq = [(heuristic(start), start)]
    parent[start] = None

    while pq:
        _, state = heapq.heappop(pq)

        if state == des:
            solution = []
            while state is not None:
                solution.append(state)
                state = parent[state]
            return solution[::-1]

        visited.add(state)
        index = state.index('0')
        x, y = divmod(index, 3)

        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_index = new_x * 3 + new_y
                new_state = list(state)
                new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
                new_state_str = ''.join(new_state)

                new_g = g[state] + 1  # Chi phí từ start đến new_state
                h = heuristic(new_state_str)
                f = new_g + h

                if new_state_str not in visited or new_g < g.get(new_state_str, float('inf')):
                    g[new_state_str] = new_g
                    heapq.heappush(pq, (f, new_state_str))
                    parent[new_state_str] = state
    
    return []


def idaStar(start=start, des=des):
    def search(path, g, bound):
        state = path[-1]
        f = g + heuristic(state)
        if f > bound:
            return f
        if state == des:
            return path
        min_bound = float('inf')
        index = state.index('0')
        x, y = divmod(index, 3)
        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_index = new_x * 3 + new_y
                new_state = list(state)
                new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
                new_state_str = ''.join(new_state)
                if new_state_str not in path:
                    path.append(new_state_str)
                    t = search(path, g + 1, bound)
                    if isinstance(t, list):
                        return t
                    if t < min_bound:
                        min_bound = t
                    path.pop()
        return min_bound

    bound = heuristic(start)
    path = [start]
    while True:
        t = search(path, 0, bound)
        if isinstance(t, list):
            return t
        if t == float('inf'):
            return []
        bound = t


def SHC(start=start, des=des): # Simple Hill Climbing
    path = []
    current = start

    while True:
        path.append(current)

        if current == des:
            return path
        
        if len(path) > limitStep:
            return []
        
        neighbors = []
        index = current.index('0')
        x, y = divmod(index, 3)
        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_index = new_x * 3 + new_y
                new_state = list(current)
                new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
                new_state_str = ''.join(new_state)
                neighbors.append(new_state_str)

        current = random.choice(neighbors)


def SAHC(start=start, des=des): # Steepest Ascent-Hill Climbing
    current = start
    if current == des:
        return [current]
    
    h = heuristic(current)
    neighbors = []
    index = current.index('0')
    x, y = divmod(index, 3)
    for dx, dy in moves:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_index = new_x * 3 + new_y
            new_state = list(current)
            new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
            new_state_str = ''.join(new_state)
            neighbors.append(new_state_str)

    nh = []
    for state in neighbors:
        nh.append(heuristic(state))

    if min(nh) < h:
        next_state = SAHC(neighbors[nh.index(min(nh))], des)
        if next_state:
            return [current] + next_state

    return []


def StochasticHC(start=start, des=des): # Stochastic Hill Climbing
    current = start
    if current == des:
        return [current]
    
    h = heuristic(current)
    neighbors = []
    index = current.index('0')
    x, y = divmod(index, 3)
    for dx, dy in moves:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_index = new_x * 3 + new_y
            new_state = list(current)
            new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
            new_state_str = ''.join(new_state)
            neighbors.append(new_state_str)

    nh = []
    for state in neighbors:
        nh.append(heuristic(state))

    better_neighbors = []
    for i in range(len(neighbors)):
        if nh[i] < h:
            better_neighbors.append(neighbors[i])

    while better_neighbors:
        next_state = random.choice(better_neighbors)
        better_neighbors.remove(next_state)
        result = StochasticHC(next_state, des)
        if result:
            return [current] + result

    return []


def SimulatedAnnealing(start=start, des=des, max_iterations=10000, initial_temp=100.0, cooling_rate=0.995):
    current = start
    current_cost = heuristic(current)
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
        next_cost = heuristic(next_state)
        delta = next_cost - current_cost

        if delta < 0 or random.random() < math.exp(-delta / temperature):
            current = next_state
            current_cost = next_cost
            solution_path.append(current)

        temperature *= cooling_rate

    return []


def BeamSearch(start=start, des=des, beam_width=3):
    from heapq import heappush, heappop

    queue = [(heuristic(start), [start])]
    visited = set()

    while queue:
        new_queue = []
        count = 0

        while queue and count < beam_width:
            _, path = heappop(queue)
            state = path[-1]

            if state == des:
                return path

            visited.add(state)
            index = state.index('0')
            x, y = divmod(index, 3)

            for dx, dy in moves:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < 3 and 0 <= new_y < 3:
                    new_index = new_x * 3 + new_y
                    new_state = list(state)
                    new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
                    new_state_str = ''.join(new_state)

                    if new_state_str not in visited:
                        new_path = path + [new_state_str]
                        heappush(new_queue, (heuristic(new_state_str), new_path))
            count += 1

        queue = sorted(new_queue)[:beam_width]

    return []


def timer(func):
    def wrapper(*args, **kwargs):
        global totalTime
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        elapsed_time = end - start
        totalTime += elapsed_time
        return result
    return wrapper
# Nhóm 1
bfs = timer(bfs)
dfs = timer(dfs)
ucs = timer(ucs)
ids = timer(ids)
# Nhóm 2
aStar = timer(aStar)
greedy = timer(greedy)
idaStar = timer(idaStar)
# Nhóm 3
SHC = timer(SHC)
SAHC = timer(SAHC)
StochasticHC = timer(StochasticHC)
SimulatedAnnealing = timer(SimulatedAnnealing)
BeamSearch = timer(BeamSearch)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
