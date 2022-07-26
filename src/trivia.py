import requests
from random import random

class theTriviaApi:
    question = "https://the-trivia-api.com/api/questions?categories={category}&limit={num}&difficulty={difficulty}"
    categories = "https://the-trivia-api.com/api/categories"

class TriviaBoard:
    def __init__(self, categoriesNum, questionsPerCategory):
        self.categoriesNum = categoriesNum
        self.questionsPerCategory = questionsPerCategory
        self.questions = {}
        self.fillCategories()

    def fillCategories(self):
        self.categories = requests.get(theTriviaApi.categories).json()

        availableCategories = len(self.categories)
        if self.categoriesNum > availableCategories:
            self.categoriesNum = availableCategories    # If there are not enough categories, just use all of them
        self.categories = random.sample(self.categories, self.categoriesNum)
