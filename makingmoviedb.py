import requests
import pandas as pd

API_KEY = "" #Generate your own key from the OMDb website and put it here
API_URL = "https://www.imdb.com/chart/top?ref_=nv_mv_250"+ API_KEY + "&t="
SHEET = './movieDB.xlsx'
movielist = []
movieDicts = []

def getMovieData(name, year = ''):
    name = name.replace(' ', '%20')
    if year != '':
        return (API_URL + name + "&y=" + year)
    return (API_URL + name)

def writeMovieData(data, i):  
    title = (data['Title'])
    year = (data['Year'])
    genre = (data['Genre'])
    runtime = (data['Runtime'].split(' ')[0])
    language = (data['Language'])
    language = language.split(',')[0]

    movieDict = {
        'name': title,
        'year': year,
        'genre': genre,
        'runtime': runtime,
        'language': language,
    }

    movieDicts.append(movieDict)

df = pd.read_excel(SHEET, sheet_name="Sheet1")
movielist = df['name'].tolist()

for movie in movielist:
    movieData = requests.get(getMovieData(movie)).json()
    if 'Title' in movieData:
        writeMovieData(movieData)

df = pd.DataFrame.from_dict(movieDicts)
df.to_excel(SHEET, sheet_name="movies")
