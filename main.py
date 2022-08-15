import json
from collections import defaultdict

json_file_path = "data2.json"

with open(json_file_path, 'r') as j:
     contents = json.loads(j.read())
     data = contents["data"]

def retweeted():

    ordered_data = sorted(data, key=lambda x: x["retweetCount"], reverse=True)

    for i in range(10):
        print("")
        print(ordered_data[i]["content"])
        print(f"Retweet count: {ordered_data[i]['retweetCount']}")
    
    

def users():
    user_tweets = defaultdict(lambda : 0)

    for i in range(len(data)):
        user_tweets[data[i]["user"]["username"]] += 1

    lista_user_tweets = []
    for key, value in user_tweets.items():
        lista_user_tweets.append((key, value))

    ordered_data = sorted(lista_user_tweets, key=lambda x: x[1], reverse=True)
    print(ordered_data[:10])

def days():
    pass

def hashtags():
    pass

def main():
    
    users()

main()