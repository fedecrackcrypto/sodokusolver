import numpy as np
import math


class Variable():
    """
    A class representing a sodoku number in the grid on the position (i, j)
    """
    def __init__(self, i: int, j: int, grid: int, number = None) -> None:
        self.i = i
        self.j = j
        self.number = number
        self.grid = grid
    
    def __str__(self) -> str:
        return f"This variable has the number {self.number} in the position {self.i}, {self.j}"



class Sodoku():
    """"
    A class representing the Sodoku board
    """

    def __init__(self, size: int) -> None:
        self.size = size
        self.board = np.full((self.size, self.size), fill_value=None)
        #Defining subgrid values and populating the nparray with variables
        self.subgrid_size = int(math.sqrt(self.size))
        grid_i = -self.subgrid_size
        for i in range(self.size):
            if (i)%self.subgrid_size == 0:
                grid_i += self.subgrid_size
            grid_j = 0
            for j in range(self.size):
                if (j)%self.subgrid_size == 0:
                    grid_j += 1
                self.board[i][j] = Variable(i,j, grid_j + grid_i)
        

    def __str__(self):
        return f"{self.board}"

    def change_value(self, i: int, j: int, number: int) -> None:
        """
        Change the value of the position [i, j] of the Sodoku to number.
        """
        if number in range(1, self.size+1):
            self.board[i,j].number = number
        else:
            raise ValueError("Invalid Number")
    
    def reset_value(self, i: int, j: int) -> None:
        """
        Change the value of the variable in the position [i, j] of the Sodoku to None.
        """       
        self.board[i,j].number = None

    def get_neighbors(self, i: int, j: int) -> set:
        """
        Defining neighbors as any variable that has a constraint with the variable in the [i,j] position.
        Return a list of all the neighbors of the variable in the [i,j] position.
        """
        neighbors = set()
        var = self.board[i][j]
        for x in range(self.size):
            for y in range(self.size):
                y = self.board[x][y]
                if (var.i == y.i or var.j == y.j or var.grid == y.grid) and var != y:
                    neighbors.add(y)
        return neighbors
            
