from scrapers import asian_recipes
import time


start = time.time()
recipes = asian_recipes.main()
end = time.time()
length = end - start
print("Code successfully ran in " + str(length) + "seconds.")
