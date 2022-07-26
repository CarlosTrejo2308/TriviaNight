import trivia
import random

def main():
    categoriesNum = int(input("How many categories do you want to play? "))
    questionsPerCategory = int(input("How many questions per player do you want to play? "))
    # Negative score?
    # Winning score?

    board = trivia.TriviaBoard(categoriesNum, questionsPerCategory)
    #board.fillCategories()
    #board.fillQuestions()
    #board.askQuestions()
    #board.printResults()

if __name__ == "__main__":
    main()