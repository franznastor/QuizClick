Name = input("Enter your username: ")
print("Hello", Name + "." + " Welcome to Quiz-Click!")


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
print("Your final score is: ", score)
