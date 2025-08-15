import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = sns.load_dataset('data science workshop')
#df.head(20)
#df.tail(10)
#df.info()
#df['age'].fillna(df['age'].median(), inplace=True)
#df['embarked'].fillna(df['embarked'].mode(), inplace=True)
#df.drop(columns = ['deck'], inplace= True)
#df.isnull().sum()
#df.drop_duplicates
'''print(df[df.duplicated().sum()])
df.duplicated()'''

'''plt.figure(figsize=(6,4))
sns.boxplot(x = df['age'])
plt.show()'''

'''q1 = df['age'].quantile(0.25)
q3 = df['age'].quantile(0.75)
iqr = q3 - q1'''



'''lower_limit = q1 - 1.5 * iqr
upper_limit = q3 - 1.5 * iqr'''

'''df = [(df['age']>= lower_limit) & (df['age'] <= upper_limit)]
df['Family_size'] = df['sibsp'] +'''

'''sns.countplot(x = 'survived', data = df)
plt.title('survival count')
plt.show()'''

#histogram
plt.figure(figsize=(8,5))
sns.histplot(df['age in years'], bins = 6)
b = 6
plt.title('Age Distribution')
plt.show()