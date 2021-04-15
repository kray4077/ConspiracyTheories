import pandas as pd

df = pd.read_csv("lastfm-one-play-per-line-shuffled-truncated.tsv", sep="\t", header=None)

numOfEach = df[3].value_counts()

numOfEach.to_csv('numOfArtists_v2.csv')

print(df)
print(numOfEach)

