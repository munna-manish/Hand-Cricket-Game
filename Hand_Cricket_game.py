# Hand Cricket Game 

import random
while True:
    toss = random.choice(["heads","tails"])
    player_toss = input("Enter 'heads' or 'tails' for toss: ").lower()
    game_over = False
    if player_toss == toss:
        print("You won the toss!")
        player_choice = input("Do you want to bat or ball? Enter 'bat' or 'ball': ").lower()
        comp_score = 0
        player_score = 0
        if player_choice == "bat":  # For toss selection: 'BAT' by the player
            while not game_over:  #  Player first batting
                player_turn = int(input("You: "))
                if player_turn > 10:
                    print("Run are only valid from 1-10")
                comp_turn = random.randint(1,10)
                print(f"Computer: {comp_turn}")
                player_score += player_turn
                if player_turn == comp_turn:
                    print(f"You lost the bat! Your score is: {player_score}\nComputer's goal:",player_score+1)
                    game_over = True
            print("Now it's the Computer's turn! Get ready to ball!")
            game_over = False
            comp_score2 = 0
            while not game_over:  # Computer second batting
                player_turn2 = int(input("You: "))
                if player_turn2 > 10:
                    print("Run are only valid from 1-10")
                comp_turn2 = random.randint(1,10)
                print(f"Computer: {comp_turn2}")
                comp_score2 += comp_turn2
                if player_score<comp_score2:
                    game_over = True
                    print(f"You lost! Computer's score is: {comp_score2}\tYour score:{player_score}")
                elif player_turn2 == comp_turn2 and player_score>comp_score2:
                    game_over = True
                    print(f"You won! Computer's score is: {comp_score2}\nYour score:{player_score}")
                if comp_score2==player_score:
                    print(f"It's a draw! Computer's score: {comp_score2}\nYour score:{player_score}")
                    game_over = True
                    
                
        else:     # If the player selects 'BALL' for the toss
            while not game_over:      #  Computer first batting
                player_turn = int(input("You: "))
                if player_turn > 10:
                    print("Run are only valid from 1-10")
                comp_turn = random.randint(1,10)
                print(f"Computer: {comp_turn}")
                comp_score += comp_turn
                if player_turn == comp_turn:
                    print(f"You won the bat! Computer's score is: {comp_score}\nYour goal:",comp_score+1)
                    game_over = True
            print("Now it's the Computer's turn to ball! Get ready to bat!")
            game_over = False
            player_score2 = 0
            while not game_over:     # Player second batting
                player_turn2 = int(input("You: "))
                if player_turn > 10:
                    print("Run are only valid from 1-10")
                comp_turn2 = random.randint(1,10)
                print(f"Computer: {comp_turn2}")
                player_score2 += player_turn2
                if player_score2>comp_score:
                    game_over = True
                    print(f"You won! Computer's score is: {comp_score}\tYour score:{player_score2}")
                elif player_turn2 == comp_turn2 and player_score2<comp_score:
                    game_over = True
                    print(f"You lost! Computer's score is: {comp_score}\nYour score:{player_score2}")


# This code is executed when the player loses the toss
    else:
        print("Sorry you lost the toss!")
        comp_choice = random.choice(["bat","ball"])
        print(f"Computer chose to {comp_choice}")
        comp_score = 0
        player_score = 0
        if comp_choice == "ball":   # Computer choice for the toss is 'BALL'
            while not game_over:   # Computer balling
                player_turn = int(input("You: "))
                if player_turn > 10:
                    print("Run are only valid from 1-10")
                comp_turn = random.randint(1,10)
                print(f"Computer: {comp_turn}")
                player_score += player_turn
                if player_turn == comp_turn:
                    print(f"You lost the bat! Your score is: {player_score}\nComputer's goal:",player_score+1)
                    game_over = True
            print("Now it's the Computer's turn! Get ready to ball!")
            game_over = False
            comp_score2 = 0
            while not game_over:   # Computer second batting
                player_turn2 = int(input("You: "))
                if player_turn > 10:
                    print("Run are only valid from 1-10")
                comp_turn2 = random.randint(1,10)
                print(f"Computer: {comp_turn2}")
                comp_score2 += comp_turn2
                if player_score<comp_score2:
                    game_over = True
                    print(f"You lost! Computer's score is: {comp_score2}\tYour score:{player_score}")
                elif player_turn2 == comp_turn2 and player_score>comp_score2:
                    game_over = True
                    print(f"You won! Computer's score is: {comp_score2}\nYour score:{player_score}")
                elif player_turn == comp_turn2 and player_score==comp_score2:
                    game_over = True
                    print(f"It's a draw!\nYour score: {player_score}\tComputer's score:{comp_score2}")
        else:     # Computer's choice for toss is 'BAT'
            while not game_over: # Computer batting
                player_turn = int(input("You: "))
                if player_turn > 10:
                    print("Run are only valid from 1-10")
                comp_turn = random.randint(1,10)
                print(f"Computer: {comp_turn}")
                comp_score += comp_turn
                if player_turn == comp_turn:
                    print(f"You won the bat! Computer's score is: {comp_score}\nYour goal:",comp_score+1)
                    game_over = True
            print("Now it's the Computer's turn to ball! Get ready to bat!")
            game_over = False
            player_score2 = 0
            while not game_over: # Computer balling
                player_turn2 = int(input("You: "))
                if player_turn > 10: 
                    print("Run are only valid from 1-10")
                comp_turn2 = random.randint(1,10)
                print(f"Computer: {comp_turn2}")
                player_score2 += player_turn2
                if player_score2>comp_score:
                    game_over = True
                    print(f"You won! Computer's score is: {comp_score}\tYour score:{player_score2}")
                elif player_turn2 == comp_turn2 and player_score2<comp_score:
                    game_over = True
                    print(f"You lost! Computer's score is: {comp_score}\nYour score:{player_score2}")
                elif player_turn2 == comp_turn2 and player_score==comp_score:
                    game_over = True
                    print(f"That's a draw\nYour score = {player_score}\tComputer's score = {comp_score}")  # In case of draw
                







