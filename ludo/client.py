import time
import os
from network import network
from player import player

width = 1000
height = 1000

class Board:

    def __init__(self, players = None, colours=None):
        self.players = players
        self.colours = colours
        self.board = self.make_board(players)

    def make_board(self, players):
        b = [[[Square("start_square") for i in range(4)] for j in range(players)]]
        
        b.append([Square("general_square") for i in range(13) for j in range(players)])

        b.append([[Square("end_squares") for i in range(5)] for j in range(players)])
        
        return b

    def set_board():
        for i in players:
            pass

class Square:

    def __init__(self, contents):
        self.contents = contents





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