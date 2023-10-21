rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
while True:
    
    print("Welcome to rock paper scissors")
    player = int(input("Enter your choice 0 = rock, 1 = paper and 2 = scissors: "))
    choice = player
    print("Players choice:")
    if choice == 0:
        print(rock)
    elif choice == 1:
        print(paper)
    elif choice == 2:
        print(scissors)
    else:
        print("please input a valid number")
        

    computer = random.randint(0,2)
    choice = computer
    print("Computers choice:")
    if choice == 0:
        print(rock)
    elif choice == 1:
        print(paper)
    elif choice == 2:
        print(scissors)

    if (player == 0) and (computer == 1) or (player == 1) and (computer == 2) or (player == 2) and (computer == 0):
        print("Computer wins")
    elif (player == 1) and (computer == 0) or (player == 2) and (computer == 1) or (player == 0) and (computer == 2):
        print("Player wins")
    else:
        print ("This is a draw")
        
