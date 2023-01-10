import numpy as np

SODOKU_SIZE = 9

# class Variable():
#     """
#     A class representing a sodoku number in the grid on the position (i, j)
#     """
#     def __init__(self, i, j, number) -> None:
#         self.i = i
#         self.j = j
#         self.number = number
    
#     def __str__(self) -> str:
#         return f"This variable has the number {self._number} in the position {self.i}, {self.j}"

#     @property
#     def number(self):
#         return self._number

#     @number.setter
#     def number(self, number):
#         if number not in range(1,10):
#             raise ValueError("Invalid number")
#         self._number = number

class Sodoku():
    """"
    A class representing the Sodoku board
    """

    def __init__(self, file) -> None:
        with open(file) as f:
            contents = f.read().splitlines()
            self.height = len(contents)
            self.width = len(contents[0])
            self.board = np.full((self.height, self.width), fill_value=None)
            for i, line in enumerate(contents):
                for j, char in enumerate(line):
                    if char == "#":
                        continue
                    elif char.isnumeric():
                        self.change_value(i, j, int(char))
                    else:
                        raise ValueError("Invalid Char")

    def __str__(self):
        return f"{self.board}"

    def change_value(self, i: int, j: int, number: int) -> None:
        """
        Change the value of the position [i, j] of the Sodoku to number.
        """
        if number in range(1, SODOKU_SIZE+1):
            self.board[i,j] = number
        else:
            raise ValueError("Invalid Number")
            
        



print(Sodoku("sodokus\sodoku0.txt"))



