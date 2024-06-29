import requests
from bs4 import BeautifulSoup
from classes.recipe_dbo import Recipe_DBO


base_url = 'https://www.allrecipes.com/recipes/227/world-cuisine/asian/'
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}
r = requests.get(base_url)
soup = BeautifulSoup(r.content, 'lxml')
recipe_links = []
recipes = []

for link in soup.find_all('a', class_='mntl-card-list-items'):
  recipe_links.append(link.get('href'))

counter = 0

for link in recipe_links:
  r = requests.get(link)
  soup = BeautifulSoup(r.content, 'lxml')
  counter = counter + 1
  ingredients = []
  for ingredient in soup.find_all('li', class_='mm-recipes-structured-ingredients__list-item'):
    ingredients.append(ingredient.get_text().strip())

  directions = soup.find('div', class_='mm-recipes-steps__content')
  directions.figcaption.extract()
  directions_text = directions.get_text().strip()
  title = soup.find('h1', class_='article-heading').get_text()
  recipe = Recipe_DBO(link, title, ingredients, directions_text)
  recipes.append(recipe)
  if counter > 0:
    break

for recipe in recipes:
  print(recipe)

