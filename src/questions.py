import enum
from math import random

class Difficultly(enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3

class Question:
    def __init__(self, question, answer, difficulty):
        self.question = question
        self.answer = answer
        self.difficulty = difficulty
        self.asked = False

    def ask_and_check(self):
        if self.asked:
            return False

        self.asked = True
        print(self.question)
        return self.answer == input()

    def __str__(self):
        return self.question

class MultipleChoiceQuestion(Question):
    def __init__(self, question, answer, options, difficulty):
        super().__init__(question, answer, difficulty)
        self.choices = []
        self.correct_answer = None

        for i in range(len(options)):
            self.choices.append(options[i])
            if options[i] == answer:
                self.correct_answer = i

    def ask_and_check(self):
        if self.asked:
            return False
        self.asked = True

        print(self.question)
        for i in range(len(self.choices)):
            print(f"{i+1}: {self.choices[i]}")
        answer = int(input())
        return answer == self.correct_answer

    def remove_one_incorrect_option_randomly(self):
        pass

class TrueOrFalseQuestion(Question):
    def __init__(self, question, answer):
        super().__init__(question, answer)

    def ask_and_check(self):
        print(self.question)
        return self.answer == input()