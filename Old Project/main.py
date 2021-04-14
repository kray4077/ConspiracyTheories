import requests
import random
from random import randrange
import matplotlib.pyplot as plt
plt.close("all")


# Loop through POST requests
user1 = [0] * 100
user2 = [0] * 100
user3 = [0] * 100
user4 = [0] * 100


def recordChoice(user, choice):
    # Headers will be the same for all of them
    params = {'userid': str(user), 'username': str(user), 'productid': str(choice), 'productname': str(choice)}
    r = requests.post("http://127.0.0.1:5001/purchased", data=params)
    print(r.content)


    # headers = {'Content-Type': 'application/x-www-form-urlencoded', "Accept": "text/plain"};
    # conn.request("POST", "/purchased", payload, headers);
    # res = conn.getresponse();
    # data = res.read();
    # print(data.decode("utf-8"))


# User 1 always picks the same things (videos 1-10)
def user1Picks():
    i = randrange(10)
    recordChoice("user1", i)
    params = {'userid': "user1", 'productid': str(i)}
    try:
        r = requests.get("http://127.0.0.1:5001/recommend", params=params)
        print(r.json()["user-specific"])
    except:
        pass
    user1[i] += 1


# Recommended videos are videos 80-100
# and user 2 picks a recommended video half the time
def user2Picks():
    pickRecommended = randrange(0, 2)  # Will return 0 or 1
    if pickRecommended == 0:  # Pick a recommended video
        user2[randrange(79, 100)] += 1
    else:
        user2[randrange(0, 80)] += 1

    # i = randrange(0, 2)
    # params = {'userid': "user2", 'productid': str(i)}
    # try:
    #     r = requests.get("http://127.0.0.1:5001/recommend", params=params)
    #     recommended = r.json()["user-specific"]
    #     rec = int(random.choice(recommended)[0])
    #     print(rec)
    #     if (random.random()<.5):
    #         i = rec
    # except:
    #     pass
    #
    # recordChoice("user2", i)
    # user2[i] += 1


# Recommend videos are videos 80-100
# and user 3 always picks a recommended video
def user3Picks():
    # user3[randrange(79, 100)] += 1
    i = randrange(79, 100)
    params = {'userid': "user3", 'productid': str(i)}
    try:
        r = requests.get("http://127.0.0.1:5001/recommend", params=params)
        recommended = r.json()["user-specific"]
        rec = int(random.choice(recommended)[0])
        print(rec)
        # 20% chance to change choice i to recommendation. Then records it.
        if(random.random()<.2):
            i = rec
    except:
        pass

    recordChoice("user3", i)
    user3[i] += 1


# User 4 never picks a recommended video
def user4Picks():
    user4[randrange(0, 79)] += 1


for i in range(0, 100):
    user1Picks()
    user2Picks()
    user3Picks()
    user4Picks()
    r = requests.post("http://127.0.0.1:5001/update-model")
    print(r.content)

for i in range(0, 100):
    timesViewed = user1[i] + user2[i] + user3[i] + user4[i]
    print("Video %u was viewed %u times." % (i, timesViewed))




# import http.client
# import mimetypes
# import urllib.parse

# Loop through POST requests

# conn = http.client.HTTPSConnection("127.0.0.1", 5001)

# for info in articles.values:

#   payload = 'articles = [ {'userid': 1, 'username': "Mikka Willis", 'storyid': 1, 'storyname': "Plandemic"}, {'userid': 2, 'username': "News Editors", 'storyid': 2, 'storyname': "Another Gates vaccine bites the dust … Sick monkeys everywhere!"}, {'userid': 2, 'username': "News Editors", 'storyid': 3, 'storyname': "Was the coronavirus created by a Chinese scientist who tried to cover her tracks – and failed?"}]'

# Headers will be the same for all of them

# headers = {'Content-Type': 'application/x-www-form-urlencoded', "Accept": "text/plain"};

# conn.request("POST", "/purchased", payload, headers);

# res = conn.getresponse();

# data = res.read();

# print(data.decode("utf-8"))


# import numpy as np

# Function for the clicks
# def click(n_clicks = 1000):
#    clicks = 0

# np.arrange(0, 1000, 1)


# Loop through clicks
# for i in range(n_clicks):

# Set up rules for clicks
#     user1 =
#     user2 =
#     user3 =

# Add up number of clicks per user

# return #The added up clicks
