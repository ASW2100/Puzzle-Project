# Name: Andrew Wolk
# UIC Email: awolk2@uic.edu
# UIC ID: 668250903

# I hereby attest that I have adhered to the rules for quizzes and projects as well as UIC’s
# Academic Integrity standards. Signed: Andrew Wolk

import random

class PuzzlePiece:
    #Represents a single puzzle piece with a unique (x, y) coordinate and a list of connected pieces.

    def __init__(self, x, y):
        self.secret_id = (x, y)
        self.connected_to = []

    def __str__(self):
        return str(self.secret_id)


class Puzzle:
    
    #Represents a jigsaw puzzle with unsolved and solved pieces.
    #Provides methods to simulate solving the puzzle.

    def __init__(self):
        self.u_pieces = []  # Unsolved pieces
        self.s_pieces = []  # Solved pieces

        # Generate 10x10 grid of puzzle pieces
        for y in range(10):
            for x in range(10):
                self.u_pieces.append(PuzzlePiece(x, y))

    def get_rand_piece(self):
        #Returns a random PuzzlePiece from the unsolved pieces list.
        return random.choice(self.u_pieces)

    def are_neighbors(self, id1, id2):
        #Returns True if two pieces are neighbors (adjacent on the grid).       
        x1, y1 = id1
        x2, y2 = id2
        return (abs(x1 - x2) == 1 and y1 == y2) or (abs(y1 - y2) == 1 and x1 == x2)

    def solve_one_piece(self):
        
        #Solves one piece of the puzzle by either picking a starting piece or connecting
        #a new piece to an existing solved piece if they are next to each other.
        
        if not self.s_pieces:
            # First piece: pick randomly and move to solved
            piece = self.get_rand_piece()
            self.u_pieces.remove(piece)
            self.s_pieces.append(piece)
        else:
            while True:
                candidate = self.get_rand_piece()
                connected = False

                for solved_piece in self.s_pieces:
                    if self.are_neighbors(candidate.secret_id, solved_piece.secret_id):
                        # Connect both pieces
                        candidate.connected_to.append(solved_piece)
                        solved_piece.connected_to.append(candidate)
                        connected = True

                if connected:
                    self.u_pieces.remove(candidate)
                    self.s_pieces.append(candidate)
                    break  # Successfully connected one piece

    def solve_all_pieces(self):
        #Recursively solves all the pieces in the puzzle.
        if not self.u_pieces:
            return
        self.solve_one_piece()
        self.solve_all_pieces()


#For testing and visualization
def display_puzzle_summary(puzzle):
    print(f"Total pieces solved: {len(puzzle.s_pieces)}")
    for piece in puzzle.s_pieces:
        connections = [str(p) for p in piece.connected_to]
        print(f"Piece {piece} is connected to: {connections}")


 # test the puzzle solving
if __name__ == "__main__":
     puzzle = Puzzle()
     puzzle.solve_all_pieces()
     display_puzzle_summary(puzzle)

