#!/usr/bin/python3

print("Hi there!\nWelcome to The Fruit House...\nPlease note that we deliver only within Enugu State, Nigeria.")
name = input("What is your name please:  ")
answer = input(f"Welcome here {name}...\nWould you like to explore our available fruit serves ?\nPlease use 'Yes' or 'No':  ")
if answer == 'Yes' or answer == 'yes':
    print("Got it!\nCheck below...")
    print("1. Fruit Salad ($10 each).\n2. Parfait ($8 each).\n3. Fruit Pap ($11 each).\n4. Fruit Juice ($5 each).")
    fruit = int(input("Enter 1,2,3 or 4 to select your favourite package:  "))
    if fruit == 1:
        amount = 10
        num = int(input(f"Got it {name}!\nHow many Fruit salad cups would you want:  "))
        total = amount * num
        print(f"Got it!\n{num} Fruit Salad will cost ${total}")
        final = input("Enter 'Shop' to package your fruit salad or 'Cancel' to cancel transaction:  ")
        if final == 'Shop' or final == 'shop':
            location = input(f"Okay {name}...\nEnter your preferred delivery address(Please avoid errors):  ")
            email = input("Provide a valid email address please:  ")
            phone = int(input(f"Got it {name}!\nNow provide a phone number for possible direction and safe delivery:  "))
            print(f"{phone} is registered.\nOur dispatch rider will leave for the provided address in 10 minutes")
            print(f"Thank you {name}!")
        elif final == 'Cancel' or final == 'cancel':
            print("Transaction terminated!")
        else:
            print("Unrecognised!\nTry again please.")
    elif fruit == 2:
        amount = 8
        num = int(input(f"Gat you!\nHow many Parfait cups would you need {name}:  "))
        total = amount * num
        print(f"Well {name}!\n{num} Parfait cups will cost ${total}")
        final = input("Enter 'Shop' to package your parfait or 'Cancel' to cancel transaction:  ")
        if final == 'Shop' or final == 'shop':
            location = input(f"Okay {name}...\nEnter your preferred delivery address(Please avoid errors):  ")
            email = input("Provide a valid email address please:  ")
            phone = int(input(f"Got it {name}!\nNow provide a phone number for possible direction and safe delivery:  "))
            print(f"{phone} is registered.\nOur dispatch rider will leave for the provided address in 10 minutes")
            print(f"Thanks for shopping with us {name}!")
        elif final == 'Cancel' or final == 'cancel':
            print("Transaction terminated!")
        else:
            print("Unrecognised!\nTry again please.")
    elif fruit == 3:
        amount = 11
        num = int(input(f"Gat you!\nHow many Fruit paps would do {name}:  "))
        total = amount * num
        print(f"Good one {name}!\n{num} Fruit paps will cost ${total}")
        meat_pie = input("Fruit pap always go with meat pie($5 each), Would you need some ?\nUse 'yes or 'no':  ")
        if meat_pie == 'Yes' or meat_pie == 'yes':
            meat_pie_price = 5
            meat_pie_num = int(input("How many would be okay for you please:  "))
            meat_pie_final_price = meat_pie_price *  meat_pie_num
            print(f"Got it!\nOrdered meat pie is ${meat_pie_final_price}.")
            final_total = total + meat_pie_final_price
            print(f"Well {name}, your final total is: ${final_total}.")
        elif meat_pie == 'No' or meat_pie == 'no':
            print("Okay got it!\nNo meat pie for you...")
        else:
            print("Sorry!\nThat is an incorrect input. Try again.")
        final = input("Enter 'Shop' to package your shopping or 'Cancel' to cancel transaction:  ")
        if final == 'Shop' or final == 'shop':
            location = input(f"Okay {name}...\nEnter your preferred delivery address(Please avoid errors):  ")
            email = input("Provide a valid email address please:  ")
            phone = int(input(f"Got it {name}!\nNow provide a phone number for possible direction and safe delivery:  "))
            print(f"{phone} is registered.\nOur dispatch rider will leave for the provided address in 10 minutes")
            print(f"Thank you {name} for patronizing us...")
        elif final == 'Cancel' or final == 'cancel':
            print("Transaction terminated!")
        else:
            print("Unrecognised!\nTry again please.")
    elif fruit == 4:
        amount = 5
        num = int(input(f"Good!\nHow many Fruit juice cups would be okay {name}:  "))
        total = amount * num
        print(f"Okay {name}!\n{num} Fruit juice cups will cost ${total}")
        pisa = input(f"{name}, Fruit juice go well with Pizza most often. Would you try it ?\nUse 'yes' or 'no':  ")
        if pisa == 'Yes' or pisa == 'yes':
            pisa_sise = int(input("Select...\n1. Small(1.4kg) is $3.\n2. Medium(2.9kg) is $5.\n3. Large(5kg) is $7.\nEnter 1, 2 or 3 to select your preferred size:  "))
            if pisa_sise == 1:
                pisa_price = 3
                pisa_num = int(input("How many 1.4kg Pizza would do please:  "))
                total_pisa = pisa_price * pisa_num
                print(f"Noted {name}.\nOrdered Pizza costs ${total_pisa}")
                total_shopping = total + total_pisa
                print(f"The total of your Fruit juice and Pizza is: ${total_shopping}")
            elif pisa_sise == 2:
                pisa_price = 5
                pisa_num = int(input("How many 2.9kg Pizza would do please:  "))
                total_pisa = pisa_price * pisa_num
                print(f"Got it {name}!\nOrdered Pizza costs ${total_pisa}")
                total_shopping = total + total_pisa
                print(f"The total of your Fruit juice and Pizza is: ${total_shopping}")
            elif pisa_sise == 3:
                pisa_price = 7
                pisa_num = int(input("How many 5kg Pizza would be enough:  "))
                total_pisa = pisa_price * pisa_num
                print(f"Alright {name}!\nOrdered Pizza costs ${total_pisa}")
                total_shopping = total + total_pisa
                print(f"The total of your Fruit juice and Pizza is: ${total_shopping}")
            else:
                print("Sorry...\nThis input is an incorrect option\nCheck the list and try again")
        elif pisa == 'No' or pisa == 'no':
            print("Okay, Noted!\nNo Pizza for you.")
        else:
            print("Sorry...\nWrong input. Read instructions and try again.")
        final = input("Enter 'Shop' to package your foods or 'Cancel' to cancel transaction:  ")
        if final == 'Shop' or final == 'shop':
            location = input(f"Okay {name}...\nEnter your preferred delivery address(Please avoid errors):  ")
            email = input("Provide a valid email address please:  ")
            phone = int(input(f"Got it {name}!\nNow provide a phone number for possible direction and safe delivery:  "))
            print(f"{phone} is registered.\nOur dispatch rider will leave for the provided address in 10 minutes")
            print(f"Thank you for shopping with us today {name}!")
        elif final == 'Cancel' or final == 'cancel':
            print("Transaction terminated!")
        else:
            print("Unrecognised!\nTry again please.")
    else:
        print(f"Wrong input {name}.\nRead instructions and try again.")
    print(f"Please {name}, we would love you give us a rating...")
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
