import time
import os
from network import network
from random import randint

moves = []

class Player:

    player_count = 0

    def __init__(self, b): 
        self.player_id = Player.player_count
        self.pieces = [Piece(self.player_id, i, b) for i in range(4)]

        Player.player_count += 1

    def play(self, die):
        goes = 1
        i = 0
        while i < 3 and goes > 0:
            piece = self.pieces[randint(0,3)]
            roll = die.roll()

            print (roll)
            if roll == 6 and piece.in_prison():
                moves.append(6)
                piece.move(1)
            elif roll == 6:
                moves.append(6)
                piece.move(6)
            else:
                moves.append(roll)
                piece.move(roll)
                goes -= 1
            i += 1
                     
    def get_player_id(self):
        return self.player_id
    
    

class Step:
    
    def __init__(self, val=None):
        self.val = val
        self.next = None
    
    def look_forward(self, n):
        if n <= 0:
            return True
        elif not self.next:
            return False
        
        return self.next.look_forward(n-1)
    
    def journey(self):
        p = []
        s = self
        while s:
            p.append(s)
            s = s.next
        return p
        
    def __repr__(self):
        return self.val.__repr__()
    
	
class Piece:

    def __init__(self, owner_id, piece_id, b):
        self.owner_id = owner_id
        self.piece_id = piece_id
        self.board = b
        self.path = self.generate_path()
		
    def generate_path(self):
        i = 2 + self.owner_id * 13
        step = Step(self.board.board[0][self.owner_id][self.piece_id])
        step.val.contents = self
        start = step
        
        j = 0
        while j < (Player.player_count+1) * 51:
            step.next = Step(self.board.board[1][i])
            step = step.next
            j += 1
            i = (i + 1) % 52
            
        j = 0
        while j < 5:
            step.next = Step(self.board.board[2][self.owner_id][j])
            step = step.next
            j += 1
        return start
        
    def in_prison(self):
        return self.path.val == self.board.board[0][self.owner_id][self.piece_id]
        
    def move(self, steps):
        start = self.path
        piece = self.path.val
        if self.path.look_forward(steps):
            for i in range(steps):
                self.path = self.path.next
        start.val.contents = self.__repr__()
        self.path.val.contents = piece
        
    def __repr__(self):
        return "({};{})".format(self.owner_id, self.piece_id)

    def __repr__1(self):
        return "'blah'"

		
class Die:

    def __init__(self, sides=6):
        self.sides = 6

    def roll(self):
        return randint(1,self.sides)

        
class Board:

    def __init__(self, players):
        self.board = self.make_board(players)

    def make_board(self, players):
        b = [[[Square("start_square") for i in range(4)] for j in range(players)]]
        
        b.append([Square("general_square") for i in range(13) for j in range(players)])

        b.append([[Square("end_squares") for i in range(5)] for j in range(players)])
        
        return b

    def display(self):
        for i in self.board:
            print (i)


class Square:

    def __init__(self, contents):
        self.contents = contents
        
    def __repr__(self):
        return self.contents.__repr__()

def main():
    run = True
    n = network()
    clientNo = n.getBo()
    print(clientNo)
    #p = player.Player(clientNo, 244, 'blah', b)
    print ("Setting up board...")
    #player.Player_count = 0
    print("Setting up 4 players and their pieces...")
    b = Board(4)
    players = [Player(b), Player(b), Player(b), Player(b)]
    print("Setting up Die...")
    die = Die()
    print("First player takes his turn...")
    while run:
        while True:
            re = n.getBo()
            re = n.send(re)
            if re == "br":
                break
            print(re)
            time.sleep(1)
        keyboard = input("roll board or quit: \n")
        if keyboard == "roll":
            global moves
            players[clientNo].play(die)
            print(moves)
            roll = n.send(moves)
            moves = []
        if keyboard == "board":
            b.display()
        if keyboard == "quit":
            quit()

if __name__ == "__main__":
    main()