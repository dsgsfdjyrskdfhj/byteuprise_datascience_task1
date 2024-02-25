import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

students = pd.read_csv('STUDENTS.csv')

print("Dataset Information:")
print(students.info())


students['age'].fillna(students['age'].median(), inplace=True)


plt.figure(figsize=(12, 8))
plt.hist(students['age'], bins=20, edgecolor='black', color='skyblue', alpha=0.7)
plt.xlabel('Age', fontsize=14, labelpad=10)
plt.ylabel('Frequency', fontsize=14, labelpad=10)
plt.title('Age Distribution', fontsize=18, pad=15)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.axvline(students['age'].mean(), color='red', linestyle='dashed', linewidth=2, label='Mean Age')
plt.legend(fontsize=12)
plt.show()


plt.figure(figsize=(10, 6))
sns.countplot(x='gender', data=students, palette='pastel')
plt.xlabel('Gender', fontsize=14, labelpad=10)
plt.ylabel('Count', fontsize=14, labelpad=10)
plt.title('Gender Composition', fontsize=18, pad=15)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()


plt.figure(figsize=(14, 10))
sns.pairplot(students[['age', 'score', 'hours_study']], height=2, aspect=1.2, diag_kind='kde')
plt.suptitle('Pairplot of Age, Score, and Hours of Study', fontsize=20, y=1.02)
plt.show()
