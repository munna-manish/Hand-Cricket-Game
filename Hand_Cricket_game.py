# Hand Cricket Game
import random
toss = random.choice(["heads","tails"])
player_toss = input("Enter 'heads' or 'tails' for toss: ").lower()
game_over = False
if player_toss == toss:
    print("You won the toss!")
    player_choice = input("Do you want to bat or ball? Enter 'bat' or 'ball': ").lower()
    comp_score = 0
    player_score = 0
    if player_choice == "bat":
        while not game_over:
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
        while not game_over:
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
            
    else:
        while not game_over:
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
        while not game_over:
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



else:
    print("Sorry you lost the toss!")
    comp_choice = random.choice(["bat","ball"])
    print(f"Computer chose to {comp_choice}")
    comp_score = 0
    player_score = 0
    if comp_choice == "ball":
        while not game_over:
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
        while not game_over:
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
            
                
                
            
    else:
        while not game_over:
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
        while not game_over:
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



