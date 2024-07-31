import requests
from bs4 import BeautifulSoup
from models.Recipe_Model import Recipe_Schema
from repository import mongo_writer


def main():
  recipes = get_recipes()
  mongo_writer.write_to_mongodb(recipes)


def get_recipes():
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
    try:
      input_data = {}
      input_data['link'] = link
      r = requests.get(link)
      soup = BeautifulSoup(r.content, 'lxml')
      counter = counter + 1
      ingredients = []
      for ingredient in soup.find_all('li', class_='mm-recipes-structured-ingredients__list-item'):
        ingredients.append(ingredient.get_text().strip())
      input_data['ingredients'] = ingredients
      directions = soup.find('div', class_='mm-recipes-steps__content')
      directions.figcaption.extract()
      input_data['instructions'] = directions.get_text().strip()
      input_data['title'] = soup.find('h1', class_='article-heading').get_text()
      recipe_schema = Recipe_Schema()
      recipe = recipe_schema.load(input_data)
      recipeDTO = {
        "title" : recipe.title,
        "link" : recipe.link,
        "ingredients" : recipe.ingredients,
        "instructions" : recipe.instructions
      }
      recipes.append(recipeDTO)
    except Exception as e:
      print('Error inserting item in: ' + link)
      print(e)
  return recipes
