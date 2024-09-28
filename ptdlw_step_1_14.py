# -*- coding: utf-8 -*-
"""PTDLW-Step-1-14.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QNR4dIk482wS4iy5LvbF1HoyQ-yqJwEj
"""

#Step 1
import csv
import openpyxl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline

#Step 2
data = pd.read_csv("countries-protecting-core-lgbt-rights.csv")

data.head()

data.tail()

data.info()

data.nunique()

data.isnull().sum()

(data.isnull().sum()/(len(data)))*100

data.dropna(inplace=True)

"""Step 3 mình không cần làm vì không có dữ liệu nào cần giảm

Step4
Kỹ thuật tính năng tạo ra dữ liệu có ý nghĩa từ dữ liệu thô,
Chuyển đổi các biến phù hợp nhất từ dữ liệu thô khi tạo mô hình dự đoán bằng cách sử dụng machine learning hoặc mô hình thống kê

Step 5 mình không cần làm vì mình không cần tách dữ liệu hoặc tạo biến tính năng
"""

#Step 6
print(data.Entity.unique())
print(data.Entity.nunique())

print(data.Code.unique())
print(data.Code.nunique())

"""Step 6 sau khi kiểm tra các cột thì thấy dữ liệu của chúng ta không có các phần tử trùng nhau hay tương tự và các phần tử ghi sai lỗi nên bước này chỉ dừng lại ở bước kiểm tra.

Step7 Phân tích khám phá dữ liệu:
Phân tích khám phá dữ liệu đề cập đến quá trình quan trọng trong việc thực hiện các nghiên cứu ban đầu về dữ liệu nhằm khám phá các mẫu nhằm kiểm tra các giả định với sự trợ giúp của số liệu thống kê tóm tắt và biểu diễn đồ họa.
"""

#step8
#Các thống kê đặc trưng
data.describe().T

data.describe(include='all').T

cat_cols=data.select_dtypes(include=['object']).columns
num_cols = data.select_dtypes(include=np.number).columns.tolist()
print("Categorical Variables:")
print(cat_cols)
print("Numerical Variables:")
print(num_cols)

#Step 9
for col in num_cols:
    print(col)
    print('Skew :', round(data[col].skew(), 2))
    plt.figure(figsize = (15, 4))
    plt.subplot(1, 2, 1)
    data[col].hist(grid=False)
    plt.ylabel('count')
    plt.subplot(1, 2, 2)
    sns.boxplot(x=data[col])
    plt.show()

#Step 10
def log_transform(data,col):
    for colname in col:
        if (data[colname] == 1.0).all():
            data[colname + '_log'] = np.log(data[colname]+1)
        else:
            data[colname + '_log'] = np.log(data[colname])
    data.info()

log_transform(data,['Same-sex sexual acts legal ("yes", number of countries)','Gender marker change ("yes", number of countries)'])
sns.distplot(data['Same-sex sexual acts legal ("yes", number of countries)_log'], axlabel='Same-sex sexual acts legal ("yes", number of countries)_log')

#Step 12
plt.figure(figsize=(13,17))
sns.pairplot(data=data.drop(['Same-sex sexual acts legal ("yes", number of countries)','Gender marker change ("yes", number of countries)'],axis=1))

plt.show()

data = pd.read_csv('countries-protecting-core-lgbt-rights.csv')
data.head()
fig, axes = plt.subplots(3, 2, figsize = (18, 18))
fig.suptitle('Bar plot for all categorical variables in the dataset')
sns.countplot(ax = axes[0, 0], x = 'Same-sex sexual acts legal ("yes", number of countries)', data = data, color = 'blue',
              order = data['Same-sex sexual acts legal ("yes", number of countries)'].value_counts().index);

sns.countplot(ax = axes[0, 1], x = 'Joint adoptions ("yes", number of countries)', data = data, color = 'blue',
              order = data['Joint adoptions ("yes", number of countries)'].value_counts().index);

sns.countplot(ax = axes[1, 0], x = 'Marriage equality ("yes", number of countries)', data = data, color = 'blue',
              order = data['Marriage equality ("yes", number of countries)'].value_counts().index);

sns.countplot(ax = axes[1, 1], x = 'Gender marker change ("yes", number of countries)', data = data, color = 'blue',
              order = data['Gender marker change ("yes", number of countries)'].value_counts().index);

sns.countplot(ax = axes[2, 0], x = 'Third gender recognition ("yes", number of countries)', data = data, color = 'blue',
              order = data['Third gender recognition ("yes", number of countries)'].head(20).value_counts().index);

axes[1][1].tick_params(labelrotation=45);
axes[2][0].tick_params(labelrotation=90);
axes[2][1].tick_params(labelrotation=90);

#Step 13
plt.figure(figsize=(12, 7))
sns.heatmap(data.drop(['Same-sex sexual acts legal ("yes", number of countries)','Gender marker change ("yes", number of countries)'],axis=1).corr(), annot = True, vmin = -1, vmax = 1)
plt.show()

#Step 14
data.loc[data["Code"]==0.0,'Code']=np.nan
data.Code.isnull().sum()

data['Entity']

s=0
i=0
j
for i in len(data['Entity']):
    for j in data['Entity']:
        while (j != 'World'):
            s = s+i
            i = i+1
            if j == 'World':
                break



