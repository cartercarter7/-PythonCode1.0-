import random

play_again = "y"

while play_again == "y":



    player1=input("rock(r),paper(p),scissors(s): ")

while player1 not in ["r", "p", "s"]:
    print ("Invalid choice. Try again.")
    player1 = input("rock (r), paper (p), or scissors (s): ")

#computer randomly chooses 
computer_number = random.randint (1,3)

if computer_number == 1:
    computer = "s"
elif computer_number == 2:
    computer = "r"
else:
    computer="p"

print("computer chose:",)

#main starts here 
if player1 == "r" and computer == "s":
    print ("player1, wins")
elif player1 == "s" and computer == "p":
    print ("player1, wins")
elif player1 == "p" and computer == "r":
    print ("player1, wins")
elif computer == "r" and player1 == "s": 
    print ("computer, wins")
elif computer == "s" and player1 == "p":
    print ("computer, wins")
elif computer == "p" and player1 == "r":
    print ("computer,wins")
else:
    print ("draw")

    #Ask to play again
    plaay_again = input ("would you like to play again? (y/n): ")

print("thanks for playing!")


