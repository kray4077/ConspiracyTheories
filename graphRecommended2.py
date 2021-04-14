import pandas as pd
import re
import matplotlib.pyplot as plt
import math
import numpy as np

pattern = "user.*"

# Get columns, drop rows formatted bad (will have an na)
df = pd.read_csv("log_http_api-truncated.txt", sep=" -- ", names=[0, 1, 2, 3, 4, 5], header=None).dropna()

# Choose artist
#artist = "marduk"
#artist = "joseph loduca"
#artist = "girls aloud"
#artist = "sugababes"
artist = "mariah carey"
#artist = "nightwish"
#artist = "britney spears"

# Pull instances of artist from data file and get the sum
numOfArtist = (df[2].values == artist).sum()
print("Number of times recommended: " + str(numOfArtist))

# We will find out what percent of recommendations in each partition is the artist in question
# Number of partitions is arbitrary, using 100
# Partition size
recommendationPartition = int(df.shape[0] / 100)

# Use an even step size for x-axis of graph close to size of partition
print("Dataframe shape: " + str(df.shape[0]))

# Use order of magnitude of size of dataset to calculate a reasonable step size
stepSize = math.pow(10, math.floor(math.log10(df.shape[0]))-1)

print("Partition size is: " + str(recommendationPartition))

# Arrays of percent of partition that was the artist, where index is the partition
percentagesRecommended = []
percentagesChosen = []
# One-dimensional nd-array with axis labels (including time series)
# Add instances where recommended to this series
wasRecommended = (df[2].values == artist)
wasRecommended = pd.Series(wasRecommended)
wasRecommended = wasRecommended.astype(int)
print(type(wasRecommended))
# Add instances of chosen to this series
wasChosen = (df[5].values == artist)
wasChosen = pd.Series(wasChosen)
wasChosen = wasChosen.astype(int)
print(wasRecommended)
 
for i in range(100):
    start = i * recommendationPartition

    # df[2] is recommended artists
    # Range with size of partition based on current partition
    rowsInPartitionRecommended = df[2][start:start + recommendationPartition]
    # df[5] is chosen artists
    rowsInPartitionChosen = df[5][start:start + recommendationPartition]
    # Get number of times artist in question was recommended and selected for this partition
    numTimesRecommendedInPartition = (rowsInPartitionRecommended.values == artist).sum()
    numTimesChosenInPartition = (rowsInPartitionChosen.values == artist).sum()
    percentChosen = (numTimesChosenInPartition / recommendationPartition) * 100
    percentRecommended = (numTimesRecommendedInPartition / recommendationPartition) * 100
    percentagesRecommended.append(percentRecommended)
    percentagesChosen.append(percentChosen)


for i in range(len(percentagesChosen)):
    if i != 0:
        percentagesChosen[i] += percentagesChosen[i-1]

for i in range(len(percentagesRecommended)):
    if i != 0:
        percentagesRecommended[i] += percentagesRecommended[i-1]

for i in range(len(wasRecommended)):
    if i != 0:
        wasRecommended[i] += wasRecommended[i-1]

for i in range(len(wasChosen)):
    if i != 0:
        wasChosen[i] += wasChosen[i-1]


plt.plot([i for i in range(len(wasChosen))], wasChosen)
plt.plot([i for i in range(len(wasRecommended))], wasRecommended)
x1,x2,y1,y2 = plt.axis()
plt.xlabel('Total Recommendations/Choices')
plt.ylabel('Instances of the Artist')
plt.title(r'Mariah Carey: Orange = Recommended, Blue = Chosen')
plt.show()

print(stepSize)

