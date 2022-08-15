import json
from collections import defaultdict

json_file_path = "data2.json"

with open(json_file_path, 'r') as j:
     contents = json.loads(j.read())
     data = contents["data"]

def choose_input(opciones):

    #Función que crea Menús aprueba de errores
    #recibe de input una lista de opciones

    while True:
        print('')
        for i in range(len(opciones)):
            print('[' + str(i) + '] ' + opciones[i])
        a = input('Indique su opción:\n')
        if a.isnumeric() == False:
            print('Opción inválida')
        elif int(a) < 0 or int(a) >= len(opciones):
            print('Opción inválida')
        else:
            return a
            break

def retweeted():

    ordered_data = sorted(data, key=lambda x: x["retweetCount"], reverse=True)

    for i in range(10):
        print((ordered_data[i]["content"], ordered_data[i]['retweetCount'] ))
    
    

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
    day_tweets = defaultdict(lambda : 0)

    for i in range(len(data)):
        day = data[i]["date"][:10]
        print(day)
        day_tweets[day] += 1
        print(day_tweets)

    lista_day_tweets = []
    for key, value in day_tweets.items():
        lista_day_tweets.append((key, value))

    ordered_data = sorted(lista_day_tweets, key=lambda x: x[1], reverse=True)
    print(ordered_data[:10])

def hashtags():
    hashtag_tweets = defaultdict(lambda : 0)

    for i in range(len(data)):
        hashtags = []
        words = data[i]["content"].split(" ")
        for element in words:
            if element:
                if element[0] == "#":
                    hashtags.append(element)
        for j in range(len(hashtags)):
            hashtag_tweets[hashtags[j]] += 1
       

    lista_hashtag_tweets = []
    for key, value in hashtag_tweets.items():
        lista_hashtag_tweets.append((key, value))

    ordered_data = sorted(lista_hashtag_tweets, key=lambda x: x[1], reverse=True)
    print(ordered_data[:10])

def main():

    opciones = ["Top 10 tweets con más retweets", "Top 10 usuarios con más tweets", "Top 10 días con más tweets", "Top 10 hashtags con más tweets"]
    opcion = choose_input(opciones)
    if opcion == "0":
        retweeted()
    elif opcion == "1":
        users()
    elif opcion == "2":
        days()
    elif opcion == "3":
        hashtags()

main()