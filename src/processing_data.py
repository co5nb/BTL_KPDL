import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from kmean_cluster import kmeans_ne
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from yellowbrick.cluster import KElbowVisualizer
from yellowbrick.cluster import SilhouetteVisualizer
# Đọc dữ liệu từ file CSV
data = pd.read_csv('./archive/Dataset_14-day_AA_depression_symptoms_mood_and_PHQ-9.csv')
data.info()


# Converting the "time" column to a datetime object / chuyển dữ liệu time từ string về datetime
data['time'] = pd.to_datetime(data['time'])

# Converting the "start.time" column to a datetime object / chuyển dữ liệu start.time từ string về datetime
data['start.time'] = pd.to_datetime(data['start.time'])
# tong hơp 2 cột / tổng hợp kết quả 2 cột
data['total.period'] = (data['time'] - data['start.time']).dt.days

# Xóa các cột 'time', 'start.time' ,'user_id', 'period.name' , 'php.day'
columns_to_drop = ['stt','time', 'start.time', 'user_id', 'period.name', 'phq.day']
data = data.drop(columns=columns_to_drop)
#điên null thành unknown
data['sex'].fillna('unknown', inplace=True)
#chuyển các giá trị thành true false với mỗi giá trị thành 1 cột
data = pd.get_dummies(data, columns=['sex'], dtype=np.int64)
#
print(data[data['sex_transgender'] == 1]['id'].unique())
data[data['sex_unknown'] == 1]['id'].unique()
# df = df[df['sex_transgender'] == 0]
#xoa transgender vi 1 dua bede
data = data.drop('sex_transgender', axis=1)
#cong tong các côt
data['depression_severity'] = data[['phq1', 'phq2', 'phq3','phq4', 'phq5', 'phq6','phq7', 'phq8', 'phq9']].sum(axis=1)
#xoa cac cot vua cong
data = data.drop(columns = ['phq1', 'phq2', 'phq3','phq4', 'phq5', 'phq6','phq7', 'phq8', 'phq9'])
#xoa cac cot null qua nhieu
data = data.drop(columns = ['q1', 'q2', 'q3','q4', 'q5', 'q6','q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q16', 'q46', 'q47'])
#in ra các gia tri null
print(data.isnull().sum())
#xoa cac cot age null hoặc lấy giá trị mean, du doan
data = data[~data['age'].isnull()]
# mean_age = data['age'].mean().round()
# data['age'].fillna(mean_age, inplace=True)
#kiem tra co bao dua ko ro gt
data[data['sex_unknown'] == 1]['id'].unique()
# có 1 dua nen xoa luon
data = data[data['sex_unknown'] == 0]
data = data.drop('sex_unknown', axis=1)
# data = data.groupby('id').median()
data = data.drop('id', axis = 1)


# # # Chuẩn hóa Min-Max Scaling cho các thuộc tính
columns_to_scale = ['age', 'happiness.score', 'total.period', 'sex_female', 'sex_male', 'depression_severity']
data[columns_to_scale] = ((data[columns_to_scale] - data[columns_to_scale].min()) / 
                         (data[columns_to_scale].max() - data[columns_to_scale].min()))
# print(data)
# print(data)
data.to_csv('output_data.csv', index=False)


print(data.describe())
plt.figure(figsize=(15, 5))

Elbow_M = KElbowVisualizer(KMeans(), k=10)
Elbow_M.fit(data)
Elbow_M.show()

plt.tight_layout()
plt.show()

kmeans = KMeans(n_clusters = 5)

kmeans.fit_predict(data)

score = silhouette_score(data, kmeans.labels_, metric='euclidean')
print('Silhouetter Average Score: %.3f' % score)


num_clusters = 5
centers = kmeans_ne(num_clusters, data)
print(centers)
