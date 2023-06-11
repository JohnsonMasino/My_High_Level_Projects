#!/usr/bin/python3

#This is the main file for the numi-calculator_clone project

class NumiCalculator():
    """Defines the class of the mathematical expression
    """
    from first_fxn import adding0 as a0, subtracting0 as s0, multiplying0 as m0, dividing0 as d0
    from second_fxn import adding1 as a1, subtracting1 as s1, multiplying1 as m1, dividing1 as d1
    
    def main_fxn():
        """defines the mathematical expression function
        """
        expression = input("Please enter your mathematical expression here. Division in word means 'over': ")
        done = expression.split(" ")
        
        if len(done) == 3:
            """indicates only two values calculation
            """
            index0 = int(done[0])
            index1 = int(done[2])
            if done[1] == '+' or done[1] == 'Plus' or done[1] == 'plus' or done[1] == 'PLUS':
                """calls the addition function only
                """
                print(NumiCalculator.a0(index0, index1))
            elif done[1] == '-' or done[1] == 'Minus' or done[1] == 'minus' or done[1] == 'MINUS':
                """calls the subtraction function only
                """
                print(NumiCalculator.s0(index0, index1))
            elif done[1] == "*" or done[1] == "times" or done[1] == "Times" or done[1] == "TIMES":
                """calls the multiplication functio only
                """
                print(NumiCalculator.m0(index0, index1))
            elif done[1] == "/" or done[1] == "Over" or done[1] == "over" or done[1] == "OVER":
                """calls the division function only
                """
                try:
                    print(NumiCalculator.d0(index0, index1))
                
                except ZeroDivisionError:
                    print("Division by zero is not allowed")
                except (ValueError):
                    print("OOps!!!\nEnter numbers only...")
            else:
                print("Unidentified Funtion call...")
        elif len(done) == 5:
            """this indicates three values calculation
            """
            index0 = int(done[0])
            index1 = int(done[2])
            index2 = int(done[4])
            
            if done[1] == '+' or done[1] == 'Plus' or done[1] == "PLUS" or done[1] == 'plus' and done[3] == "+" or done[3] == "plus" or done[3] == "PLUS" or done[3] == "Plus":
                """calls the addition function only
                """
                print(NumiCalculator.a1(index0, index1, index2))

            elif done[1] == '-' or done[1] == 'Minus' or done[1] == "MINUS" or done[1] == 'minus' and done[3] == "-" or done[3] == "minus" or done[3] == "MINUS" or done[3] == "Minus":
                """calls the subtraction function only
                """
                print(NumiCalculator.s1(index0, index1, index2))

            elif done[1] == '*' or done[1] == 'Times' or done[1] == "TIMES" or done[1] == 'times' and done[3] == "*" or done[3] == "times" or done[3] == "TIMES" or done[3] == "Times":
                """calls the multiplication functio only
                """
                print(NumiCalculator.m1(index0, index1, index2))
            
            elif done[1] == '/' or done[1] == 'Over' or done[1] == "OVER" or done[1] == 'over' and done[3] == "/" or done[3] == "over" or done[3] == "OVER" or done[3] == "Over":
                """
                calls the division function only
                """
                try:
                    print(NumiCalculator.d1(index0, index1, index2))
                except ZeroDivisionError:
                    print("Division by zero is not allowed please...")
                except (ValueError):
                    print("OOps!!!\nEnter numbers only...")
            
            else:
                print("Unidentified Function call...")
        
        else:
            print("Sorry!, I am not programmed for this length of calculation yet.\nOr try separating your inputs with a single space")

NumiCalculator.main_fxn()
print("\nCode develoepd by Masino")
