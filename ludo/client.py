import time
import os
from network import network
from player import player

def main():
	run = True
	n = network()
	clientNo = n.connect()
	b = Board(4)
	p = player(clientNo, 244, 'blah', b)
	while run:
		time.sleep(2)

		

if __name__ == "__main__":
	main()