from random import randint

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
            if i == 0:
                roll = 6
            else:
                roll = die.roll()
            print (roll)
            if roll == 6 and piece.in_prison():
                piece.move(1)
            elif roll == 6:
                 piece.move(6)
            else:
                piece.move(roll)
                goes -= 1
            i += 1
                     
    def get_player_id(self):
        return self.player_id
    
    def quit(self):
        quit()
    

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
        start.val.contents = "OLD"
        self.path.val.contents = piece
        
    def __repr__(self):
        return "({};{})".format(self.owner_id, self.piece_id)

class Die:

    def __init__(self, sides=6):
        self.sides = 6

    def roll(self):
        return randint(1,self.sides)

        
class Board:

    def __init__(self):
        self.board = self.make_board()

    def make_board(self):
        players = Player.player_count
        b = [[[Square("start_square") for i in range(4)] for j in range(players)]]
        
        b.append([Square("general_square") for i in range(13) for j in range(players)])

        b.append([[Square("end_squares") for i in range(5)] for j in range(players)])
        
        return b

    def set_board(self, players):
        for i in players.pieces:
            pass
            
    def display(self):
        for i in self.board:
            print (i)
            print ()
            print ()

class Square:

    def __init__(self, contents):
        self.contents = contents
        
    def __repr__(self):
        return self.contents.__repr__()

def main():
    Player.player_count = 4
    print ("Setting up board...")
    b = Board()
    print (type(b), id(b))
    Player.player_count = 0
    print ("Setting up 4 players and their pieces...")
    players = [Player(b) for i in range(4)]
    print ("Setting up Die...")
    die = Die()
    print ("First player takes his turn...")
    p = 10
    i = 0
    while p > 0:
        b.display()
        print ("--"*50)
        players[i].play(die)
        p -= 1
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    main()