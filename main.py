from square import Square
from vaccum_cleaner import VaccumCleaner

'''
about squares status:
0 = clean
1 = dirty

about position:
-1 = left
1 = right
'''

def main():
    #possible configurations
    configs = [(0, 0, -1), (0, 0, 1), (0, 1, -1), (0, 1, 1), (1, 0, -1), (1, 0, 1), (1, 1, -1), (1, 1, 1)]
    #list with all squares
    squares = []

    for config in configs:
        #creating instances of my entities based on configurations
        squares.append(Square(config[0], -1))
        squares.append(Square(config[1], 1))
        vaccum_cleaner = VaccumCleaner(config[2])
        
        print(f"{config}: ", end="")

        #the vacuum cleaner will keep acting until check if all squares are cleaned
        while vaccum_cleaner.clean_squares < len(squares):
            current_square = vaccum_cleaner.check_and_return_current_square(squares)
            vaccum_cleaner.check_if_square_is_dirty(current_square)
        
        #reset the list for the next config
        squares = []

        print("\n")

if __name__ == '__main__':
    main()