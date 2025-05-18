from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QColor, QFont
from PyQt6.QtCore import Qt, QTimer
import time
from algorithm.utils import isSolvable, randomState, randomStateWithFixed
from algorithm.BFS import bfs
from algorithm.DFS import dfs
from algorithm.UCS import ucs
from algorithm.IDS import ids
from algorithm.Greedy import greedy
from algorithm.AStar import aStar
from algorithm.IDAStar import idaStar
from algorithm.SimpleHC import SHC
from algorithm.SteepestAscentHC import SAHC
from algorithm.StochasticHC import StochasticHC
from algorithm.SimulatedAnnealing import SimulatedAnnealing
from algorithm.BeamSearch import BeamSearch
from algorithm.Genetic import Genetic
from algorithm.AndOrGraphSearch import AndOrGraphSearch
from algorithm.NoObservationSearch import NoObservation
from algorithm.PartiallyObservationSearch import PartiallyObservation
# from algorithm.Backtracking import Backtracking
from algorithm.Backtracking_2 import Backtracking
from algorithm.test_search import testSearch
from algorithm.AC_3 import Backtracking_AC3
from algorithm.QLearning import QLearning

start = '265087431'
des = '123456780'

StartStateListRandomSize = 30
DesStateListRandomSize = 10
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

        if algorithm == NoObservation or algorithm == PartiallyObservation:
            StartStateList = randomState(StartStateListRandomSize)
            DesStateList = randomState(DesStateListRandomSize) if algorithm == NoObservation else randomStateWithFixed(0, "123", DesStateListRandomSize)
            self.solution = algorithm(StartStateList, DesStateList)
            data = f"Belief Start State:\n"
            data += ''.join(f"{i}{',\n' if (idx + 1) % 10 == 0 else ', '}" for idx, i in enumerate(StartStateList))
            data = data[:-2]
            data += "\nBelief Des State:\n"
            data += ''.join(f"{i}{',\n' if (idx + 1) % 10 == 0 else ', '}" for idx, i in enumerate(DesStateList))
            data = data[:-2] + "\n\n"
        else:
            if not isSolvable(start, des):
                data = "No solution!"
                return
            self.solution = algorithm(start, des)

        if not self.solution:
            data += "No solution!"
            return
        
        data += f"Time: {totalTime}s\nSteps: {len(self.solution) - 1}\nPath:\n"
        data += ''.join(f"{i}{'\n-> ' if (idx + 1) % 9 == 0 else ' -> '}" for idx, i in enumerate(self.solution))
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
        MainWindow.resize(1100, 700)
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
        self.btBFS.setGeometry(QtCore.QRect(750, 50, 100, 30))
        self.btBFS.setObjectName("btBFS")
        self.btDFS = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btDFS.setGeometry(QtCore.QRect(870, 50, 100, 30))
        self.btDFS.setObjectName("btDFS")
        self.btUCS = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btUCS.setGeometry(QtCore.QRect(990, 50, 100, 30))
        self.btUCS.setObjectName("btUCS")
        self.btIDS = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btIDS.setGeometry(QtCore.QRect(750, 90, 100, 30))
        self.btIDS.setObjectName("btIDS")
        self.btAStar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btAStar.setGeometry(QtCore.QRect(750, 165, 100, 30))
        self.btAStar.setObjectName("btAStar")
        self.btGreedy = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btGreedy.setGeometry(QtCore.QRect(870, 165, 100, 30))
        self.btGreedy.setObjectName("btGreedy")
        self.btidaStar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btidaStar.setGeometry(QtCore.QRect(990, 165, 100, 30))
        self.btidaStar.setObjectName("btidaStar")
        self.btSimpleHC = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btSimpleHC.setGeometry(QtCore.QRect(750, 240, 100, 30))
        self.btSimpleHC.setObjectName("btSimpleHC")
        self.btSAHC = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btSAHC.setGeometry(QtCore.QRect(870, 240, 100, 30))
        self.btSAHC.setObjectName("btSAHC")
        self.btStochasticHC = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btStochasticHC.setGeometry(QtCore.QRect(990, 240, 100, 30))
        self.btStochasticHC.setObjectName("btStochasticHC")
        self.btSimulatedAnnealing = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btSimulatedAnnealing.setGeometry(QtCore.QRect(750, 280, 100, 30))
        self.btSimulatedAnnealing.setObjectName("btSimulatedAnnealing")
        self.btBeamSearch = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btBeamSearch.setGeometry(QtCore.QRect(870, 280, 100, 30))
        self.btBeamSearch.setObjectName("btBeamSearch")
        self.btGenetic = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btGenetic.setGeometry(QtCore.QRect(990, 280, 100, 30))
        self.btGenetic.setObjectName("btGenetic")
        self.btAndOrGS = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btAndOrGS.setGeometry(QtCore.QRect(870, 355, 100, 30))
        self.btAndOrGS.setObjectName("btAndOrGS")
        self.btNoObservation = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btNoObservation.setGeometry(QtCore.QRect(990, 355, 100, 30))
        self.btNoObservation.setObjectName("btNoObservation")
        self.btPartiallyObservation = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btPartiallyObservation.setGeometry(QtCore.QRect(750, 355, 100, 30))
        self.btPartiallyObservation.setObjectName("btPartiallyObservation")
        self.btBacktracking = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btBacktracking.setGeometry(QtCore.QRect(750, 430, 100, 30))
        self.btBacktracking.setObjectName("btBacktracking")
        self.btTestSearch = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btTestSearch.setGeometry(QtCore.QRect(870, 430, 100, 30))
        self.btTestSearch.setObjectName("btTestSearch")
        self.btAC_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btAC_3.setGeometry(QtCore.QRect(990, 430, 100, 30))
        self.btAC_3.setObjectName("btAC_3")
        self.btQLearning = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btQLearning.setGeometry(QtCore.QRect(750, 510, 100, 30))
        self.btQLearning.setObjectName("btQLearning")

        self.btStop = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btStop.setGeometry(QtCore.QRect(950, 650, 100, 30))
        self.btStop.setObjectName("btStop")
        self.btPath = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btPath.setGeometry(QtCore.QRect(790, 650, 100, 30))
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
        self.btGenetic.clicked.connect(lambda: (self.PuzzleWidget.solve(Genetic), self._update()))
        self.btAndOrGS.clicked.connect(lambda: (self.PuzzleWidget.solve(AndOrGraphSearch), self._update()))
        self.btNoObservation.clicked.connect(lambda: (self.PuzzleWidget.solve(NoObservation), self._update(), self._hideObject()))
        self.btPartiallyObservation.clicked.connect(lambda: (self.PuzzleWidget.solve(PartiallyObservation), self._update(), self._hideObject()))
        self.btTestSearch.clicked.connect(lambda: (self.PuzzleWidget.solve(testSearch), self._update(), self._hideObject()))
        self.btBacktracking.clicked.connect(lambda: (self.PuzzleWidget.solve(Backtracking), self._update(), self._hideObject()))
        self.btAC_3.clicked.connect(lambda: (self.PuzzleWidget.solve(Backtracking_AC3), self._update(), self._hideObject()))
        self.btQLearning.clicked.connect(lambda: (self.PuzzleWidget.solve(QLearning), self._update()))
        self.btPath.clicked.connect(lambda: (luuPath(), self._update("Save to path.txt")))
        self.btStop.clicked.connect(self.PuzzleWidget.stop_solution)

        self.PathListView = QtWidgets.QListWidget(parent=self.centralwidget)
        self.PathListView.setGeometry(QtCore.QRect(20, 390, 720, 290))
        self.PathListView.setObjectName("PathListView")
        self.PathListView.setViewMode(QtWidgets.QListView.ViewMode.ListMode)  
        self.PathListView.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded) # Bật cuộn dọc nếu cần

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        self.labelStart = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelStart.setGeometry(QtCore.QRect(26, 15, 61, 31))
        self.labelStart.setFont(font)
        self.labelStart.setObjectName("labelStart")
        self.labelDes = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelDes.setGeometry(QtCore.QRect(26, 205, 61, 31))
        self.labelDes.setFont(font)
        self.labelDes.setObjectName("labelDes")
        self.labelNhom1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelNhom1.setGeometry(QtCore.QRect(750, 15, 350, 31))
        self.labelNhom1.setFont(font)
        self.labelNhom1.setObjectName("labelNhom1")
        self.labelNhom2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelNhom2.setGeometry(QtCore.QRect(750, 130, 350, 31))
        self.labelNhom2.setFont(font)
        self.labelNhom2.setObjectName("labelNhom2")
        self.labelNhom3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelNhom3.setGeometry(QtCore.QRect(750, 205, 350, 31))
        self.labelNhom3.setFont(font)
        self.labelNhom3.setObjectName("labelNhom3")
        self.labelNhom4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelNhom4.setGeometry(QtCore.QRect(750, 320, 350, 31))
        self.labelNhom4.setFont(font)
        self.labelNhom4.setObjectName("labelNhom4")
        self.labelNhom5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelNhom5.setGeometry(QtCore.QRect(750, 395, 370, 31))
        self.labelNhom5.setFont(font)
        self.labelNhom5.setObjectName("labelNhom5")
        self.labelNhom6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelNhom6.setGeometry(QtCore.QRect(750, 470, 350, 31))
        self.labelNhom6.setFont(font)
        self.labelNhom6.setObjectName("labelNhom6")


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 22))
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
        self.btGenetic.setStyleSheet(button_style)
        self.btAndOrGS.setStyleSheet(button_style)
        self.btNoObservation.setStyleSheet(button_style)
        self.btPartiallyObservation.setStyleSheet(button_style)
        self.btBacktracking.setStyleSheet(button_style)
        self.btTestSearch.setStyleSheet(button_style)
        self.btAC_3.setStyleSheet(button_style)
        self.btQLearning.setStyleSheet(button_style)

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
        self.btGenetic.setText(_translate("MainWindow", "Genetic"))
        self.btAndOrGS.setText(_translate("MainWindow", "AndOrGS"))
        self.btNoObservation.setText(_translate("MainWindow", "NOS"))
        self.btPartiallyObservation.setText(_translate("MainWindow", "POS"))
        self.btBacktracking.setText(_translate("MainWindow", "Backtracking"))
        self.btTestSearch.setText(_translate("MainWindow", "Test Search"))
        self.btQLearning.setText(_translate("MainWindow", "Q-Learning"))
        self.btAC_3.setText(_translate("MainWindow", "AC-3"))
        self.labelStart.setText(_translate("MainWindow", "Start"))
        self.labelDes.setText(_translate("MainWindow", "Des"))
        self.labelNhom1.setText(_translate("MainWindow", "Môi trường không có thông tin:"))
        self.labelNhom2.setText(_translate("MainWindow", "Môi trường có thông tin:"))
        self.labelNhom3.setText(_translate("MainWindow", "Cục bộ:"))
        self.labelNhom4.setText(_translate("MainWindow", "Môi trường có hành động bất định:"))
        self.labelNhom5.setText(_translate("MainWindow", "Thỏa mãn ràng buộc:"))
        self.labelNhom6.setText(_translate("MainWindow", "Học tăng cường:"))
    
    def _hideObject(self, hideStart = True, hideDes = True):
        if hideStart:
            self.StartPuzzleWidget.hide()
            self.labelStart.hide()
        if hideDes: 
            self.DesPuzzleWidget.hide()
            self.labelDes.hide()

    def _showObject(self):
        self.StartPuzzleWidget.show()
        self.DesPuzzleWidget.show()
        self.labelStart.show()
        self.labelDes.show()

    def _update(self, text = ""):
        self._showObject()
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
# Nhóm 1: Uninformed Search Algorithms (Tìm kiếm trong môi trường không thông tin)
bfs = timer(bfs)
dfs = timer(dfs)
ucs = timer(ucs)
ids = timer(ids)
# Nhóm 2: Informed Search Algorithms (Tìm kiếm trong môi trường có thông tin)
aStar = timer(aStar)
greedy = timer(greedy)
idaStar = timer(idaStar)
# Nhóm 3: Local Search Algorithms (Tìm kiếm cục bộ)
SHC = timer(SHC)
SAHC = timer(SAHC)
StochasticHC = timer(StochasticHC)
SimulatedAnnealing = timer(SimulatedAnnealing)
BeamSearch = timer(BeamSearch)
Genetic = timer(Genetic)
# Nhóm 4: Searching With Nondeterministic Actions (Tìm kiếm trong môi trường có hành động không xác định)
AndOrGraphSearch = timer(AndOrGraphSearch)
NoObservation = timer(NoObservation)
PartiallyObservation = timer(PartiallyObservation)
# Nhóm 5: Constraint Satisfaction (Thỏa mãn ràng buộc)
Backtracking = timer(Backtracking)
testSearch = timer(testSearch)
Backtracking_AC3 = timer(Backtracking_AC3)

# Nhóm 6: Reinforcement Learning (Học tăng cường)
QLearning = timer(QLearning)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
