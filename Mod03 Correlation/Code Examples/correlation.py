import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_csv('./spotify.csv')

print(df.head())

# streams & playlists
r, p = stats.pearsonr(df['streams'], df['in_spotify_playlists'])
print(f'r (Pearson correlation coefficient): {r:.3f}')
print(f'p-value:                             {p:.3f}')

print('')

# bpm & released month
r, p = stats.pearsonr(df.bpm, df.released_month)
print(f'r (Pearson correlation coefficient): {r:.3f}')
print(f'p-value:                             {p:.3f}')