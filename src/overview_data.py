import pandas as pd

# Đọc dữ liệu từ file CSV
data = pd.read_csv('./rawdata/Dataset_14-day_AA_depression_symptoms_mood_and_PHQ-9.csv')
data.info()
print(data.head())
