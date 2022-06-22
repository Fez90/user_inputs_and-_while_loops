# input() functions waits for users for enter some text
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
name = input("Please enter your name: ")
print(f"\nHello, {name}!")

# if you need to write a promt that's longer than one line,  you can assign your promt to a variableand pass that variable to input() function. This allows to build a promt with several line.
promt = "If you tell us who you are, we can personalize the messages you see"
promt += "\What is your first name?"
name = input(promt)
print(f"\nHello, {name}!")

# int() converts string into numerical
age = input(f"\nHow old are you? ")
age = int(age)
age >= 18
print(age)
height = input("How tall are you, in inches? ")
height = int(height)
if height >= 48:
    print("You allowed to ride!")
else:
    print("\nYou'll be able to ride when you're a little older")
    
# Modulo operator % divides one number by another and returns the remainder
modul = 4%3
print(modul)
number = input("Enter a number, I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 ==0:
    print(f"\nThe number {number} is even")
else:
    print(f"\nThe number {number} is odd")

# While loops runs as long a certain condition true. 
current_number = 1
while current_number <=5:
    print(current_number)
    current_number += 1
    
# parrot example
promt = "\nTell me something and I will repeat it back to you:"
promt += "\nEnter 'quit to end the program'"
message = ""
while message != 'quit':
    message = input(promt)
    if message != 'quit':
        print(message)
        
# Using a Flag//for a program that should run only as long as many conditions are trueyou can define one variable that determines whether or not the entire program is active
active = True
while active:
    message = input(promt)
    if message == 'quit':
        active = False
    else:
        print(message)
        
# using break to exit a loop. break statement/
travel = "Please enter the name of a city you have visited:"
travel += "(Enter 'quit' when you are finished)"
while True:
    city = input(travel)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")
        
# using continue in a loop ////
# rather than breaking out of a loop entirely without executing the rest of a code you can use continue statement to return to beginning of the loop based on result conditional test
current_number = 0
while current_number <10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
    
# avoiding infinite loops////
# x = 1
# while x <= 5:
#     print(f"\n{x}")
#     x += 1
# is accidentally omit the line x +=1 the loop will run forever//
# x = 1
# while x <= 5:
#     print(f"\n{x}")

# Using while loops with the lists an dictionaries
# moving items from One list to another

# Start with users that need to be verified and empty list to hold confirmed users
    
unconfirmed_users = ['alice','brian','candace']
confirmed_users = []

# verify each user until there are no more unconfirmed users. move each verified user into the list of confirmed users
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
# Display all confirmed users
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# removing all instances of specific values from a list. We used remove() function to remove specific value from a list, function worked in chapter 3 because the value we were interested appeared only once in the list.But what if you want remove all instances of value in the list? Example you have list with 'cat' that repeated several times in the list? To remove all instances you can you while loop/
pets = ['dog','cat','dog','cat','goldfish','cat','rabbit','cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

# filling dictionary with usser input
# example polling program
responses = {}
# set a flag to indicate that polling is active/
polling_active = True
while polling_active:
    # promt for persons name and response/
    name = input("\nWhat is your name? ")
    response = input("\nWhich mountain would you like to climb someday? ")
    # store response in the dictionary/
    responses[name] = response
    # Find out if anyone else is going to take poll/
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False
# Polling is complete.Show results/
print("\n---Poll Results---")
for name,response in responses.items():
    print(f"\n{name} would like to climb {response}")