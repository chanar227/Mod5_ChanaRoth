#Chana Roth
#MCON 141
#Midnight Carnival Program
#10/26/2026


#Challange 1: Check

#set accumulators before loop.
totalAdmits = 0
totalAdmitRev = 0
totalTickRev = 0
totalPrizes = 0
#use a whie loop to run throhg whole system so reprompts each time until sentinel (done) is entered.
while True:
    name = input("Enter your name (or type done to close): ").strip()
    #starts if/elif/else statments to check age requirments.
    #Set sentinel as first if statement.
    if name.lower() == 'done':
        break
    age = int(input("Enter your age: "))
    Vip = input("Do you have a VIP pass? (yes/no): ").strip().lower()

    if age >=8 and Vip == 'yes':
        print("Enter for free.")
        admitPrice = 0
        totalAdmits += 1

    elif age < 8:
        print("Must be accompanied by an adult.")
        #add continue to skip and redo.
        continue

    elif age >= 8 and age <= 17:
        print("Pay $5 and enter.")
        admitPrice = 5
        totalAdmits += 1

    else:
        print("Pay $10 and enter.")
        admitPrice = 10
        totalAdmits += 1
    totalAdmitRev += admitPrice

#Challange 2: Check

    while True:
        #use try except block to catch int() errors and out of range errors with raise.
        try:
            ticket = int(input("How many tickets? (1-20): "))
            if ticket <1 or ticket >20:
                raise ValueError("Number must be between 1 and 20.")
            else:
                price = ticket * 2
                break

        except ValueError as e:
            print(f"Error, {e}.")

    print(f"Accepted: {ticket}")
    print(f"Ticket Cost: ${price}")


    totalTickRev += price



#Challange 3:
    prize = 0
    print("\n---The Lucky Number Game: one ticket per play---")
    print()
    #logic loop to loop through the game for each ticket purchased.
    for i in range(ticket):
        guess = int(input("Guess a number between 1 and 5: "))
        if guess <1 or guess >5:
            print("0 points: A guess outside range of 1 to 5 earns 0")
        elif guess == 3:
            print("Congrats! You guessed the number, here are 10 points!")
            prize += 10
        else:
            print("Sorry, wrong guess, you earn 2 points.")
            prize += 2
    print(f"\nTotal prize points earned today: {prize}")
    print()

    totalPrizes += prize



#Challange 4:
    row = 0
    positions = 0
    while row < 5:
        col = 0
        while col < 5:
            if (row == 0 or row == 4) and (col == 0 or col == 4):
                print("*", end=" ")
            elif (row == 1 or row == 3) and (col == 1 or col == 3):
                print("*", end = " ")
            elif row == 2 and col == 2:
                print("*", end=" ")
            else:
                print("-", end=" ")
            positions += 1
            col += 1

        print()
        row += 1
    print(f"Total number of positions examined: {positions}")

    print()



#Challange 5:
#Added in see on top and rest here.

combinedRev = totalAdmitRev + totalTickRev

print()
print("---End of Night Report---\n")
print(f"Total Visitors admitted: {totalAdmits}")
print(f"Total Admission Revenue: {totalAdmitRev}")
print(f"Total Ticket Revenue: {totalTickRev}")
print(f"Total Prize Points Awarded: {totalPrizes}")
print()
print("Have a Great Night!")


#Testing Record:
#1)
#Inputs: Name = Sarah, Age = 5, VIP = no:
#Expected response: Must be accompanied by an adult. - nad then it skips to next visitor.
#correct.
#2)
#Inputs: Name = Alex, Age = 23, Vip Pass = yes, tickets = 3, Game guess = 8,4,3.
#Expected response = "enter for free" (price = $0), tickets are purchased ($6) and game goes smoothly (12 points). Shows the mystery prize board and reprompts.
#3)
#Inputs: Name = David, Age = 15, VIP = no, ticket = 24. reenter ticket = 5.
#Expected Response:
#Pay $5 and enter, Error, Number must be between 1 and 20, accepted 5 tickets, cost = $10, guesses goes smoothly, 1,2,3,4,5: earn 18 points, mystery prize board appears. reprompts.
#correct
#4)
#Inputs: Name= Fanny, Age = 54,VIP = no, tickets = abc, error, tickets = 2.
#Expected Response: Pay 10$ and enter, (input abc for tickets) - error invalid literal for int()... tickets = 2, pay $4, guess goe smoothly, 1 and 4 = 4 points. Prize board is shown and reprompts.
#correct
#5)
#Inputs: done
#expected response: System ends while loop. and shows end of year results from previous entries/visitors.
#correct.
