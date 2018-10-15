from random import randint
items=["stone","paper","scissors"]
computer=items[randint(0,2)]
player=False
pscore=0
cscore=0
while (player==False):
	player=input("\nstone,paper,scissors :\n")
	if player==computer:
		print("\nTie!")
	elif player=="stone":
		if computer=="paper":
		    print("\nYou lose!",computer,"covers",player)
		else:
		    print("\nYou win!",player,"blunts",computer)
	elif player=="paper":
		if computer=="scissors":
		    print("\nYou lose!",computer,"cuts",player)
		else:
		    print("\nYou win!",player,"covers",computer)
	elif player=="scissors":
		if computer=="stone":
		    print("\nYou lose...",computer,"blunts",player)
		else:
		    print("\nYou win!",player,"cuts",computer)
	else:
		print("\nSorry your spelling is not valid !! Check your Spelling !!")
	player = False
	computer = items[randint(0,2)]
	
