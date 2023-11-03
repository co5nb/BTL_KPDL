import pandas as pd
import numpy as np


# Đọc dữ liệu từ file CSV
data = pd.read_csv('./rawdata/Dataset_14-day_AA_depression_symptoms_mood_and_PHQ-9.csv')
data.info()

# Xóa các cột không cần thiết "stt", "user_id", "period.name", "phq.day"
data = data.drop(columns=['stt', 'user_id', 'period.name', 'phq.day'])
# Xóa các cột q1 đến q14, q16, q46, q47 thì null quá nhiều
data = data.drop(columns = ['q1', 'q2', 'q3','q4', 'q5', 'q6','q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q16', 'q46', 'q47'])



# Chuyển "time" và "start.time" thành kiểu dữ liệu "datetime"
data['time'] = pd.to_datetime(data['time'])
data['start.time'] = pd.to_datetime(data['start.time'])
# Tổng hợp kết quả 2 cột "time" và "start.time" thành cột "total.period"
data['total.period'] = (data['time'] - data['start.time']).dt.days
# Xóa 2 cột "time" và "start.time" 
data = data.drop(columns=['time', 'start.time'])


# xử lý phq bị thiếu
#lấy trung bình cộng
# Tính giá trị trung bình của cột 'phq1' (loại bỏ giá trị NaN khi tính toán)
# mean_phq1 = data['phq1'].mean(skipna=True)

# # Thay thế giá trị NaN bằng giá trị trung bình
# data['phq1'].fillna(mean_phq1, inplace=True)
for i in range(1, 10):
    column_name = f'phq{i}'  # Tạo tên cột 'phq{i}'
    
    # Tính giá trị trung bình của cột (loại bỏ giá trị NaN khi tính toán)
    mean_value = data[column_name].mean(skipna=True)
    
    # Thay thế giá trị NaN bằng giá trị trung bình
    data[column_name].fillna(mean_value, inplace=True)



# Điền giá trị "unknown" cho các hàng không có giá trị của cột "sex"
# data['sex'].fillna('unknown', inplace=True)

# ==>thấy được female nhiều hơn nhiều nên thay thế các giá trị NaN thành female
data['sex'].fillna('female', inplace=True)

# loại bỏ các mẫu có giá trị sex = transgender để tránh ảnh hưởng kq
data = data.drop(data[data['sex'] == 'transgender'].index)

# Chuyển các giá trị của cột 'sex' thành các cột mới với các giá trị là 0 và 1 tương ứng
data = pd.get_dummies(data, columns=['sex'], dtype=np.int64)

# Kiểm tra cột "sex_transgender" và "sex_unknow"
# print(data[data['sex_transgender'] == 1]['id'].unique())
# print(data[data['sex_unknown'] == 1]['id'].unique())
# # Xóa cột sex_unknown vì chỉ có một người
# data = data[data['sex_unknown'] == 0]
# data = data.drop('sex_unknown', axis=1)
# # Xóa "sex_transgender" vì chỉ có 1 người
# data = data[data['sex_transgender'] == 0]
# data = data.drop('sex_transgender', axis=1)




# Kiểm tra các cột còn lại có null không
print(data.isnull().sum())
# Cộng tổng các cột phq1 đến phq9 thành cột "depression_severity"
data['depression_severity'] = data[['phq1', 'phq2', 'phq3','phq4', 'phq5', 'phq6','phq7', 'phq8', 'phq9']].sum(axis=1)
# Xóa các cột sau khi đã cộng
data = data.drop(columns = ['phq1', 'phq2', 'phq3','phq4', 'phq5', 'phq6','phq7', 'phq8', 'phq9'])
# Xóa hàng có giá trị null trong cột "age"
# data = data[~data['age'].isnull()]
# # Kiểm tra cột "sex_unknown"
# # print(data[data['sex_unknown'] == 1]['id'].unique())

# # Xóa cột "id"
# data = data.drop('id', axis = 1)

# # Chuẩn hóa Min-Max Scaling cho các thuộc tính
# columns_to_scale = ['age', 'happiness.score', 'total.period', 'sex_female', 'sex_male', 'depression_severity']
# data[columns_to_scale] = ((data[columns_to_scale] - data[columns_to_scale].min()) / 
#                          (data[columns_to_scale].max() - data[columns_to_scale].min()))

# data.info()
# data.to_csv('normalized_data.csv', index=False)
