import pandas
import json
import random

SOURCE_STRING = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

df = pandas.read_excel("./movieDB.xlsx", sheet_name="Sheet1")

names = df["name"].tolist()
years = df["year"].tolist()
genres = df["genre"].tolist()
runtimes = df["runtime"].tolist()
languages = df["language"].tolist()
imgs = df["img"].tolist()
watcheds = df["watched"].tolist()
tag_lengths = df["tag-length"].tolist()
tag_langs = df["tag-lang"].tolist()
tag_moods = df["tag-mood"].tolist()


count = len(names)
movies = []

for i in range(count):
    movie = {
        "id": ''.join((random.choice(SOURCE_STRING)) for x in range(16)),
        "name": names[i],
        "year": years[i],
        "runtime": runtimes[i],
        "genre": genres[i],
        "language": languages[i],
        "img": imgs[i],
        "watched": bool(watcheds[i]),
        "tags": {
            "len": tag_lengths[i],
            "lang": tag_langs[i],
            "mood": tag_moods[i],
        },
    }

    movies.append(movie)


json_object = json.dumps({
    "movies" : movies,
 }, indent = 4) 

with open("movieDB.json", "w") as outfile:
    outfile.write(json_object)