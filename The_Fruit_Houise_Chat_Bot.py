#!/usr/bin/python3

name = input("Hi there!\nWelcome to The Fruit House!\nWhat is your name please ?  ")
answer = input(f"Welcome here {name}...\nWould you like to explore our available fruit serves ?\nPlease use 'Yes' or 'No'  ")
if answer == 'Yes' or answer == 'yes':
    print("Got it!\nCheck below...")
    print("1. Fruit Salad ($10 each).\n2. Parfait ($8 each).\n3. Fruit Pap ($11 each).\n4. Fruit Juice ($5 each).")
    fruit = int(input("Enter 1,2,3 or 4 to select your favourite package:  "))
    if fruit == 1:
        amount = 10
        num = int(input(f"Got it {name}!\nHow many Fruit salad cups would you want?  "))
        total = amount * num
        print(f"Got it!\n{num} Fruit Salad will cost ${total}")
        final = input("Enter 'Shop' to package your fruit salad or 'Cancel' to cancel transaction.  ")
        if final == 'Shop' or final == 'shop':
            print(f"Thank you {name}!\nYou can now go to the counter, pay and collect your goods.")
        elif final == 'Cancel' or final == 'cancel':
            print("Transaction terminated!")
        else:
            print("Unrecognised!\nTry again please.")
    elif fruit == 2:
        amount = 8
        num = int(input(f"Gat you!\nHow many Parfait cups would you need {name} ?  "))
        total = amount * num
        print(f"Well {name}!\n{num} Parfait cups will cost ${total}")
        final = input("Enter 'Shop' to package your parfait or 'Cancel' to cancel transaction.  ")
        if final == 'Shop' or final == 'shop':
            print(f"Thank you {name}!\nYou can now go to the counter, pay and collect your goods.")
        elif final == 'Cancel' or final == 'cancel':
            print("Transaction terminated!")
        else:
            print("Unrecognised!\nTry again please.")
    elif fruit == 3:
        amount = 11
        num = int(input(f"Gat you!\nHow many Fruit paps would do {name} ?  "))
        total = amount * num
        print(f"Good one {name}!\n{num} Fruit paps will cost ${total}")
        final = input("Enter 'Shop' to package your fruit pap or 'Cancel' to cancel transaction.  ")
        if final == 'Shop' or final == 'shop':
            print(f"Thank you {name}!\nYou can now go to the counter, pay and collect your goods.")
        elif final == 'Cancel' or final == 'cancel':
            print("Transaction terminated!")
        else:
            print("Unrecognised!\nTry again please.")
    elif fruit == 4:
        amount = 5
        num = int(input(f"Good!\nHow many Fruit juice cups would be okay {name} ?  "))
        total = amount * num
        print(f"Okay {name}!\n{num} Fruit juice cups will cost ${total}")
        final = input("Enter 'Shop' to package your fruit juice or 'Cancel' to cancel transaction.  ")
        if final == 'Shop' or final == 'shop':
            print(f"Thank you {name}!\nYou can now go to the counter, pay and collect your goods.")
        elif final == 'Cancel' or final == 'cancel':
            print("Transaction terminated!")
        else:
            print("Unrecognised!\nTry again please.")
    else:
        print(f"Wrong input {name}.\nRead instructions and try again.")
    print(f"Please {name}, we would love you give us a rating")
    rating = int(input("1. *\n2. **\n3. ***\n4. ****\n5. *****\nEnter 1,2,3,4 or 5 to give us number of star rating(s):  "))
    if rating == 1:
        print("Oh well! our bad.\nSorry for the inconviniences we may have caused you.\nWe will work on improving our services.")
    elif rating == 2:
        print(f"Okay {name}, We will improve!")
    elif rating == 3:
        print("Thanks for that rating")
    elif rating == 4:
        print(f"Wow that is a cool rating {name}. Thanks!!!")
    elif rating == 5:
        print(f"We are so glad you enjoy our services {name}.\nWe will keep working to serve you better always...")
    else:
        print("Sorry!\nWrong input. Try again next time.")
elif answer == 'No' or answer == 'no':
    print(f"Okay cool!\nThanks for tuning in {name}.")
else:
    print("You have used a wrong input.\nTry 'Yes' or 'No' next time.")
print(f"Have a nice day {name}.\nAlso check back another time.")
print("\nCode developed by Masino")
