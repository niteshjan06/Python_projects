# computer will pick rock, paper or scissor at random by itself.
import random
player_bot = 0
player_you = 0
i = 1
sets = input("Enter number of sets you want to play: ")
while(i<=sets):


# code for condition of the game.
    computer_choice = random.choice(["rock","paper","scissor"])
    choice = input("Choice[rock,paper or scissor]: ")


# taking input from the user.
    your_choice = choice.lower()


#printing your choice and computer's choice.
    print(f"Computer choose: {computer_choice}")
    print(f"You choose: {your_choice}")


#conditions for winning / losing the game
    if(computer_choice == "rock" and your_choice == "paper"):
       player_you += 1 
       print("You Win!")
       print("<-- Game Over -->")
    elif(computer_choice == "rock" and your_choice == "scissor"):
        print("You lose!")
        player_bot += 1
        print("<-- Game Over -->")
    elif(computer_choice == "paper" and your_choice == "rock"):
        print("You lose!")
        player_bot += 1
        print("<-- Game Over -->")
    elif(computer_choice == "paper" and your_choice == "scissor"):
        print("You Win!")
        player_you += 1 
        print("<-- Game Over -->")
    elif(computer_choice == "scissor" and your_choice == "rock"):
        print("You win!")
        player_you += 1 
        print("<-- Game Over -->")
    elif(computer_choice == "scissor" and your_choice == "paper"):
        print("You lose!")
        player_bot += 1
        print("<-- Game Over -->")
    elif(computer_choice == your_choice):
        print("It's a draw")
        print("Try again")
    else:
        print("Invalid Selection")
    i += 1

    
# conditions for the printing the scores. 
if(player_you > player_bot):
    print("You win the entire set")
    print(f"your score is {player_you}")
    print(f"Bot's score is {player_bot}")
elif(player_you == player_bot):
     print("It's a Draw")
     print("Try again !")
else:
    print("You lose the entire set")
    print(f"your score is {player_you}")
    print(f"Bot's score is {player_bot}")
