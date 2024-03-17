from bs4 import BeautifulSoup
import requests
import json


url = 'https://www.imdb.com/chart/top/'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')

movies = soup.find_all('li', class_='ipc-metadata-list-summary-item sc-10233bc-0 iherUv cli-parent')

print(len(movies))

movies_data = []

# Write data for each movie in the list
for movie in movies:
    name = movie.find('div', class_='ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-b0691f29-9 klOwFB cli-title').a.text.split('.')[1]
    rank = movie.find('div', class_='ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-b0691f29-9 klOwFB cli-title').a.text.split('.')[0]
    year = movie.find('div', class_='sc-b0691f29-7 hrgukm cli-title-metadata').span.text
    rating_full = movie.find('div', class_='sc-e2dbc1a3-0 ajrIH sc-b0691f29-2 bhhtyj cli-ratings-container').span.text
    # Only the first two characters of the rating
    rating = rating_full[:2]
    
    # Dictionary for the current movie
    movie_data = {
        'Rank': rank,
        'Name': name,
        'Year': year,
        'Rating': rating
    }

    # Append the movie data dictionary to the list
    movies_data.append(movie_data)

# Define the output JSON file path
json_filename = 'movies.json'

# Write the list of movie data dictionaries to the JSON file
with open(json_filename, 'w') as json_file:
    json.dump(movies_data, json_file, indent=4)
