import json


def get_input():
    with open('data.txt') as file:
        data = json.load(file)

    # user input
    for question in data["question"]:
        print(question["'category"])
        choose = input("Please choose your category: ")
        if choose == "True/False":
            print(data["ask_question"])
            insert = input("Insert a true of false question: ")
            if insert == "answers":
                print("answer1")
                print("answer2")
                ans = input("Select your answer: ")
                if ans == "answer1" is True or ans == "answer2" is True:
                    print("Correct! You receive a point.")
                else:
                    print("Sorry, your answer is wrong! You do not receive a point.")
                return get_input()
        if choose == "Multiple Choice":
            print(data["ask_question"])
            insert1 = input("Insert a multiple choice question: ")
            if insert1 == "answers":
                print("answer1")
                print("answer2")
                print("answer3")
                print("answer4")
                ans1 = input("Select your answer: ")
                if ans1 == "answer1" or ans1 == "answer2" or ans1 == "answer3" or ans1 == "answer4" is True:
                    print("Correct! You receive a point.")
                else:
                    print("Sorry, your answer is wrong! You do not receive a point.")
                return get_input()
        if choose == "Matching":
            print(data["ask_question"])
            insert2 = input("Insert a matching question: ")
            if insert2 == "answers":
                print("answer1")
                print("answer2")
                print("answer3")
                print("answer4")
                ans2 = input("Select your answer: ")
                if ans2 == "answer1" or ans2 == "answer2" or ans2 == "answer3" or ans2 == "answer4" is True:
                    print("Correct! You receive a point.")
                else:
                    print("Sorry, your answer is wrong! You do not receive a point.")
                return get_input()


def lets_begin():
    # still working on this part
    name = input("Enter your username: ")
    print("Hello, {0}! Welcome to Quiz Click!".format(name))
    print("Lets begin!\n")
    play = get_input()
    score = 0
    print()
    print()
    for next_question in range(number):
        question = random.choice(play)

    print("Your final score was {0} out of {1}.".format(score, number))

    with open('answers.json', 'w', encoding='utf-8') as new_data:
        json.dump(new_data, indent=3)

    # data = json.loads(open('quiz_click.json').read())
    # '''The .loads() method converts a JSON string to a Python dictionary'''
    #
    # # print(data)
    # '''Output is a Python dictionary'''
    #
    # # print(type(data))
    # '''Confirms that data is a dict object'''
    #
    # # for question in data['questions']:
    # #    print(question['category'])
    # '''Output is all the categories'''
    #
    # new_data = json.dumps(data, indent=3)
    # '''The .dumps() method converts a Python object into a JSON string'''
    #
    # with open('quiz_click.json', 'w', encoding='utf-8') as file:
    #     json.dump(file)
