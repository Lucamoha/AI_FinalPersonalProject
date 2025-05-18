# AI_FinalPersonalProject
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
- Phía dưới: Hiển thị chi tiết

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
Dự án nhằm mục tiêu nghiên cứu, đánh giá hiệu suất và triển khai các thuật toán tìm kiếm để giải bài toán cổ điển **8-puzzle**
## B. Nội dung
### I. Uninformed Search Algorithms
Trong phạm vi đề tài, các thuật toán tìm kiếm không có thông tin (Uninformed search) được sử dụng khi không có thông tin gì về khoảng cách đến đích (không dùng heuristic).
Các thành phần chính của bài toán tìm kiếm:
|Trạng thái bắt đầu|Trạng thái kết thúc|
| :--- | :--- |
| ![](https://github.com/user-attachments/assets/fe5efcee-6b20-48c7-9a6f-ba04268521a6) | ![](https://github.com/user-attachments/assets/7d3ef320-6683-4952-aaf0-5a59ef51c545) |
- Tập trạng thái: Tất cả các trạng thái hợp lệ của bảng 3x3 (với 8 ô số và 1 ô trống, không có số nào giống nhau)
- Tập hành động (Actions): Các thao tác di chuyển ô trống: Lên (Up), Xuống (Down), Trái (Left), Phải (Right)
- Solution (Lời giải): Lời giải là một dãy các trạng thái hợp lệ dẫn từ trạng thái bắt đầu đến trạng thái đích.
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
|Trạng thái bắt đầu|Trạng thái kết thúc|
| :--- | :--- |
| ![](https://github.com/user-attachments/assets/fe5efcee-6b20-48c7-9a6f-ba04268521a6) | ![](https://github.com/user-attachments/assets/7d3ef320-6683-4952-aaf0-5a59ef51c545) |
- Tập trạng thái: Tất cả các trạng thái hợp lệ của bảng 3x3 (với 8 ô số và 1 ô trống, không có số nào giống nhau)
- Tập hành động (Actions): Các thao tác di chuyển ô trống: Lên (Up), Xuống (Down), Trái (Left), Phải (Right)
- Solution (Lời giải): Lời giải là một dãy các trạng thái hợp lệ dẫn từ trạng thái bắt đầu đến trạng thái đích.
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

**Nhìn chung, việc tối ưu về thời gian của các thuật toán trong nhóm Informed Search tốt hơn nhiều so với các thuật toán trong nhóm Uninformed Search. Greedy dù nhanh nhưng chưa tối ưu về số bước, hiệu quả lời giải thấp. IDA\* có số bước thấp nhưng tối ưu thời gian chưa tốt nhất. A\* là thuật toán ưu việt nhất trong nhóm này.**

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
**Các thuật toán trong nhóm Local Search không phù hợp để giải bài toán 8-puzzle do không gian tìm kiếm có thể dẫn đến local optima. Chỉ một số thuật toán như Beam Search có thể đưa ra lời giải nhưng vẫn chưa tối ưu.**

### IV. Searching With Nondeterministic Actions
#### 1. AndOrGraphSearch – And-Or Graph Search
|Các trạng thái|Hiệu suất thuật toán|
| :--- | :--- |
| ![](https://github.com/user-attachments/assets/b20a4fdd-c677-4462-9a82-6d05cb2092f6)|<p>Time: 0.653152200000477s</p><p>Steps: 31</p>|
#### 2. NoObservation - Searching with No Observation
Belief Start State:
428013756, 382107564, 067312548, 603745128, 370246851, 683470215, 732854061, 105462873, 164327508, 402763581, 081635427, 043862517, 253076841, 687415320, 635812704, 671085243, 026487153, 625740381, 876521403, 673510842, 543627018, 248610537, 480213675, 162408735, 148237605, 763584021, 236417580, 458120376, 067241853, 841507623

Belief Des State:
835024671, 283405176, 018762345, 406318572, 085763412, 640581273, 023158647, 520638714, 156087423, 370562814

|Các trạng thái|Hiệu suất thuật toán|
| :--- | :--- |
| ![](https://github.com/user-attachments/assets/98e59049-915e-485f-b341-6ae4984cc0cd)|<p>Time: 0.03213900001719594s</p><p>Steps: 9</p>|
#### 3. PartiallyObservation - Searching with Partially Observation
Belief Start State:
321864075, 451280637, 352741860, 120783546, 145327086, 238167540, 541082763, 142670385, 801235746, 081245673, 831472560, 286451730, 765412038, 416372058, 087135624, 751603248, 083514672, 534721086, 210457683, 356148207, 753486102, 370418256, 083251467, 748156023, 128307465, 234807615, 342085176, 632580147, 231607845, 523168470

Belief Des State:
123057684, 123574806, 123086475, 123560487, 123560847, 123460875, 123605748, 123567408, 123574806, 123067584

|Các trạng thái|Hiệu suất thuật toán|
| :--- | :--- |
| ![](https://github.com/user-attachments/assets/f310a1be-85a1-4643-b040-75fbd628dd17)|<p>Time: 0.00037960000918246806s</p><p>Steps: 8</p>|
#### 4. Nhận xét
**Trong môi trường có tính bất định, khả năng quan sát (dù chỉ một phần) đóng vai trò rất lớn trong việc rút ngắn thời gian và nâng cao hiệu quả lời giải. Ngoài ra, chất lượng lời giải còn phụ thuộc vào chất lượng belief state.**

### V. Constraint Satisfaction
Biến: 1 ô là 1 số nguyên
Miền: Tập hợp các giá trị có thể có của 1 biến: 0->8
Ràng buộc: 1 số không thể xuất hiện 2 lần

**Lưu ý:** Có thể điều chỉnh ràng buộc của các biến trong algorithm\\Constraint.json
#### 1. Backtracking
|Các trạng thái|Hiệu suất thuật toán|
| :--- | :--- |
| ![](https://github.com/user-attachments/assets/f7c52042-dee1-4841-9abd-ba62b7dd199e)|<p>Time: 9.129999671131372e-05s</p><p>Steps: 8</p>|
#### 2. Test Search
|Các trạng thái|Hiệu suất thuật toán|
| :--- | :--- |
| ![](https://github.com/user-attachments/assets/a9788fa4-02fa-42de-8f0f-bdab7285acee)|<p>Time: 0.0033423999848309904s</p><p>Steps: 354</p>|

*Do tính chất của thuật toán nên thời gian và số bước có thể khác nhiều*
#### 3. AC-3
|Các trạng thái|Hiệu suất thuật toán|
| :--- | :--- |
| ![](https://github.com/user-attachments/assets/ee0952c7-4be6-48d1-aef1-c39fb21a8c12)|<p>Time: 0.0010409000096842647s</p><p>Steps: 8</p>|
#### 4. Nhận xét
![Image](https://github.com/user-attachments/assets/8a0b2e9e-a49f-497b-9f10-42ee47c9395d)

### VI. Reinforcement Learning
**Reinforcement Learning (RL) – học tăng cường:** một tác nhân (agent) học cách đưa ra quyết định thông qua tương tác với môi trường và nhận được phần thưởng (reward) hoặc hình phạt (penalty) sau mỗi hành động. Khác với các thuật toán tìm kiếm truyền thống vốn dựa vào mô hình rõ ràng về môi trường, RL hướng đến việc học thông qua thử – sai, và dần dần rút ra chính sách tối ưu.
#### 1. QLearning - Q-Learning
|Các trạng thái|Hiệu suất thuật toán|
| :--- | :--- |
| ![](https://github.com/user-attachments/assets/b5458a01-fff2-4ec7-8754-12d44d804c27)|<p>Time: 0.0013556999911088496s</p><p>Steps: 23</p>|
#### 2. Nhận xét
**Trải qua một quá trình huấn luyện đúng cách, Q-Learning đưa ra lời giải với thời gian nhanh (~0.00135s) và số bước tối ưu (23 bước), có thể so sánh được với với các thuật toán heuristic mạnh như A\***

## C. Kết luận
**Qua quá trình triển khai và đánh giá, dự án đã thực hiện thành công việc áp dụng nhiều nhóm thuật toán trí tuệ nhân tạo để giải bài toán cổ điển 8-puzzle, từ đó rút ra nhiều nhận định quan trọng về hiệu suất và đặc điểm của từng nhóm thuật toán.**

**Dự án không chỉ củng cố kiến thức về thuật toán tìm kiếm mà còn mở rộng tầm nhìn về cách thức vận dụng AI trong các bài toán ra quyết định và tối ưu hóa trong thực tế.**