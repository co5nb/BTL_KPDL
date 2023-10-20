import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file CSV
data = pd.read_csv("../output_data.csv")

X = data.values

# Tính WCSS (Within-Cluster Sum of Squares) cho các số lượng cụm từ 1 đến max_clusters
max_clusters = 10
wcss = []
for num_clusters in range(2, max_clusters + 1):
    kmeans = KMeans(n_clusters=num_clusters, n_init=10)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

# Vẽ biểu đồ Elbow Method
plt.figure(figsize=(10, 6))
plt.plot(range(2, max_clusters + 1), wcss, marker='o')
plt.xticks(range(2, max_clusters + 1))
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()