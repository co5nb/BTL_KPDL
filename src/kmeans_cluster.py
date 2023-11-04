import pandas as pd
import numpy as np

# Hàm tính khoảng cách giữa các điểm và trung tâm cụm
def distance(x, centers):
    return np.linalg.norm(x - centers, axis=1)

# Tạo bảng thông tin chi tiết về từng cụm
def info_cluster(number_clusters, data):
    cluster_info = pd.DataFrame()
    cluster_info['Attribute'] = data.columns.drop('cluster')
    cluster_info.set_index('Attribute', inplace=True)

    # Tính giá trị trung bình của các thuộc tính trong từng cụm
    for i in range(number_clusters):
        cluster_data = data[data['cluster'] == i].drop(columns=['cluster'])
        cluster_info[f'Cluster {i}'] = cluster_data.mean()

    # Thêm cột tổng cộng của toàn bộ dữ liệu
    cluster_info['Full Data'] = data.drop(columns=['cluster']).mean()

    # Hiển thị bảng thông tin chi tiết
    print("\nTâm cụm cuối cùng:")
    print(cluster_info)

    # Số lượng bệnh nhân trong mỗi cụm
    cluster_counts = data['cluster'].value_counts()

    print("===========================================================")
    print("\nSố lượng bệnh nhân trong mỗi cụm:")
    for cluster_id, cluster_count in cluster_counts.items():
        print(f"Cụm {cluster_id}: {cluster_count} bệnh nhân ({cluster_count / len(data) * 100:.2f}%)")


def kmeans_algorithm(number_clusters, data):
    # Lấy tên cột và chuyển đổi data từ pandas => numpy
    columns_name = data.columns
    data = data.values
    # Khởi tạo các tâm cụm ban đầu ngẫu nhiên
    np.random.seed(42)
    start_center_index = np.random.choice(data.shape[0], size=number_clusters, replace=False)
    start_centers = data[start_center_index]

    print("===========================================================")
    print(number_clusters , "tâm cụm ban đầu:")
    for i, initial_center in enumerate(start_centers):
        center_str = ', '.join(format(x, '.5f') for x in initial_center)
        print(f"Tâm cụm {i}: {center_str}")

    # Áp dụng thuật toán KMeans để phân cụm dữ liệu
    max_iters = 100
    tolerance = 1e-10
    centers = start_centers
    for iteration in range(max_iters):
        # Gán nhãn tâm cụm cho từng điểm dữ liệu
        distance_matrix = np.apply_along_axis(lambda x: distance(x, centers), axis=1, arr=data)
        labels = np.argmin(distance_matrix, axis=1)
        
        # Lưu trữ trung tâm cũ để so sánh sau
        old_centers = centers.copy()
        
        # Cập nhật trung tâm cụm
        for i in range(number_clusters):
            cluster_points = data[labels == i]
            if len(cluster_points) > 0:
                centers[i] = np.mean(cluster_points, axis=0)
        
        # Kiểm tra điều kiện dừng
        if np.linalg.norm(centers - old_centers) < tolerance:
            break
    
    print("\nSố lần lặp:", iteration + 1)

    data = pd.DataFrame(data, columns=columns_name)
    data['cluster'] = labels
    data.to_csv('completed_data.csv', index=False)
    # Hiển thị thông tin các cụm sau khi hoàn thành
    info_cluster(number_clusters, data)
    return centers

# Hàm fit_predict cho thuật toán K-Means tự tạo
# def fit_predict_custom_kmeans(number_clusters, data):
#     # Lấy tên cột và chuyển đổi data từ pandas => numpy
#     columns_name = data.columns
#     data = data.values

#     # Khởi tạo các tâm cụm ban đầu ngẫu nhiên
#     np.random.seed(42)
#     start_center_index = np.random.choice(data.shape[0], size=number_clusters, replace=False)
#     start_centers = data[start_center_index]

#     # Áp dụng thuật toán KMeans để phân cụm dữ liệu
#     max_iters = 100
#     tolerance = 1e-10
#     centers = start_centers
#     for iteration in range(max_iters):
#         # Gán nhãn tâm cụm cho từng điểm dữ liệu
#         distance_matrix = np.apply_along_axis(lambda x: distance(x, centers), axis=1, arr=data)
#         labels = np.argmin(distance_matrix, axis=1)
        
#         # Lưu trữ trung tâm cũ để so sánh sau
#         old_centers = centers.copy()
        
#         # Cập nhật trung tâm cụm
#         for i in range(number_clusters):
#             cluster_points = data[labels == i]
#             if len(cluster_points) > 0:
#                 centers[i] = np.mean(cluster_points, axis=0)
        
#         # Kiểm tra điều kiện dừng
#         if np.linalg.norm(centers - old_centers) < tolerance:
#             break
    
#     return labels



