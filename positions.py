import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('players_22.csv')
df = df[ (df['club_position'] != 'SUB') & (df['club_position'] != 'RES')]
position = df['club_position']
print(len(position))
plt.figure(figsize=(20, 8))
ax = sns.countplot(position)
ax.set_title(label="Player Count Based on club's position", fontsize=22)
ax.set_xlabel(xlabel="Club's position", fontsize=15)
ax.set_ylabel(ylabel="Number of Players", fontsize=15)
plt.show()
