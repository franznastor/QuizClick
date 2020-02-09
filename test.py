

def main():
    qs = {}
    print("*** Quiz ***\n")
    name = input("Please enter your name: ").title()
    print()
    print("\nWell done {0}, you scored {1} out of {2}.".format(name, quiz(qs), len(qs)))


@staticmethod
def run():
    score = 0
    for i in question:
        print()
        print(i)
        checkpoint1 = input("Do you want to skip this question (Y/N): ")
        if checkpoint1 == "Y":
            continue
        ans = input("Enter the answer A, B, C, or D: ")
        if ans == question[i]:
            print("Correct answer, you got 1 point!")
            score = score + 1
            print("Your current score is: ", score)
        else:
            print("Wrong answer, you lost 1 point.")
            score = score - 1
            print("Your current score is: ", score)
        checkpoint2 = input("Do you want to quit (Y/N): ")
        if checkpoint2 == "Y":
            break
    print('Your final score is: ', score)

if __Name__ == "__main__":
    main()