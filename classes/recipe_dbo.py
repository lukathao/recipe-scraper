class Recipe_DBO:
  def __init__(self, link, title, ingredients, instructions):
    self.link = link
    self.title = title
    self.ingredients = ingredients
    self.instructions = instructions

  def __str__(self):
    return f"{self.title}{self.link}\n{self.ingredients}\n{self.instructions}"