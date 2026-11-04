player1=input("rock(r),paper(p),scissors(s)")
computer="s"

if player1 == "r" and computer == "s":
    print ("player1, wins")
if player1 == "s" and computer == "p":
    print ("player1, wins")
if player1 == "p" and computer == "r":
    print ("player1, wins")
if computer == "r" and player1 == "s": 
    print ("computer, wins")
if computer == "s" and player1 == "p":
    print ("computer, wins")
if computer == "p" and player1 == "r":
    print ("computer,wins")
else:
    print ("draw")
    

