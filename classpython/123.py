import requests
from bs4 import BeautifulSoup
import lxml

url = "https://www.kinopoisk.ru/lists/movies/top250/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
films = soup.find_all("span", class_="styles_mainTitle__IFQyZ styles_activeMovieTittle__kJdJj")
print(films)
for film in films:
    print(film.text)

