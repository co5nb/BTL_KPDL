import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Đọc dữ liệu từ file CSV
data = pd.read_csv('./rawdata/Dataset_14-day_AA_depression_symptoms_mood_and_PHQ-9.csv')
data.info()
print(data.head())

# Biểu đồ cột các giá trị null
null_counts = data.isnull().sum()
null_counts.plot(kind='bar')
plt.title('Số lượng giá trị null trong từng cột')
plt.show()
# ==> các giá trị q1 - q thiếu quá nhiều nên bỏ qua 

# biểu đồ về tần suất phân bố các thuộc tính
sns.set_context(context = 'paper', font_scale= 1.2)
axes = data.hist(bins = 20, figsize = (15,15), color = 'teal', edgecolor = 'white',  
               layout=(7,5))
for ax in axes.flatten():
    plt.setp(ax.get_xticklabels(), rotation=45)
plt.tight_layout()
plt.show()
#

#Mô tả về các thuộc tính

#xem cột sex có những giá trị nào
num_unique_values = data['sex'].unique()
print(num_unique_values)


sex_counts = data['sex'].value_counts()

# Đếm số lần xuất hiện của giá trị 'male' và 'female'
male_count = sex_counts.get('male', 0)
female_count = sex_counts.get('female', 0)
transgender_count = sex_counts.get('transgender', 0)

print("Số lần xuất hiện của 'male':", male_count)
print("Số lần xuất hiện của 'female':", female_count)
print("Số lần xuất hiện của 'transgender':", transgender_count)

# ==>thấy được female nhiều hơn nhiều nên thay thế các giá trị NaN thành female



min_age = data['age'].min()
max_age = data['age'].max()

print(f"Giá trị tối thiểu của cột 'age': {min_age}")
print(f"Giá trị tối đa của cột 'age': {max_age}")

min_happy = data['happiness.score'].min()
max_happy = data['happiness.score'].max()

print(f"Giá trị tối thiểu của cột 'age': {min_happy}")
print(f"Giá trị tối đa của cột 'age': {max_happy}")

# compare time-startTime với phq.day
# Converting the "time" column to a datetime object
data['time'] = pd.to_datetime(data['time'])

# Converting the "start.time" column to a datetime object
data['start.time'] = pd.to_datetime(data['start.time'])

sns.set_context(context = 'paper', font_scale= 1.3)

plt.subplot(2,1,1)
(data['time'] - data['start.time']).dt.days.hist(bins = 20, color = 'teal', 
                                             edgecolor = 'white',
                                            figsize = (14,6))
plt.title('time - start.time')

plt.subplot(2,1,2)
plt.title('Absolute value of phq.day')
data['phq.day'].abs().hist(bins = 20, color = '#3b528b', edgecolor = 'white',
                                            figsize = (14,6))

plt.tight_layout()
plt.show()

# bỏ phq.day vì có 1 số giá trị âm, thời gian thì không thể âm
