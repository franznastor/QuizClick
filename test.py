import json
import random


def get_questions():
    questions = []
    with open("data.txt", mode="r", encoding="utf-8") as my_file:
        reader = json.reader(my_file)
        for row in reader:
            questions.append(row)
    return questions


def ask_questions(question, score):
    print(question[0])
    for multi in ask_questions[1:-1]:
        print("{0:>5}{1}".format("", multi))
    answer = input("Please select an answer: ")
    print()
    if answer == question[-1]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect! The correct answer was {0}.".format(question[-1]))
    print()
    return score


def main():
    Name = input("Enter your username: ")
    print("Hello", Name + "." + " Welcome to Quiz-Click!")
    questions = get_questions()
    score = 0
    print("Welcome to Quiz-Click!")
    print("==========================")
    print()
    print()
    number = int(input("There are {0} questions - how many would you like in the quiz?"))
    for next_question in range(number):
        question = random.choice(questions)
        score = ask_questions(question, score)
        questions.remove(question)
    print("Your final score was {0} out of {1}.".format(score, number))


if __name__ == "__main__":
    main()
