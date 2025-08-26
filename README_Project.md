# CET: Counterfactual Explanation Tree

Mã nguồn này được fork từ mã nguồn của bài nghiên cứu *[Counterfactual Explanation Trees: Transparent and Consistent
Actionable Recourse with Decision Trees](https://proceedings.mlr.press/v151/kanamori22a.html)* có sẵn tại [đây](https://github.com/kelicht/cet).

CET là một framework cho bài toán Giải thích phản thực (CE), trong đó tóm tắt các hành động trên toàn bộ không gian đầu vào bằng một cây quyết định.

![demo](https://user-images.githubusercontent.com/52521189/151741986-3244bdb8-e47f-4c84-93d0-dca9b4a756a8.png)

# Các tập dữ liệu được sử dụng

- `adult.csv:` [Adult [Dataset]. UCI Machine Learning Repository](https://doi.org/10.24432/C5XW20)
- `attrition.csv:` [Kaggle - IBM HR Analytics Employee Attrition & Performance](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)
- `bank.csv:` [Bank Marketing [Dataset]. UCI Machine Learning Repository](https://doi.org/10.24432/C5K306)
- `compas.csv:` 
- `diabetes.csv:` [Predict Diabetes From Medical Records]([www.kaggle.com/code/paultimothymooney/predict-diabetes-from-medical-records](https://www.kaggle.com/code/paultimothymooney/predict-diabetes-from-medical-records))
- `german.csv:` Dua, D. and Graff, C. (2017) UCI Machine Learning Repository
- `heloc.csv:`
- `NHANESI.csv:`
- `student.csv:`
- `toy_attrition.csv:`
- `wine.csv:` [Wine Quality [Dataset]. UCI Machine Learning Repository](https://doi.org/10.24432/C56S3T)

| Mã tập dữ liệu | Tên tập dữ liệu | Kích thước | Trường hợp sử dụng |
|--------------|--------------|-------|-------------------|
| 'g' | German | Vừa | Phê duyệt tín dụng |
| 'w' | Wine | Vừa | Dự đoán chất lượng |
| 'h' | HELOC | Lớn | Dự đoán rủi ro tín dụng |
| 'c' | COMPAS | Vừa | Dự đoán tội phạm |
| 'a' | Adult | Lớn | Dự đoán thu nhập |
| 'd' | Diabetes | Vừa | Dự đoán bệnh tiểu đường |
| 'n' | NHANESI | Lớn | Dự đoán sức khỏe |
| 's' | Student | Vừa | Dự đoán thành công học tập |
| 'b' | Bank | Lớn | Dự đoán khách hàng |
| 'i' | Attrition | Vừa | Dự đoán nghỉ việc |
| 't' | Toy Attrition | Nhỏ | Kiểm thử |

| Mã mô hình | Tên mô hình | Phân loại | Tốc độ | Độ chính xác | Khả năng lý giải |
|----------|-----------|----------|--------|--------------|----------------|
| 'L' | Logistic Regression | Tuyến tính | Nhanh | Tương đối | Cao |
| 'F' | Random Forest | Tập hợp cây quyết định | Trung bình | Cao | Trung bình |
| 'M' | Multi-Layer Perceptron | Mạng nơ-ron | Trung bình | Cao | Thấp |
| 'X' | LightGBM | Tăng cường theo gradient | Nhanh | Rất cao | Thấp |
| 'T' | TabNet | Học sâu | Chậm | Rất cao | Trung bình |

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

## Chạy thử

1. Chạy thử CET:
- Để thay đổi mô hình hoặc tập dữ liệu, chỉnh sửa các tham số `dataset` và `model` trong hàm `demo_cet` trong tệp `demo.py`.
```bash
if(__name__ == '__main__'):
    demo_cet(dataset='t', model='X')
```

- Để thay đổi các siêu tham số, chỉnh sửa các tham số trong hàm `demo_cet` trong tệp `demo.py`.
```bash
def demo_cet(dataset='t', model='X'):
    np.random.seed(0)
    LAMBDA = 0.01    # Change regularization parameter
    GAMMA = 1.0      # Change trade-off parameter
```

- Chạy thử mô phỏng đơn giản:
```bash
cd 02_Experiments
python source_code/demo.py
```


# Cấu trúc thư mục

```
📦02_Experiments
 ┣ 📂datasets
 ┃ ┣ 📜adult.csv
 ┃ ┣ 📜attrition.csv
 ┃ ┣ 📜bank.csv
 ┃ ┣ 📜compas.csv
 ┃ ┣ 📜diabetes.csv
 ┃ ┣ 📜german.csv
 ┃ ┣ 📜heloc.csv
 ┃ ┣ 📜NHANESI.csv
 ┃ ┣ 📜student.csv
 ┃ ┣ 📜toy_attrition.csv
 ┃ ┗ 📜wine.csv
 ┣ 📂results
 ┃ ┣ 📂complexity
 ┃ ┃ ┗ 📂L
 ┃ ┃ ┃ ┣ 📜tradeoff.pdf
 ┃ ┃ ┃ ┣ 📜tradeoff.png
 ┃ ┃ ┃ ┣ 📜tradeoff_attrition.pdf
 ┃ ┃ ┃ ┣ 📜tradeoff_attrition.png
 ┃ ┃ ┃ ┣ 📜tradeoff_german.pdf
 ┃ ┃ ┃ ┣ 📜tradeoff_german.png
 ┃ ┃ ┃ ┣ 📜tradeoff_pareto.pdf
 ┃ ┃ ┃ ┗ 📜tradeoff_pareto.png
 ┃ ┣ 📂convergence
 ┃ ┃ ┗ 📂L
 ┃ ┃ ┃ ┣ 📜convergence_attrition.pdf
 ┃ ┃ ┃ ┣ 📜convergence_attrition.png
 ┃ ┃ ┃ ┣ 📜convergence_german.pdf
 ┃ ┃ ┃ ┗ 📜convergence_german.png
 ┃ ┗ 📂gamma
 ┃ ┃ ┗ 📂L
 ┃ ┃ ┃ ┣ 📜sensitivity.pdf
 ┃ ┃ ┃ ┗ 📜sensitivity.png
 ┗ 📂source_code
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
 ┃ ┣ 📜rule_miner.py
 ┃ ┣ 📜userstudy.py
 ┃ ┗ 📜utils.py
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

