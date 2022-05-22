import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('players_22.csv')
age = df['age']
print(len(age))
plt.figure(figsize=(20, 8))
ax = sns.countplot(age)
ax.set_title(label="Player Count Based on Age", fontsize=22)
ax.set_xlabel(xlabel="Age", fontsize=15)
ax.set_ylabel(ylabel="Number of Players", fontsize=15)
plt.show()
