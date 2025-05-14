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
![](https://github.com/user-attachments/assets/f4ec30b8-5ffa-4807-a823-b2288713da7a)
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
- Nhóm 2 - Informed Search: A*, Greedy, Iterative Deepening A*
- Nhóm 3 - Local Search: Simple Hill Climbing, Steepest Ascent Hill Climbing, Stochastic Hill Climbing, Simulated Annealing, Beam Search, Genetic
- Nhóm 4 - Searching With Nondeterministic Actions: And-Or Graph Search, Searching with No Observation, Searching with Partially Observation
- Nhóm 5 - Constraint Satisfaction: Backtracking, Test Search, AC-3
- Nhóm 6 - Reinforcement Learning: Q-Learning

### Lưu ý
- Một số thuật toán có thể mất nhiều thời gian để tìm ra lời giải hoặc không tìm được lời giải do đặc tính của thuật toán
- Có thể điều chỉnh tốc độ hiển thị bằng cách thay đổi giá trị DELAY trong file main.py

### Tài liệu tham khảo: 
**Russell 2016 Artificial intelligence a modern approach**

## Mục lục
- [A. Mục tiêu](#a-mục-tiêu)
- [B. Nội dung](#b-nội-dung)
  - [I. Uninformed Search Algorithms](#i-uninformed-search-algorithms)
    - [1. bfs – Breadth-First Search](#1-bfs--breadth-first-search)
    - [2. dfs – Depth-First Search](#2-dfs--depth-first-search)
    - [3. ucs – Uniform Cost Search](#3-ucs--uniform-cost-search)
    - [4. ids – Iterative Deepening Search](#4-ids--iterative-deepening-search)
    - [5. Nhận xét](#5-nhận-xét)
  - [II. Informed Search Algorithms](#ii-informed-search-algorithms)
    - [1. aStar – A* Search](#1-astar--a-search)
    - [2. greedy – Greedy Best-First Search](#2-greedy--greedy-best-first-search)
    - [3. idaStar – Iterative Deepening A*](#3-idastar--iterative-deepening-a)
    - [4. Nhận xét](#4-nhận-xét)
  - [III. Local Search Algorithms](#iii-local-search-algorithms)
    - [1. SHC – Simple Hill Climbing](#1-shc--simple-hill-climbing)
    - [2. SAHC – Steepest Ascent Hill Climbing](#2-sahc--steepest-ascent-hill-climbing)
    - [3. StochasticHC – Stochastic Hill Climbing](#3-stochastichc--stochastic-hill-climbing)
    - [4. SimAnn – Simulated Annealing](#4-simann--simulated-annealing)
    - [5. BeamSearch – Beam Search](#5-beamsearch--beam-search)
    - [6. Genetic - Genetic Algorithm](#6-genetic---genetic-algorithm)
    - [7. Nhận xét](#7-nhận-xét)
  - [IV. Searching With Nondeterministic Actions](#iv-searching-with-nondeterministic-actions)
    - [1. AndOrGraphSearch – And-Or Graph Search](#1-andorgraphsearch--and-or-graph-search)
    - [2. NoObservation - Searching with No Observation](#2-noobservation---searching-with-no-observation)
    - [3. PartiallyObservation - Searching with Partially Observation](#3-partiallyobservation---searching-with-partially-observation)
    - [4. Nhận xét](#4-nhận-xét-1)
  - [V. Constraint Satisfaction](#v-constraint-satisfaction)
    - [1. Backtracking](#1-backtracking)
    - [2. Test Search](#2-test-search)
    - [3. AC-3](#3-ac-3)
    - [4. Nhận xét](#4-nhận-xét-2)
  - [VI. Reinforcement Learning](#vi-reinforcement-learning)
    - [1. QLearning - Q-Learning](#1-qlearning---q-learning)
    - [2. Nhận xét](#2-nhận-xét)
- [C. Kết luận](#c-kết-luận)

## A. Mục tiêu
## B. Nội dung
### I. Uninformed Search Algorithms
Trong phạm vi đề tài, các thuật toán tìm kiếm không có thông tin (Uninformed search) được sử dụng khi không có thông tin gì về khoảng cách đến đích (không dùng heuristic).
Các thành phần chính của bài toán tìm kiếm:
- Tập trạng thái: Tất cả các trạng thái hợp lệ của bảng 3x3 (với 8 ô số và 1 ô trống, không có số nào giống nhau)
- Trạng thái bắt đầu
- Tập hành động (Actions): Các thao tác di chuyển ô trống: Lên (Up), Xuống (Down), Trái (Left), Phải (Right)
- Trạng thái đích
- Solution (Lời giải): Lời giải là một dãy hành động dẫn từ trạng thái bắt đầu đến trạng thái đích.
#### 1. bfs – Breadth-First Search
|Các trạng thái|Hiệu suất thuật toán|
| :--- | :--- |
| ![](https://github.com/user-attachments/assets/2964a580-521b-43d3-b1e6-523e79e6b52d) |<p>Time: 0.5699903999920934s</p><p>Steps: 23</p>|
#### 2. dfs – Depth-First Search
**No Solution**
#### 3. ucs – Uniform Cost Search
|Các trạng thái|Hiệu suất thuật toán|
| :--- | :--- |
| ![](https://github.com/user-attachments/assets/b7a98cda-93bb-4bfe-a3c0-a370a19e980d) |<p>Time: 0.33811870007775724s</p><p>Steps: 23</p>|
#### 4. ids – Iterative Deepening Search
|Các trạng thái|Hiệu suất thuật toán|
| :--- | :--- |
| ![](https://github.com/user-attachments/assets/b788ce8e-82a2-43ce-a537-f029e27a5c95)|<p>Time: 0.24040450004395097s</p><p>Steps: 27</p>|
#### 5. Nhận xét
![](https://github.com/user-attachments/assets/66949811-f515-4bf6-a894-5c5411a55aad)
**Trong số các thuật toán trong nhóm: BFS và UCS tìm ra lời giải tốt nhưng tốn thời gian và bộ nhớ. DFS không đáng tin cậy trong các bài toán như 8-puzzle. IDS là một lựa chọn cân bằng, với chi phí thời gian – bộ nhớ hợp lý hơn.**

### II. Informed Search Algorithms
Trong phạm vi đề tài, các thuật toán tìm kiếm có thông tin (Informed Search), ta ước lượng khoảng cách (chi phí) đến mục tiêu để việc tìm kiếm hiệu quả hơn
Các thành phần chính của bài toán tìm kiếm:
- Tập trạng thái: Tất cả các trạng thái hợp lệ của bảng 3x3 (với 8 ô số và 1 ô trống, không có số nào giống nhau)
- Trạng thái bắt đầu
- Tập hành động (Actions): Các thao tác di chuyển ô trống: Lên (Up), Xuống (Down), Trái (Left), Phải (Right)
- Trạng thái đích
- Solution (Lời giải): Lời giải là một dãy hành động dẫn từ trạng thái bắt đầu đến trạng thái đích.
- Hàm heuristic: Ước lượng chi phí từ trạng thái hiện tại đến trạng thái đích
#### 1. aStar – A* Search
|Các trạng thái|Hiệu suất thuật toán|
| :--- | :--- |
| ![](https://github.com/user-attachments/assets/03236232-9ebb-49a4-8b00-a4885c027a4a)|<p>Time: 0.010279600042849779s</p><p>Steps: 23</p>|
#### 2. greedy – Greedy Best-First Search
|Các trạng thái|Hiệu suất thuật toán|
| :--- | :--- |
| ![](https://github.com/user-attachments/assets/16e8b254-43bf-45d4-972b-c76981cf251b)|<p>Time: 0.005781499901786447s</p><p>Steps: 79</p>|
#### 3. idaStar – Iterative Deepening A*
|Các trạng thái|Hiệu suất thuật toán|
| :--- | :--- |
| ![](https://github.com/user-attachments/assets/a2ff7efb-32d7-42f1-add4-a798ecb408d1)|<p>Time: 0.018657599999983177s</p><p>Steps: 23</p>|
#### 4. Nhận xét
![](https://github.com/user-attachments/assets/8725f26e-5430-4131-97f5-0f26a30f2e0f)
**Nhìn chung, việc tối ưu về thời gian của các thuật toán trong nhóm Informed Search tốt hơn nhiều so với các thuật toán trong nhóm Uninformed Search. Greedy dù nhanh nhưng chưa tối ưu về số bước, hiệu quả lời giải thấp. IDA* có số bước thấp nhưng tối ưu thời gian chưa tốt nhất. A* là thuật toán ưu việt nhất trong nhóm này.**

### III. Local Search Algorithms
#### 1. SHC – Simple Hill Climbing
**No Solution**
#### 2. SAHC – Steepest Ascent Hill Climbing
**No Solution**
#### 3. StochasticHC – Stochastic Hill Climbing
**No Solution**
#### 4. SimAnn – Simulated Annealing
**No Solution**
#### 5. BeamSearch – Beam Search
|Các trạng thái|Hiệu suất thuật toán|
| :--- | :--- |
| ![](https://github.com/user-attachments/assets/d8fa8d87-895f-4796-976a-ac72d3520c6d)|<p>Time: 0.0038005000023986213s</p><p>Steps: 77</p>|
#### 6. Genetic - Genetic Algorithm
**No Solution**
#### 7. Nhận xét

### IV. Searching With Nondeterministic Actions
#### 1. AndOrGraphSearch – And-Or Graph Search
|Các trạng thái|Hiệu suất thuật toán|
| :--- | :--- |
| ![](https://github.com/user-attachments/assets/b20a4fdd-c677-4462-9a82-6d05cb2092f6)|<p>Time: 0.653152200000477s</p><p>Steps: 31</p>|
#### 2. NoObservation - Searching with No Observation
#### 3. PartiallyObservation - Searching with Partially Observation
#### 4. Nhận xét

### V. Constraint Satisfaction
#### 1. Backtracking
#### 2. Test Search
#### 3. AC-3
#### 4. Nhận xét

### VI. Reinforcement Learning
#### 1. QLearning - Q-Learning
#### 2. Nhận xét

## C. Kết luận