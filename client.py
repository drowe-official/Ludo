#import arcade


class Player:
    def __init__(self, player_id, colour, name, board): 
        self.player_id = player_id
        self.colour = colour
        self.name = name
        self.board = board
        self.piece = [Piece(self, i) for i in range(4)]

    def play():
        #plays his turn...
            #if rolls 6
                #game logic
            #if rolls < 6
                #game logic
        pass
    
    def get_player_id(self):
        return self.player_id
    
    def quit():
        quit()
    

class Step:
    
    def __init__(self, val=None):
        self.val = val
        self.next = None
    
    def look_forward(self, n):
        # look forward n steps. Returns False if n > steps left.
        pass
    
    
class Piece:

    def __init__(self, owner, piece_id):
        self.owner = owner
        self.piece_id = piece_id
        self.step = self.generate_path(owner.board, piece_id)

    def generate_path(self, board, piece_id):
        player_id = self.owner.get_player_id()
        i = 2 + player_id * 13
        j = 0
        p = Step(board.board[0][player_id][piece_id])
        start = p
        while j < board.players:
            p.next = Step(board.board[1][i])
            p = p.next
            j += 1
            i = (i + 1) % 52

        j = 0
        while j < 5:
            p.next = Step(board.board[2][player_id][j])
            p = p.next
            j += 1
        return start


class Square:

    def __init__(self, contents):
        self.contents = contents


class Board:

    def __init__(self, players, colours=None):
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

        
class Die:

    def __init__(self, sides=6):
        self.sides = 6

    def roll():
        #return random(1, self.sides)

        pass


def main():
    pass

if __name__ == "__main__":
    main()
