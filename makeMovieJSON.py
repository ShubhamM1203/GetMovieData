import pandas
import json
import random

SOURCE_STRING = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

df = pandas.read_excel("./movieDB.xlsx", sheet_name="Sheet1")

names = df["name"].tolist()
Ratings = df["Rating"].tolist()
release dates = df["release date"].tolist()
durations = df["duration"].tolist()
descriptions = df["description"].tolist()
Dates = df["Date"].tolist()
Times = df["Time"].tolist()

count = len(names)
movies = []

for i in range(count):
    movie = {
        "id": ''.join((random.choice(SOURCE_STRING)) for x in range(16)),
        "name": names[i],
        "Rating": Ratings[i],
        "release date": release dates[i],
        "duration": durations[i],
        "description": descriptions[i],
        "Date": Dates[i],
        "Time": Times[i], 
        "watched": bool(watcheds[i]), 
    }

    movies.append(movie)


json_object = json.dumps({
    "movies" : movies,
 }, indent = 4) 

with open("movieDB.json", "w") as outfile:
    outfile.write(json_object)
