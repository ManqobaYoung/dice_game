import random

print("welcome to Manqoba Young game of dice")

player_1 = input("Enter your name , player 1 : ")
player_2 = input("Enter your name , player 2 : ")

list_number = [1, 2, 3, 4, 5, 6]

print("let the game start...")

player_1_number = random.choice(list_number)

player_2_number = random.choice(list_number)

print(player_1 + " your number is : " + str(player_1_number))
print(player_2 + " your number is : " + str(player_2_number))


if player_1_number > player_2_number:
    print("You won, " + player_1+ "!")
elif player_1_number < player_2_number:
        print("You won, " + player_2+ "!")
else:
    print("It is  a tie")