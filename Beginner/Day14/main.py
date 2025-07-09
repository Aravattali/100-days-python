from art import logo, versus
from data import data
import random

print(logo)

def follower_count():
    count_a = random.choice(data)
    score = 0

    while True:
        count_b = random.choice(data)
        while count_b == count_a:
            count_b = random.choice(data)

        print(f"Compare A: {count_a['name']} , {count_a['description']} , from  {count_a ['country']}")
        print(versus)
        print(f"Against B: {count_b['name']} , {count_b['description']} , from  {count_b ['country']}")

        ask = input("Who has more followers type A or B ").lower()

        if ask not in ['a', 'b']:
            print("please enter A or B")
            continue

        a = count_a['follower_count']
        b = count_b['follower_count']
        print("\n" * 30)

        if ask == 'a' and a > b:
            score += 1
            print(f"you win, and your score is {score}")
            count_a = count_b
        elif ask == 'b' and b > a:
            score += 1
            print(f"that is right and your score is {score}")
            count_a = count_b
        else:
            print(f"you lose. Your final score is {score}")
            return

follower_count()
