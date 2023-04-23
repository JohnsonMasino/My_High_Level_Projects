#!/usr/bin/python3

import random as rd

generated_number = rd.randint(1, 5)
#input_number = int(input("Please enter a number to sign in for gift: "))
trial_times = 2
while True:
    gift_number = int(input("Please enter a numer to win: "))
    if gift_number == generated_number:
        print("Congratulations!\nYou won")
        print(f"{generated_number} is the lucky number with the gift")
        break
    elif trial_times <= 0:
        print("Sorry You did not win.\nYou have exhausted your chances.")
        print(f"The number with the gift was: {generated_number}.")
        break
    else:
        print("Sorry you did not win.\nTry again")
        print(f"You have {trial_times} times left")
        trial_times -= 1
        continue
else:
    print("All done!\nThanks for tuning in")
print("\nCode developed by Masino")    
