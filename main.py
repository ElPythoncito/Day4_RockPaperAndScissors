#  100 Days of Code
#  Day 4 Rock Paper or Scissors
import random

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
options = [rock, paper, scissors]
computer = random.randint(0, 2)
user_election = int(input("What do you choose. "
                          "Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

print(f"Computer choose: \n{options[computer]}")
print(f"User choose: \n{options[user_election]}")

if computer == user_election:
    print("It's a tie.")
elif computer == 0 and user_election == 1:
    print("You win 🎊🎊.")
elif computer == 0 and user_election == 2:
    print("You lose 😪.")
elif computer == 1 and user_election == 0: #---------------------------------
    print("You lose 😪.")
elif computer == 1 and user_election == 2:
    print("You win 🎊🎊.")
elif computer == 2 and user_election == 0: #-----------------------------------
    print("You win 🎊🎊.")
elif computer == 2 and user_election == 1:
    print("You lose 😪.")

input("\n\nType ENTER to finish!!!")
