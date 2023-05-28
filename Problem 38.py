"""Guys You can modify this code."""

#Rock paper and cutter
import random
welcome = input("Enter you name: ")
print(f"Welcome {welcome} to Rock, Paper and scissors")
#Game function
def game_fun():
    while True:
        #points
        ai_point = 0
        user_point = 0
        #elements
        choss = ["Rock", "Paper", "Scissors"]
        print(choss)
        #inputs and random choice
        user_choss = input("Enter your choice: ")
        ai_choss = random.choice(choss)
        if user_choss == ai_choss:
            print("Game Tie")
        elif (user_choss == "Rock" and ai_choss == "Scissors") or (user_choss == "Paper" and ai_choss == "Rock") or (user_choss == "Scissors" and ai_choss == "Paper"):
            print("User get point")
            user_point += 1
        elif user_choss == "break":
            print(f"User: {user_point}")
            print(f"A.I: {ai_point}")
            break
        else:
            print("A.I get point")
            ai_point += 1
        print(f"User: {user_point}")
        print(f"A.I: {ai_point}")
#driver code
if __name__ == '__main__':
    game_fun()