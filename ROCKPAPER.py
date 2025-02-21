# ROCK PAPER AND SCISSORS GAME:
import random

Rock= '''  _______
      ---'   ____)
            (_____)
            (_____)
    VK      (____)
      ---.__(___)
'''
Paper = '''_______
      ---'   ____)____
                ______)
                _______)
    VK         _______)
      ---.__________)'''

Scissors= '''_______
      ---'   ____)____
                ______)
             __________)
    VK      (____)
      ---.__(___)'''

game_img= [Rock , Paper , Scissors]

user_choice=int(input("what would you like to choose?Type 0 for Rock,1 for Paper or 2 for Scissors.\n"))
if user_choice>=0 and user_choice<=2:
    print(game_img[user_choice])
com_choice = random.randint(0,2)
print(f"computer choose:")
print(game_img[com_choice])

if user_choice >= 3 or user_choice <0:
    print("YOU ENTRED INVALID INPUT")
elif user_choice == 0 and com_choice == 0:
    print("congratulations!!! \n WINNER!!!")
elif com_choice == 2 and user_choice == 0:
    print("YOU LOOSE THE GAME!!!\n HARD LUCK!!")
elif user_choice < com_choice:
    print("YOU LOOSE THE GAME!!!\n SORRY!!!")
elif user_choice> com_choice:
    print("VICTORY!!! \n CONGRATULATIONS!!!")
elif user_choice== com_choice:
    print("It's Going INTRESTING!!! \n IT's A DRAW")



