from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QColor, QFont
from PyQt6.QtCore import Qt, QTimer
import time
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


start = '265087431'
des = '123456780'

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
        self.btGenetic = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btGenetic.setGeometry(QtCore.QRect(750, 320, 100, 30))
        self.btGenetic.setObjectName("btGenetic")
        self.btAndOrGS = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btAndOrGS.setGeometry(QtCore.QRect(870, 320, 100, 30))
        self.btAndOrGS.setObjectName("btAndOrGS")

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
        self.btGenetic.clicked.connect(lambda: (self.PuzzleWidget.solve(Genetic), self._update()))
        self.btAndOrGS.clicked.connect(lambda: (self.PuzzleWidget.solve(AndOrGraphSearch), self._update()))
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
        self.btGenetic.setStyleSheet(button_style)
        self.btAndOrGS.setStyleSheet(button_style)

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
# Nhóm 1: Uninformed Search Algorithms
bfs = timer(bfs)
dfs = timer(dfs)
ucs = timer(ucs)
ids = timer(ids)
# Nhóm 2: Informed Search Algorithms
aStar = timer(aStar)
greedy = timer(greedy)
idaStar = timer(idaStar)
# Nhóm 3: Local Search Algorithms
SHC = timer(SHC)
SAHC = timer(SAHC)
StochasticHC = timer(StochasticHC)
SimulatedAnnealing = timer(SimulatedAnnealing)
BeamSearch = timer(BeamSearch)
# Nhóm 4: 
Genetic = timer(Genetic)
AndOrGraphSearch = timer(AndOrGraphSearch)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
