#!/usr/bin/python3

#This is the main file for the numi-calculator_clone project

class NumiCalculator():
    from first_fxn import adding0 as a0
    from first_fxn import subtracting0 as s0
    from second_fxn import adding1 as a1
    from second_fxn import subtracting1 as s1
    
    def main_adding_fxn():
        expression = input("Please enter your mathematical expression here: ")
        done = expression.split(" ")
        if len(done) == 3:
            if done[1] == '+' or done[1] == 'Plus' or done[1] == 'plus' or done[1] == 'PLUS':
                index0 = int(done[0])
                index1 = int(done[2])
                print(NumiCalculator.a0(index0, index1))
            elif done[1] == '-' or done[1] == 'Minus' or done[1] == 'minus' or done[1] == 'MINUS':
                index0 = int(done[0])
                index1 = int(done[2])
                print(NumiCalculator.s0(index0, index1))
            else:
                print("Unidentified Funtion call...")
        elif len(done) == 5:
            if done[1] == '+' or done[1] == 'Plus' or done[1] == "PLUS" or done[1] == 'plus' and done[3] == "+" or done[3] == "plus" or done[3] == "PLUS" or done[3] == "Plus":
                index0 = int(done[0])
                index1 = int(done[2])
                index2 = int(done[4])
                print(NumiCalculator.a1(index0, index1, index2))
            elif done[1] == '-' or done[1] == 'Minus' or done[1] == "MINUS" or done[1] == 'minus' and done[3] == "-" or done[3] == "minus" or done[3] == "MINUS" or done[3] == "Minus":
                index0 = int(done[0])
                index1 = int(done[2])
                index2 = int(done[4])
                print(NumiCalculator.s1(index0, index1, index2))
            else:
                print("Unidentified Function call...")
        else:
            print("Sorry!, I am not programmed for this length of expression yet.\nCheck back when we notify you about an upgrade")

NumiCalculator.main_adding_fxn()
print("\nCode develoepd by Masino")
