import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from yellowbrick.cluster import KElbowVisualizer

data = pd.read_csv("./normalized_data.csv")

Elbow_M = KElbowVisualizer(KMeans(), k=10)
Elbow_M.fit(data)
Elbow_M.show()

plt.tight_layout()
plt.show()

kmeans = KMeans(n_clusters = 5)

kmeans.fit_predict(data)

data.to_csv('completed_data.csv', index=False)
# score = silhouette_score(data, kmeans.labels_, metric='euclidean')
# print('Silhouetter Average Score: %.3f' % score)