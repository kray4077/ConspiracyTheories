import pandas as pd
import re
import matplotlib.pyplot as plt

pattern = "user.*"

# Get columns, drop rows formatted badly (will have an na)
df = pd.read_csv("log_http_api-truncated.txt", sep=" -- ", names=[0, 1, 2, 3, 4, 5], header=None).dropna()

#artist = "darkthrone"
#artist = "skinny puppy"
#artist = "joseph loduca"
#artist = "marduk"
#artist = "nattefrost"
#artist = "rihanna"
#artist = "big bang"
#artist = "mariah carey"
#artist = "nightwish"
artist = "nofx"

numOfArtist = (df[2].values == artist).sum()
print("Number of times recommended: " + str(numOfArtist))

# This will find out what percent of recommendations in each partition feature the artist in question
# Number of partitions is arbitrary, using 100
recommendationPartition = int(df.shape[0] / 100) # Partition size
print("Partition size is: " + str(recommendationPartition))

# Arrays of percent of partition that was the artist, where index is the partition
percentagesRecommended = []
percentagesChosen = []
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

plt.plot([i for i in range(len(percentagesChosen))], percentagesChosen)
plt.plot([i for i in range(len(percentagesChosen))], percentagesRecommended)
plt.show()

