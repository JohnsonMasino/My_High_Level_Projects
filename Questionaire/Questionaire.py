#!/usr/bin/python3

"""
This program asks the user some questions on python basics
and performs some calculations including other features
like converting to percentage
"""

class Slide:
    """The class of the program"""

    def Prompt():
        """The slideshow function"""
        print("*" * 50 + "\n" + "Welcome to our Questionaire.\nPlease think and choose your answers wisely..." + "\n" + "*" * 50)
        correct = 0
        total = 5

        q1 = input("\nQ1/5\nWhat is the meaning of STDERR ?\nOPTIONS:\n(A). Standard Input\n(B). String Error\n(C). Standard Error\n(D). None\nChose Option: ")
        if q1 == 'C' or q1 == 'c':
            correct = correct + 1
            print("Correct!")
        elif q1 == 'A' or q1 == 'a' or q1 == 'B' or q1 == 'b' or q1 == 'D' or q1 == 'd':
            print("Incorrect Answer!\nThe correct answer is 'C'")
        else:
            print("Invalid Input !")

        q2 = input("\nQ2/5\nWhat is the meaing of STDIN ?\nOPTIONS:\n(A). Standard Input.\n(B). String Error.\n(C). Standard Error.\n(D). Standard Output.\nChose Option: ")
        if q2 == 'A' or q2 == 'a':
            correct = correct + 1
            print("Correct!")
        elif q2 == 'B' or q2 == 'b' or q2 == 'C' or q2 == 'c' or q2 == 'D' or q2 == 'd':
            print("Incorrect Answer!\nThe correct answer is 'A'")
        else:
            print("Invalid Input !")

        q3 = input("\nQ3/5\nWhat is the meaing of STDOUT ?\nOPTIONS:\n(A). Standard Input.\n(B). String Error.\n(C). Standard Error.\n(D). Standard Output.\nChose Option: ")
        if q3 == 'D' or q3 == 'd':
            correct = correct + 1
            print("Correct!")
        elif q3 == 'B' or q3 == 'b' or q3 == 'C' or q3 == 'c' or q3 == 'A' or q3 == 'a':
            print("Incorrect Answer!\nThe correct answer is 'D'")
        else:
            print("Invalid Input !")

        q4 = input("\nQ4/5\nWhat database represents whole numbers in Python3 ?\nOPTIONS:\n(A). def\n(B). int\n(C). char\n(D). float\nChose Option: ")
        if q4 == 'B' or q4 == 'b':
            correct = correct + 1
            print("Correct!")
        elif q4 == 'D' or q4 == 'd' or q4 == 'C' or q4 == 'c' or q4 == 'A' or q4 == 'a':
            print("Incorrect Answer!\nThe correct answer is 'D'")
        else:
            print("Invalid Input !")

        q5 = input("\nQ5/5\nWhat function takes in input in Python3 ?\nOPTIONS:\n(A). def()\n(B). str()\n(C). scanf()\n(D). input()\nChose Option: ")
        if q5 == 'D' or q5 == 'd':
            correct = correct + 1
            print("Correct!")
        elif q5 == 'B' or q5 == 'b' or q5 == 'C' or q5 == 'c' or q5 == 'A' or q5 == 'a':
            print("Incorrect Answer!\nThe correct answer is 'D'")
        else:
            print("Invalid Input !")
        print(f"\nYou scored {correct} out of 5")
        if correct == 1:
            print(f"Your score in percentage is: 20%\nTry harder next time.")
        elif correct == 2:
            print("Your score in percentage is: 40%\nFair result.")
        elif correct == 3:
            print("Your score in percentage is: 60%\nGood Job.")
        elif correct == 4:
            print("Your score in percentage is: 80%\nYou did great.")
        elif correct == 5:
            print("Your score in percentage is: 100%\nNow this is perfection...\nThank you! :)")
        else:
            print("0% recorded :(")

if __name__ == "__main__":
    Slide.Prompt()
print("\nCode developed by Masino")
