import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl


df = pd.read_csv('players_22.csv')
top5_laliga = df[df['league_name'].isin(['Spain Primera Division'])]
top5_serieA = df[df['league_name'].isin(['Italian Serie A'])]
top5_pl = df[df['league_name'].isin(['English Premier League'])]
top5_bundes = df[df['league_name'].isin(['German 1. Bundesliga'])]
top5_ligue = df[df['league_name'].isin(['French Ligue 1'])]

fig = plt.figure(figsize=(30, 15))
spec = mpl.gridspec.GridSpec(ncols=6, nrows=2) # 6 columns evenly divides both 2 & 3

ax1 = fig.add_subplot(spec[0,0:2]) # row 0 with axes spanning 2 cols on evens
ax2 = fig.add_subplot(spec[0,2:4])
ax3 = fig.add_subplot(spec[0,4:])
ax4 = fig.add_subplot(spec[1,1:3]) # row 0 with axes spanning 2 cols on odds
ax5 = fig.add_subplot(spec[1,3:5])
fig.set_tight_layout(True)

bt_ligue = top5_ligue['body_type'].value_counts().plot(kind="barh",ax=ax1,title='French Ligue 1 body type',x='number of players')
bt_laliga = top5_laliga['body_type'].value_counts().plot(kind="barh",ax=ax2,title='Spain Primera Division body type',x='number of players')
bt_bundes = top5_bundes['body_type'].value_counts().plot(kind="barh",ax=ax3,title='German 1. Bundesliga body type',x='number of players')
bt_pl = top5_pl['body_type'].value_counts().plot(kind="barh",ax=ax4,title='English Premier League body type',x='number of players')
bt_serieA = top5_serieA['body_type'].value_counts().plot(kind="barh",ax=ax5,title='Italian Serie A body type',x='number of players')
plt.show()

