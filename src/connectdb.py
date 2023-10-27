import mysql.connector
import pandas as pd
from kmeans_cluster import kmeans_algorithm

# Kết nối đến MySQL
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="191816"
)

# Tạo một đối tượng cursor
mycursor = mydb.cursor()

# Truy vấn SQL để kiểm tra xem database "PHQ9-cluster" đã tồn tại chưa
mycursor.execute("SHOW DATABASES")
databases = mycursor.fetchall()

database_exists = False
for db in databases:
    if 'phq9_cluster' in db:
        database_exists = True
        break

if database_exists:
    print("Kết nối thành công!")
else:
    # Truy vấn SQL để tạo database "PHQ9-cluster" nếu nó chưa tồn tại
    mycursor.execute("CREATE DATABASE PHQ9_cluster")
    print("Database 'phq9-cluster' đã được tạo thành công!")

mycursor.execute("USE phq9_cluster")
# Tạo một bảng trong database để lưu trữ các tâm cụm
mycursor.execute("CREATE TABLE IF NOT EXISTS centers (id INT AUTO_INCREMENT PRIMARY KEY, age FLOAT, happiness_score FLOAT, total_period FLOAT, sex_female FLOAT, sex_male FLOAT, depression_severity FLOAT)")

centers = kmeans_algorithm(5, pd.read_csv('./normalized_data.csv'))
print("===========================================================")
print(centers)

for row in centers:
    mycursor.execute("INSERT INTO centers (age, happiness_score, total_period, sex_female, sex_male, depression_severity) VALUES (%s, %s, %s, %s, %s, %s)", tuple(row))

mydb.commit()
# Đóng kết nối
mydb.close()

print("Các tâm cụm đã được lưu vào database 'PHQ9-cluster'!")