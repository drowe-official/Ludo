import time
import os
from network import network
import player

def main():
	run = True
	n = network()
	clientNo = n.getBo()
	#print(clientNo)
	#p = player.Player(clientNo, 244, 'blah', b)
	print ("Setting up board...")
	b = Board(4)
	#player.Player_count = 0
	print("Setting up 4 players and their pieces...")
	players = [player.Player(b), player.Player(b), player.Player(b), player.Player(b)]
	print("Setting up Die...")
	die = player.Die()
	print("First player takes his turn...")
	while run:
		#players[clientNo].play(die)
		time.sleep(2)
		#print (b.display())

		

if __name__ == "__main__":
	main()