# Nome do Aluno/a: Marcos Vinicius Mendes Faria
# Disciplina/semestre: Inteligência Artificial
# Turma: Sistemas de Informação, 7º Período
# Professor: Sergio Nery Simões

'''
about squares status:
0 = clean
1 = dirty

about position:
-1 = left
1 = right
'''

class Square:
    def __init__(self, dirty, position):
        self.dirty = dirty
        self.position = position

class VaccumCleaner:
    def __init__(self, position):
        self.position = position
        self.clean_squares = 0

    def check_and_return_current_square(self, squares):
        for square in squares:
            if square.position == self.position:
                return square

    def cleanup(self, square: Square):
        square.dirty = 0
        print("Clean", end=",")
        self.clean_squares += 1

        if self.clean_squares < 2:
            self.move()

    def check_if_square_is_dirty(self, square: Square):
        if square.dirty:
            self.cleanup(square)
        else:
            self.clean_squares += 1
            if self.clean_squares < 2:
                self.move()

    def move(self):
        if self.position == 1:
            print("Left", end=",")
        else:
            print("Right", end=",")
        self.position = self.position * -1

def main():
    print("(left square, right square, initial robot position): actions")
    # possible configurations
    configs = [(0, 0, -1), (0, 0, 1), (0, 1, -1), (0, 1, 1),
               (1, 0, -1), (1, 0, 1), (1, 1, -1), (1, 1, 1)]
    # list with all squares
    squares = []

    for config in configs:
        # creating instances of my entities based on configurations
        squares.append(Square(config[0], -1))
        squares.append(Square(config[1], 1))
        vaccum_cleaner = VaccumCleaner(config[2])

        print(f"{config}: ", end="")

        # the vacuum cleaner will keep acting until check if all squares are cleaned
        while vaccum_cleaner.clean_squares < len(squares):
            current_square = vaccum_cleaner.check_and_return_current_square(squares)
            vaccum_cleaner.check_if_square_is_dirty(current_square)

        # reset the list for the next config
        squares = []

        print("\n")

if __name__ == '__main__':
    main()
