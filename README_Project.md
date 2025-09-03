# CET: Counterfactual Explanation Tree

Mã nguồn này được fork từ mã nguồn của bài nghiên cứu *[Counterfactual Explanation Trees: Transparent and Consistent
Actionable Recourse with Decision Trees](https://proceedings.mlr.press/v151/kanamori22a.html)* có sẵn tại [đây](https://github.com/kelicht/cet).

CET là một framework cho bài toán Giải thích phản thực (CE), trong đó tóm tắt các hành động trên toàn bộ không gian đầu vào bằng một cây quyết định.

![demo](https://user-images.githubusercontent.com/52521189/151741986-3244bdb8-e47f-4c84-93d0-dca9b4a756a8.png)

# Các tập dữ liệu được sử dụng

- `attrition.csv:` [Kaggle - IBM HR Analytics Employee Attrition & Performance](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)
- `diabetes.csv:` [Predict Diabetes From Medical Records](https://www.kaggle.com/code/paultimothymooney/predict-diabetes-from-medical-records)
- `german.csv:` Dua, D. and Graff, C. (2017) UCI Machine Learning Repository

| Mã tập dữ liệu | Tên tập dữ liệu | Kích thước | Trường hợp sử dụng |
|--------------|--------------|-------|-------------------|
| 'g' | German | Vừa | Phê duyệt tín dụng |
| 'd' | Diabetes | Vừa | Dự đoán bệnh tiểu đường |
| 'i' | Attrition | Vừa | Dự đoán nghỉ việc |

| Mã mô hình | Tên mô hình | Phân loại | Tốc độ | Độ chính xác | Khả năng lý giải |
|----------|-----------|----------|--------|--------------|----------------|
| 'L' | Logistic Regression | Tuyến tính | Nhanh | Tương đối | Cao |
| 'X' | LightGBM | Tăng cường theo gradient | Nhanh | Rất cao | Thấp |

# Hướng dẫn sử dụng

## Cài đặt
1. Clone repository này về máy:
```bash
git clone https://github.com/HuyTran28/Group07_DecisionTree_Project.git
cd 02_Experiments
```

2. Cài đặt các thư viện cần thiết:   
```bash
pip install -r requirements.txt --extra-index-url https://download.pytorch.org/whl/cu124
```

## Chạy thử các framework

### Chạy thử CET:
- Để thay đổi mô hình hoặc tập dữ liệu, chỉnh sửa các tham số `dataset` và `model` trong hàm `demo_cet` trong tệp `demo.py`.
```python
if(__name__ == '__main__'):
    demo_cet(dataset='t', model='X')
```
- Để thay đổi các siêu tham số, chỉnh sửa các tham số trong hàm `demo_cet` trong tệp `demo.py`.
```python
def demo_cet(dataset='t', model='X'):
    np.random.seed(0)
    LAMBDA = 0.01    # Change regularization parameter
    GAMMA = 1.0      # Change trade-off parameter
```
- Chạy thử mô phỏng đơn giản:
```bash
cd 02_Experiments/source_code
python demo.py
```

### Chạy thử CE:

- Sử dụng các hàm khác nhau để kiểm tra và đánh giá framework CE.
```python
if(__name__ == '__main__'):
    # Basic exact CE testing
    _check_ce(N=5, dataset='t', model='L')

    # Test trade-off sensitivity  
    _check_sens(N=10, dataset='g')

    # Compare exact vs LIME approximation
    _check_lime(N=3, dataset='h', model='M', compare=True)

    # Test LIME with ensemble models
    _check_lime(dataset='i', model='F', compare=False)
```
| Hàm kiểm tra | Mục đích | Mô hình có hỗ trợ |
|--------------|-------|-------------|
| `_check_ce` | Kiểm tra CE chính xác | L, F, M |
| `_check_sens` | Kiểm tra độ nhạy tham số trade-off | L |
| `_check_lime` | So sánh CE chính xác với xấp xỉ LIME | L, F, M |
| `__check_lime` | Kiểm tra xấp xỉ LIME trên các mô hình tập hợp | L, F, M |

- Chạy thử framework CE:
```bash
cd 02_Experiments/source_code
python ce.py
```

### Chạy thử baseline Clustering:
- Chạy thử framework Clustering:
```bash
cd 02_Experiments/source_code
python clustering.py
```
- Để thay đổi tập dữ liệu và số lượng cụm, chỉnh sửa tham số `dataset` và `N` trong hàm `_check` trong tệp `clustering.py`.
```python
if(__name__ == '__main__'):
    _check(dataset='d', N=10) # Clustering baseline with 10 samples
```

### Chạy thử baseline AReS:
- Sử dụng các hàm khác nhau để kiểm tra và đánh giá framework AReS.
```python
if(__name__ == '__main__'):
    # Quick test with default parameters
    _check(dataset='g', model='L')

    # Optimize hyperparameters for best performance
    _check_tuning(dataset='g', model='L', gamma=1.0)
```
- Chạy thử framework AReS:
```bash
cd 02_Experiments/source_code
python ares.py
```

## Chạy các hàm so sánh

### So sánh hiệu suất
So sánh cả 3 framework CE, CET và AReS về độ chính xác, tốc độ và khả năng giải thích bằng phương pháp k-fold cross-validation.

- Để thay đổi tập dữ liệu, mô hình và số lượng phân chia (từ 3 đến 10), chỉnh sửa tham số `dataset`, `model` và `k` trong hàm `compare_cv` trong tệp `exp.py`.
```python
if(__name__ == '__main__'):
    # Basic comparison with 5-fold CV
    compare_cv(dataset='g', model='L', n_splits=5)
```
- Chạy thử hàm so sánh:
```bash
cd 02_Experiments/source_code
python exp.py
```

### So sánh độ phức tạp
Phân tích mức độ thay đổi của độ phức tạp dựa trên số lượng hành động
- Để thay đổi tập dữ liệu, mô hình và số lượng hành động, chỉnh sửa tham số `dataset`, `model`, `n_actions` và `lambdas` trong hàm `compare_comp` trong tệp `exp_complexity.py`.
```python
if(__name__ == '__main__'):
    compare_comp(dataset='g', model='L', n_actions=[4, 8, 12, 16, 20], lambdas=[0.05, 0.04, 0.03, 0.02, 0.01])
    compare_comp(dataset='i', model='L', n_actions=[4, 8, 12, 16, 20], lambdas=[0.05, 0.04, 0.03, 0.02, 0.01])
```
- Chạy thử hàm so sánh:
```bash
cd 02_Experiments/source_code
python exp_complexity.py
```

### So sánh khả năng hội tụ
Phân tích mức độ hội tụ của CET với các siêu tham số khác nhau

- Để thay đổi tập dữ liệu, mô hình và tham số (regularization, trade-off), chỉnh sửa tham số `dataset`, `model`, `params` trong hàm `convergence` trong tệp `exp_convergence.py`.
```python
if(__name__ == '__main__'):
    if(__name__ == '__main__'):
    # Test different lambda values (regularization)
    convergence(dataset='g', model='L', params=(0.01, 0.75))
    convergence(dataset='g', model='L', params=(0.03, 0.75))
    convergence(dataset='g', model='L', params=(0.05, 0.75))
```
- Chạy thử hàm so sánh:
```bash
cd 02_Experiments/source_code
python exp_convergence.py
```

### So sánh độ nhạy tham số trade-off
Phân tích độ nhạy của CET với các giá trị khác nhau của tham số trade-off
- Để thay đổi tập dữ liệu, mô hình, số lượng trường hợp cần kiểm tra trong mỗi vòng lặp, số vòng lặp, danh sách các giá trị gamma cần kiểm tra; chỉnh sửa các tham số `dataset`, `model`, N, M, `gammas` trong hàm `sensitivity` trong tệp `exp_gamma.py`.
```python
if(__name__ == '__main__'):
    # Basic sensitivity analysis
    sensitivity(dataset='g', model='L', N=10, M=100, 
                gammas=[0.25, 0.5, 0.75, 1.0, 1.25, 1.5])
```
- Chạy thử hàm so sánh:
```bash
cd 02_Experiments/source_code
python exp_gamma.py
```

# Cấu trúc thư mục
```
📦02_Experiments
 ┣ 📂datasets
 ┃ ┣ 📜attrition.csv
 ┃ ┣ 📜diabetes.csv
 ┃ ┗ 📜german.csv
 ┣ 📂results
 ┃ ┣ 📂compare
 ┃ ┃ ┗ 📂X
 ┃ ┃ ┃ ┣ 📂convergence
 ┃ ┃ ┃ ┃ ┣ 📜cet_diabetes_objective_0.02_1.0_1.csv
 ┃ ┃ ┃ ┃ ┣ 📜cet_diabetes_objective_0.02_1.0_2.csv
 ┃ ┃ ┃ ┃ ┣ 📜cet_diabetes_objective_0.02_1.0_3.csv
 ┃ ┃ ┃ ┃ ┣ 📜cet_diabetes_objective_0.02_1.0_4.csv
 ┃ ┃ ┃ ┃ ┗ 📜cet_diabetes_objective_0.02_1.0_5.csv
 ┃ ┃ ┃ ┣ 📜ares_diabetes_0.02_1.0.csv
 ┃ ┃ ┃ ┣ 📜cet_diabetes_0.02_1.0.csv
 ┃ ┃ ┃ ┗ 📜clustering_diabetes_0.02_1.0.csv
 ┃ ┣ 📂complexity
 ┃ ┃ ┣ 📂L
 ┃ ┃ ┃ ┣ 📜ares_diabetes_1.0.csv
 ┃ ┃ ┃ ┣ 📜ares_german_1.0.csv
 ┃ ┃ ┃ ┣ 📜cet_diabetes_1.0.csv
 ┃ ┃ ┃ ┣ 📜cet_german_1.0.csv
 ┃ ┃ ┃ ┣ 📜clustering_diabetes_1.0.csv
 ┃ ┃ ┃ ┗ 📜clustering_german_1.0.csv
 ┃ ┃ ┗ 📂X
 ┃ ┃ ┃ ┣ 📜ares_diabetes_1.0.csv
 ┃ ┃ ┃ ┣ 📜ares_german_1.0.csv
 ┃ ┃ ┃ ┣ 📜cet_diabetes_1.0.csv
 ┃ ┃ ┃ ┣ 📜cet_german_1.0.csv
 ┃ ┃ ┃ ┣ 📜clustering_diabetes_1.0.csv
 ┃ ┃ ┃ ┗ 📜clustering_german_1.0.csv
 ┃ ┣ 📂convergence
 ┃ ┃ ┗ 📂L
 ┃ ┃ ┃ ┣ 📜cet_attrition_objective_0.01_0.75.csv
 ┃ ┃ ┃ ┣ 📜cet_attrition_objective_0.03_0.75.csv
 ┃ ┃ ┃ ┣ 📜cet_attrition_objective_0.05_0.75.csv
 ┃ ┃ ┃ ┣ 📜cet_diabetes_objective_0.01_0.75.csv
 ┃ ┃ ┃ ┣ 📜cet_diabetes_objective_0.03_0.75.csv
 ┃ ┃ ┃ ┗ 📜cet_diabetes_objective_0.05_0.75.csv
 ┃ ┣ 📂gamma
 ┃ ┃ ┗ 📂L
 ┃ ┃ ┃ ┣ 📜sensitivity_diabetes.csv
 ┃ ┃ ┃ ┗ 📜sensitivity_german.csv
 ┃ ┗ 📂userstudy
 ┃ ┃ ┣ 📜userstudy_attrition_LogisticRegression.md
 ┃ ┃ ┣ 📜userstudy_diabetes_LogisticRegression.md
 ┃ ┃ ┗ 📜userstudy_german_LogisticRegression.md
 ┣ 📂source_code
 ┃ ┣ 📜ares.py
 ┃ ┣ 📜ce.py
 ┃ ┣ 📜cet.py
 ┃ ┣ 📜clustering.py
 ┃ ┣ 📜demo.py
 ┃ ┣ 📜exp.py
 ┃ ┣ 📜exp_complexity.py
 ┃ ┣ 📜exp_convergence.py
 ┃ ┣ 📜exp_gamma.py
 ┃ ┣ 📜LICENSE
 ┃ ┣ 📜plot.py
 ┃ ┣ 📜prototype_ce.py
 ┃ ┣ 📜random_ce.py
 ┃ ┣ 📜rule_miner.py
 ┃ ┣ 📜userstudy.py
 ┃ ┗ 📜utils.py
 ┗ 📜requirements.txt
 ```

# Mã nguồn framework Cây giải thích phản thực

## ce.py
Triển khai các phương pháp Giải thích phản thực (CE) cho mô hình học máy. Tập trung vào việc sinh hành động hồi đáp khả thi để thay đổi nhãn dự đoán.

1. Lớp `ActionExtractor`:
- Thành phần chính, trích xuất hành động hồi đáp cho từng mẫu dựa trên mô hình đã huấn luyện.
- Hỗ trợ nhiều loại mô hình: Logistic Regression, Random Forest, MLP hoặc xấp xỉ bằng LIME.
- Xây dựng và giải các bài toán tối ưu tuyến tính để tìm hành động tối ưu với chi phí nhỏ nhất.

2. Các hàm kiểm tra (`_check_ce`, `_check_sens`, `_check_lime`, `__check_lime`): 
- Dùng để đánh giá, kiểm thử trên nhiều mô hình & dataset.
- Cho phép phân tích độ nhạy tham số trade-off và trực quan hóa kết quả CE.

## cet.py
Triển khai Cây giải thích phản thực (CET), cung cấp tóm tắt dạng cây quyết định về các hành động hồi đáp khả thi.
1. Cấu trúc cây:
- `Node`, `DummyNode`: Đại diện nút trong cây, lưu trữ thông tin chia nhánh, hành động, chi phí và tập mẫu.
- `CounterfactualExplanationTree`: Lớp cốt lõi để xây dựng, tối ưu hóa và đánh giá CET.
2. Chức năng chính:
- Xây dựng cây: từ tập CE, sinh cây quyết định phân vùng dữ liệu thành các phân lớp hành động.
- Tích hợp module:
    - `ActionExtractor` (sinh hành động CE).
    - `FeatureDiscretizer`, `FrequentRuleMiner` (tiền xử lý & khai phá luật).
    - `Cost` (tính chi phí hành động).
- Tối ưu hóa cấu trúc cây: thông qua các phép thêm, xóa, thay thế, chuyển đổi nút.
- Huấn luyện (fit): sử dụng tìm kiếm cục bộ ngẫu nhiên để cân bằng chi phí - mất mát - độ phức tạp.
- Dự đoán (predict): gán hành động cho mẫu mới dựa trên lá trong CET.
3. Hàm tiện ích
- In/hiển thị cây.
- Đánh giá chi phí/mất mát.
- Kiểm tra tính khả thi.
- `_check`: ví dụ minh họa với nhiều bộ phân loại & dataset khác nhau.

# Mã nguồn framework Giải pháp khắc phục khả thi theo cụm (Clusterwise Actionable Recourse)
Framework sinh hành động hồi đáp khả thi dựa trên clustering để thay đổi nhãn dự đoán. Ý tưởng: nhóm các trường hợp (hoặc hành động) tương đồng lại, rồi tính một hành động “đại diện” tối ưu cho từng cụm.

## Thành phần chính:
1. `ActionExtractor`: Trích xuất hành động tối ưu cho từng instance
2. Clustering module:
- Dùng KMeans để gom cụm.
- Hỗ trợ hai chế độ:
    - Instance clustering: gom cụm trực tiếp trên dữ liệu gốc.
    - Action clustering: tính action vector cho mỗi instance, rồi gom cụm trong action space.
3. Cost calculator
- Tính chi phí thực hiện hành động (theo chuẩn L1, L2, hoặc tùy chỉnh).
- Dùng để chọn ra hành động đại diện tối ưu cho cụm.

## Quy trình huấn luyện và dự đoán
1. Khởi tạo: `ActionExtractor`, `KMeans`, Cost calculator.
2. Clustering
- Instance clustering: chạy `KMeans` trên dữ liệu đầu vào $X$.
- Action clustering: trước tiên sinh action vector $a_x$ cho từng $x$, sau đó gom cụm trên ${a_x}$.
3. Hành động cụm
- Với mỗi cluster $C_k$, chọn hành động tối ưu $a_k^*$ bằng cách:
    - Tính tổng chi phí cho tất cả $x \in C_k$.
    - Chọn hành động $a$ sao cho tổng chi phí tối thiểu.
4. Dự đoán: 
- Xác định cụm của instance mới $x$ (dựa trên input hoặc action space).
- Gán hành động: trả về action vector $a_k^*$ tương ứng với cụm $C_k$.
- Feasibility check: dùng feasify() để đảm bảo action hợp lệ (đặc biệt với đặc trưng nhị phân, phân loại).

# Mã nguồn framework Giải pháp khắc phục khả thi (AReS)
Triển khai framework AReS, cung cấp tóm tắt hành động hồi đáp dưới dạng luật dễ diễn giải cho mô hình học máy.

1. `FeatureDiscretizer`
- Phân đoạn đặc trưng liên tục thành khoảng (bins).
- Hỗ trợ nhiều chiến lược: phân vị, khoảng đều.
- Mã hóa one-hot và phủ định để chuẩn bị cho khai phá luật.
- Bước quan trọng trong việc biến dữ liệu đầu vào thành dạng phù hợp cho FP-Growth.

2. `FrequentRuleMiner`
- Khai phá luật phổ biến bằng thuật toán FP-Growth.
- Hỗ trợ:
    - Ngưỡng hỗ trợ tối thiểu (min_support).
    - Giới hạn độ dài luật tối đa.
    - Đặt tên & chuyển đổi luật.
- Đầu ra: tập hợp luật ứng viên cho hành động.

3. `AReS`
- Điều phối toàn bộ pipeline:
    - Khai phá luật từ dữ liệu phân đoạn.
    - Sinh ứng viên hành động.
    - Chọn lọc bằng heuristic tham lam theo độ bao phủ - độ chính xác - chi phí.
    - Tối ưu hóa cấu trúc luật để cân bằng hiệu quả và diễn giải.
- Hỗ trợ:
    - Huấn luyện & tinh chỉnh siêu tham số.
    - Dự đoán hành động hồi đáp cho mẫu mới.

4. Các hàm tiện ích
- Kiểm tra framework trên nhiều dataset & classifier (Logistic Regression, Random Forest, LightGBM, TabNet...).
- Cho phép phân tích và so sánh hiệu quả luật hồi đáp giữa các mô hình.