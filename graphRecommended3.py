import pandas as pd
import re
import math
import numpy as np
import matplotlib.pyplot as plt

artist = "marduk"

df = pd.read_csv("log_http_api-alwaysrec.txt", sep=" -- ", names=[0, 1, 2, 3, 4, 5], header=None)

# Split dataframe into smaller dataframes by using indices of rows containing "Matrix shape..."

indices = df.isnull().any(axis=1)
lis = df[indices].index.tolist()

percentagesChosen = []
percentagesRecommended = []

listOfDfs = []
backoff = 0
restOfDF = None
listOfDfs.append(df.iloc[0])
for i in range(len(lis)):
    # Prevent index out of bounds
    if i == len(lis) - 1:
        break
    start = i
    end = start + 1
    partitionLength = lis[end] - lis[start] - 1
    tempDF = df.iloc[lis[start] + 1:lis[end], :]
    numTimesRecommendedInPartition = (tempDF[2].values == artist).sum()
    numTimesChosenInPartition = (tempDF[5].values == artist).sum()
    percentRecommended = (numTimesRecommendedInPartition / partitionLength) * 100
    percentChosen = (numTimesChosenInPartition / partitionLength) * 100
    percentagesRecommended.append(percentRecommended)
    percentagesChosen.append(percentChosen)
    listOfDfs.append(tempDF)

print(percentagesRecommended)
print(percentagesChosen)

plt.plot([i for i in range(len(percentagesChosen))], percentagesChosen)
plt.plot([i for i in range(len(percentagesRecommended))], percentagesRecommended)
plt.show()
