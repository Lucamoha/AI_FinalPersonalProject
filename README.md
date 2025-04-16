# AI_FinalPersonalProject

## Giới thiệu
Dự án nhằm mục tiêu nghiên cứu, đánh giá hiệu suất và triển khai các thuật toán tìm kiếm để giải bài toán cổ điển **8-puzzle** – một trò chơi logic với mục tiêu sắp xếp lại các ô số từ trạng thái ban đầu về trạng thái đích thông qua các phép di chuyển hợp lệ.
Giao diện đồ họa (GUI) được xây dựng bằng thư viện **PyQt6**.
> Dự án được hoàn thiện bởi [Trần Triều Dương](https://github.com/Lucamoha)

## Hướng dẫn cài đặt và sử dụng

### Yêu cầu hệ thống
- Python 3.8 trở lên
- pip (Python package installer)

### Cài đặt
1. Clone repository về máy:
```bash
git clone https://github.com/Lucamoha/AI_FinalPersonalProject.git
cd AI_FinalPersonalProject
```

2. Cài đặt các thư viện cần thiết:
```bash
pip install -r requirements.txt
```

### Cách sử dụng
1. Chạy chương trình:
```bash
python main.py
```

2. Giao diện chương trình:
- Phía trên bên trái: Hiển thị trạng thái bắt đầu (Start)
- Phía dưới bên trái: Hiển thị trạng thái đích (Des)
- Ở giữa: Hiển thị quá trình giải
- Bên phải: Các nút bấm cho từng thuật toán
- Phía dưới: Hiển thị kết quả (thời gian, số bước, đường đi)

3. Các chức năng:
- Chọn một trong các thuật toán bằng cách nhấn vào nút tương ứng
- Nút "Stop": Dừng quá trình giải và đưa puzzle về trạng thái ban đầu
- Nút "Xuất Path": Lưu kết quả vào file path.txt

4. Các thuật toán có sẵn:
- Nhóm 1 - Uninformed Search: BFS, DFS, UCS, IDS
- Nhóm 2 - Informed Search: A*, Greedy, IDA*
- Nhóm 3 - Local Search: SimpleHC, SAHC, StochasticHC, SimAnn, BeamSearch
- Nhóm 4: Genetic, AndOrGS

### Lưu ý
- Một số thuật toán có thể mất nhiều thời gian để tìm ra lời giải hoặc không tìm được lời giải do đặc tính của thuật toán
- Có thể điều chỉnh tốc độ hiển thị bằng cách thay đổi giá trị DELAY trong file main.py


## Trạng thái bắt đầu, trạng thái kết thúc minh họa:
|Trạng thái bắt đầu|Trạng thái kết thúc|
| :--- | :--- |
| ![](https://github.com/user-attachments/assets/fe5efcee-6b20-48c7-9a6f-ba04268521a6) | ![](https://github.com/user-attachments/assets/7d3ef320-6683-4952-aaf0-5a59ef51c545) |

## Mục lục

- [I. Uninformed Search Algorithms](#i-uninformed-search-algorithms)
  - [1. bfs – Breadth-First Search](#1-bfs--breadth-first-search)
  - [2. dfs – Depth-First Search](#2-dfs--depth-first-search)
  - [3. ucs – Uniform Cost Search](#3-ucs--uniform-cost-search)
  - [4. ids – Iterative Deepening Search](#4-ids--iterative-deepening-search)
- [II. Informed Search Algorithms](#ii-informed-search-algorithms)
  - [1. aStar – A* Search](#1-astar--a-search)
  - [2. greedy – Greedy Best-First Search](#2-greedy--greedy-best-first-search)
  - [3. idaStar – Iterative Deepening A*](#3-idastar--iterative-deepening-a)
- [III. Local Search Algorithms](#iii-local-search-algorithms)
  - [1. SHC – Simple Hill Climbing](#1-shc--simple-hill-climbing)
  - [2. SAHC – Steepest Ascent Hill Climbing](#2-sahc--steepest-ascent-hill-climbing)
  - [3. StochasticHC – Stochastic Hill Climbing](#3-stochastichc--stochastic-hill-climbing)
  - [4. SimAnn – SimulatedAnnealing](#4-simann--simulatedannealing)
  - [5. BeamSearch – Beam Search](#5-beamsearch--beam-search)

## I. Uninformed Search Algorithms
### 1. bfs – Breadth-First Search
|Các trạng thái|Hiệu suất thuật toán|
| :--- | :--- |
| ![](https://github.com/user-attachments/assets/2964a580-521b-43d3-b1e6-523e79e6b52d) |<p>Time: 0.5699903999920934s</p><p>Steps: 23</p>|
### 2. dfs – Depth-First Search
**No Solution**
### 3. ucs – Uniform Cost Search
|Các trạng thái|Hiệu suất thuật toán|
| :--- | :--- |
| ![](https://github.com/user-attachments/assets/b7a98cda-93bb-4bfe-a3c0-a370a19e980d) |<p>Time: 0.33811870007775724s</p><p>Steps: 23</p>|
### 4. ids – Iterative Deepening Search
|Các trạng thái|Hiệu suất thuật toán|
| :--- | :--- |
| ![](https://github.com/user-attachments/assets/b788ce8e-82a2-43ce-a537-f029e27a5c95)|<p>Time: 0.24040450004395097s</p><p>Steps: 27</p>|

## II. Informed Search Algorithms
### 1. aStar – A* Search
|Các trạng thái|Hiệu suất thuật toán|
| :--- | :--- |
| ![](https://github.com/user-attachments/assets/03236232-9ebb-49a4-8b00-a4885c027a4a)|<p>Time: 0.010279600042849779s</p><p>Steps: 23</p>|
### 2. greedy – Greedy Best-First Search
|Các trạng thái|Hiệu suất thuật toán|
| :--- | :--- |
| ![](https://github.com/user-attachments/assets/16e8b254-43bf-45d4-972b-c76981cf251b)|<p>Time: 0.005781499901786447s</p><p>Steps: 79</p>|
### 3. idaStar – Iterative Deepening A*
|Các trạng thái|Hiệu suất thuật toán|
| :--- | :--- |
| ![](https://github.com/user-attachments/assets/a2ff7efb-32d7-42f1-add4-a798ecb408d1)|<p>Time: 0.018657599999983177s</p><p>Steps: 23</p>|

## III. Local Search Algorithms
### 1. SHC – Simple Hill Climbing
### 2. SAHC – Steepest Ascent Hill Climbing
### 3. StochasticHC – Stochastic Hill Climbing
### 4. SimAnn – SimulatedAnnealing
### 5. BeamSearch – Beam Search
