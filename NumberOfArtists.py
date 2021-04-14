import pandas as pd

df = pd.read_csv("log_http_api-truncated.txt", sep=" -- ", names=[0, 1, 2, 3, 4, 5], header=None).dropna()

numOfEach = df[5].value_counts()

numOfEach.to_csv('numOfArtists-chosen.csv')

print(numOfEach)
