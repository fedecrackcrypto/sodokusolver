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
    
    def __eq__(self, other):
        return (
            (self.i == other.i) and
            (self.j == other.j) and
            (self.number == other.number) and
            (self.grid == other.grid)
        )

    def __repr__(self):
        return f"Variable(i:{self.i}, j:{self.j}, number:{self.number}, grid:{self.grid})"

    def __hash__(self):
        return hash((self.i, self.j, self.number, self.grid))



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

    def get_neighbors(self, var: Variable) -> set:
        """
        Defining neighbors as any variable that has a constraint with the variable in the [i,j] position.
        Return a list of all the neighbors of the variable in the [i,j] position.
        """
        neighbors = set()
        for x in range(self.size):
            for y in range(self.size):
                var_neighbor = self.board[x][y]
                if (var.i == var_neighbor.i or var.j == var_neighbor.j or var.grid == var_neighbor.grid) and var != var_neighbor:
                    neighbors.add(var_neighbor)
        return neighbors
    
    def are_neighbors(self, var_x: Variable, var_y: Variable):
        """
        Returns True if the variables in the position [i,j] and [i_neighbor,j_neighbor] are neighbors,
        otherwise False.
        """
        if (var_x.i == var_y.i or var_x.j == var_y.j or var_x.grid == var_y.grid) and var_x != var_y:
            return True
        return False  
