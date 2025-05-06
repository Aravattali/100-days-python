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
user_action = input("Choose one of these three Rock , Paper , Scissors: ")
possible_action = ['Rock' , 'Paper' , 'Scissors']
computer_action = random.choice(possible_action)
print(computer_action)
if user_action == computer_action:
    print("It's a ti")
elif (user_action == "Rock" and computer_action == "Scissors") or \
     (user_action == "Paper" and computer_action == "Rock") or \
     (user_action == "Scissors" and computer_action == "Paper"):
    print("You win!")
else:
    print("You lose!")
