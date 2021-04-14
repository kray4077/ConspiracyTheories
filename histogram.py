import pandas as pd
import re
import math
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("log_http_api-truncated.txt", sep=" -- ", names=[0, 1, 2, 3, 4, 5], header=None).dropna()

uniqueArtists = df[5].unique().tolist()

artistRecommendCounts = []

for artist in uniqueArtists:
    wasRecommended = (df[5].values == artist).sum()
    artistRecommendCounts.append(wasRecommended)

bins = 5

plt.hist(artistRecommendCounts, bins, facecolor='blue', alpha=0.5)
plt.xlabel('Chosen Artists')
plt.ylabel('Artists')
plt.title(r'Histogram of Chosen Artists')
plt.show()

print(uniqueArtists)


