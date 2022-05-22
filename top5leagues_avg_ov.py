import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('players_22.csv')
top5_laliga = df[df['league_name'].isin(['Spain Primera Division'])]
top5_serieA = df[df['league_name'].isin(['Italian Serie A'])]
top5_pl = df[df['league_name'].isin(['English Premier League'])]
top5_bundes = df[df['league_name'].isin(['German 1. Bundesliga'])]
top5_ligue = df[df['league_name'].isin(['French Ligue 1'])]

countLigue = len(top5_ligue)
countPl = len(top5_pl)
countBundes = len(top5_bundes)
countSerieA = len(top5_serieA)
countLaLiga = len(top5_laliga)

avg_ov_ligue = top5_ligue['overall'].mean()
avg_ov_laliga = top5_laliga['overall'].mean()
avg_ov_bundes = top5_bundes['overall'].mean()
avg_ov_pl = top5_pl['overall'].mean()
avg_ov_serieA = top5_serieA['overall'].mean()

print('Średni overall serie A: ',avg_ov_serieA,"Liczba kart: ",countSerieA)
print('Średni overall bundes: ',avg_ov_bundes,"Liczba kart: ",countBundes)
print('Średni overall pl: ',avg_ov_pl,"Liczba kart: ",countPl)
print('Średni overall laliga: ',avg_ov_laliga,"Liczba kart: ",countLaLiga)
print('Średni overall ligue: ',avg_ov_ligue,"Liczba kart: ",countLigue)
fig = plt.figure(figsize=(12, 5))

list1=[avg_ov_ligue,avg_ov_laliga,avg_ov_bundes,avg_ov_pl,avg_ov_serieA]
list2=[countLigue,countLaLiga,countBundes,countPl,countSerieA]
names=['Ligue','La liga','Bundesliga','Premier League','Serie A']
x=[0,1,2,3,4]
X_axis = np.arange(len(names))
print(X_axis)
plt.bar(X_axis - 0.2, list1, 0.4, label = 'Average Overall')
plt.bar(X_axis + 0.2, list2, 0.4, label = 'Number of players')
plt.xticks(x,names)
plt.xlabel("Leagues")
plt.ylabel("Average overall of card's & card's amount ")
plt.title("Top 5 league's average overall card's & card's amount")
plt.legend()
plt.show()

