# CET: Counterfactual Explanation Tree

Mã nguồn này được fork từ mã nguồn của bài nghiên cứu *[Counterfactual Explanation Trees: Transparent and Consistent
Actionable Recourse with Decision Trees](https://proceedings.mlr.press/v151/kanamori22a.html)* có sẵn tại [đây](https://github.com/kelicht/cet).

CET là một framework cho bài toán Giải thích phản thực (CE), trong đó tóm tắt các hành động trên toàn bộ không gian đầu vào bằng một cây quyết định.

![demo](https://user-images.githubusercontent.com/52521189/151741986-3244bdb8-e47f-4c84-93d0-dca9b4a756a8.png)

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

 # Các datasets được sử dụng

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

# Các thành phần chính

## ce.py

Tệp này triển khai các phương pháp Giải thích phản thực cho các mô hình học máy, đặc biệt tập trung vào việc sinh ra các hành động hồi đáp có thể thực hiện để thay đổi kết quả dự đoán.

- **Lớp ActionExtractor**: Là thành phần chính, dùng để trích xuất hành động hồi đáp cho từng mẫu dữ liệu dựa trên mô hình đã huấn luyện (Logistic Regression, Random Forest, MLP, hoặc sử dụng LIME approximation). Lớp này xây dựng và giải các bài toán tối ưu hóa tuyến tính để tìm ra hành động tối ưu với chi phí thấp nhất.

- **Các hàm kiểm tra (_check_ce, _check_sens, _check_lime, __check_lime)**: Dùng để kiểm tra, đánh giá và minh họa cách hoạt động của phương pháp trên các bộ dữ liệu và mô hình khác nhau, cũng như phân tích độ nhạy của tham số trade-off.

## ares.py

Tệp này triển khai framework AReS (Actionable Recourse Summary), được thiết kế để tạo ra các hành động hồi đáp có thể giải thích được dưới dạng luật cho các mô hình học máy, đặc biệt là các bộ phân loại. Các thành phần chính gồm:

- **FeatureDiscretizer**: Phân đoạn các đặc trưng liên tục và phân loại thành các khoảng (bins), hỗ trợ nhiều chiến lược (phân vị, đều), mã hóa one-hot và phủ định. Đây là bước quan trọng để khai phá luật.

- **FrequentRuleMiner**: Sử dụng thuật toán khai phá mẫu phổ biến (FP-Growth) để trích xuất các luật phổ biến từ dữ liệu đã được phân đoạn. Hỗ trợ đặt tên luật, chuyển đổi, và khai phá với ngưỡng hỗ trợ tối thiểu và độ dài luật tối đa.

- **AReS**: Lớp cốt lõi điều phối việc khai phá luật, tạo ứng viên, tối ưu hóa (chọn luật theo tham lam dựa trên độ bao phủ, độ chính xác và chi phí), và đánh giá. Cung cấp các phương thức huấn luyện, tinh chỉnh siêu tham số, dự đoán hành động hồi đáp và báo cáo kết quả.

- **Các hàm tiện ích**: Bao gồm các hàm kiểm tra và tinh chỉnh framework trên nhiều bộ dữ liệu và mô hình khác nhau (ví dụ: Logistic Regression, Random Forest, LightGBM, TabNet).

## cet.py

Tệp này triển khai phương pháp Cây giải thích phản thực, xây dựng cây quyết định để tóm tắt các hành động hồi đáp có thể thực hiện cho các mô hình học máy. Các thành phần chính gồm:

- **Lớp Node & DummyNode***: Đại diện cho các nút trong cây, lưu trữ thông tin về các nhánh chia, hành động, chi phí và các mẫu dữ liệu.
- **Lớp CounterfactualExplanationTree**: Lớp cốt lõi xây dựng, tối ưu hóa và đánh giá CET. Hỗ trợ tạo cây, trích xuất hành động, tìm kiếm cục bộ ngẫu nhiên để tối ưu hóa cấu trúc cây và dự đoán hành động hồi đáp.
- **Tích hợp với các module khác**: Sử dụng `ActionExtractor` để sinh hành động hồi đáp, `FeatureDiscretizer` và `FrequentRuleMiner` để tiền xử lý đặc trưng và khai phá luật, cùng với `Cost` để tính toán chi phí.
- **Các hàm chỉnh sửa cây**: Bao gồm các phương thức thêm, xóa, thay thế và chuyển đổi nút để tối ưu hóa cấu trúc cây.
- **Phương thức fit**: Huấn luyện CET bằng cách tìm kiếm cục bộ ngẫu nhiên, cân bằng các mục tiêu như chi phí, mất mát và độ phức tạp của cây.
- **Các hàm tiện ích**: Dùng để in cây, đánh giá chi phí/mất mát và kiểm tra tính khả thi.
- **Hàm _check**: Minh họa cách sử dụng với nhiều bộ phân loại và bộ dữ liệu khác nhau.
