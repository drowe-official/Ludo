#import arcade


class Player:
    def __init__(self, id, colour, name):
        self.id = id
        self.colour = colour
        self.name = name
        self.piece = [Piece()] * 4

    def play():
        #plays his turn...
            #if rolls 6
                #game logic
            #if rolls < 6
                #game logic
        pass

    def quit():
        quit()
        pass
    

class Path:
    
    def __init__(self):
        pass
    
    def next():
        # step through path
        pass
    
    
class Piece:

    def __init__(self, owner, position, path):
        self.owner = owner
        self.position = position #what data struct is position?
        self.path = self.generate_path()

    def generate_path(self):
        # generates the path of a piece
        pass


class Square:

    def __init__(self, contents):
        self.contents = contents


class Board:

    def __init__(self, players, colours=None):
        self.players = players
        self.colours = colours
        self.board = self.make_board(players)

    def make_board(players):
        b = []

        for i in range(players):
            p = []
            for j in range(3):
                p.append([Square(i)] * 6)
            b.append(p)
        return b
    
class Die:

    def __init__(self, sides=6):
        self.sides = 6

    def roll():
        #return random(1, self.sides)

        pass

def main():
    #set up game state
    pass

if __name__ == "__main__":
    main()
