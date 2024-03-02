from square import Square

class VaccumCleaner():
    def __init__(self, position):
        self.position = position
        self.clean_squares = 0

    def check_and_return_current_square(self, squares):
        for square in squares:
            if square.position == self.position:
                return square

    def cleanup(self, square : Square):
        square.dirty = 0
        print("Clean", end=",")
        self.clean_squares = self.clean_squares + 1
        
        if (self.clean_squares < 2):
            self.move()

    def check_if_square_is_dirty(self, square : Square):
        if(square.dirty):
            self.cleanup(square)
        else:
            self.clean_squares = self.clean_squares + 1
            if (self.clean_squares < 2):
                self.move()
    
    def move(self):
        if self.position == 1:
            print("Left", end=",")
        else:
            print("Right", end=",")
        self.position = self.position * -1
