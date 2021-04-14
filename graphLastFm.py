import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("lastfm-log-2.txt", delimiter="\t", header=None)
numSuggestions = df[0]
data = df[2]

plt.plot(numSuggestions, data)
plt.xlabel('Actions taken by Recommender (Outer limit: 17500000)')
plt.ylabel('Correct Recommendations')
plt.title(r'Successful Recommendations')
plt.gcf().subplots_adjust(left=0.15)
plt.show()

print(df)
print(numSuggestions)
print(data)
