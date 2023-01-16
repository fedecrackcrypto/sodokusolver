from sodoku import Sodoku, Variable


class SodokuSolver():
    
    def __init__(self, sodoku: Sodoku) -> None:
        self.sodoku = sodoku
        self.domains = dict()
        self.assigments = dict()
        for i in range(self.sodoku.size):
            for j in range(self.sodoku.size):
                if self.sodoku.board[i][j].number is None:
                    self.domains[self.sodoku.board[i][j]] = list(range(1,self.sodoku.size+1))
                else:
                    self.domains[self.sodoku.board[i][j]] = [self.sodoku.board[i][j].number]
                    self.assigments[self.sodoku.board[i][j]] = self.sodoku.board[i][j].number
                    
    
    def revise(self, x: Variable, y: Variable) -> bool:
        """
        Make variable x arc consistent with variable y.

        Removes any value in self.domains[x] that leaves self.domains[y] without any option.
        
        Returns True if one or more elements were remove from x domain, otherwise False.
        """
        revised = False
        for i in self.domains[x].copy():
            if i in self.domains[y]:
                copy = self.domains[y].copy()
                copy.remove(i)
                if len(copy) == 0:
                    self.domains[x].remove(i)
                    revised = True
        return revised

    def ac3(self, arcs = None) -> bool:
        """
        Check for arc consistency in all the possible arcs of the problem.
        
        If no arcs are specified it creates a queue of all the arcs in the problem. That is to
        say all the combinations (x,y) where y can't be the same value as x.
        
        Returns True if arc consistency is enforced in all domains, otherwise a domain was left
        empty while enforcing arc consistency and returns False.
        """
        queue = set()
        if arcs is None:
            #Create queue for all variables
            for x in self.domains.keys():
                if len(neighbors := self.sodoku.get_neighbors(x)) != 0:
                    for y in neighbors:
                        queue.add((x,y))
        else:
            queue = arcs
        while len(queue) != 0:
            (var_x,var_y) = queue.pop()
            if self.revise(var_x,var_y):
                if len(self.domains[var_x]) == 0:
                    return False
                neighbors = self.sodoku.get_neighbors(var_x)
                for var_z in neighbors:
                    if var_z != var_y:
                        queue.add((var_z,var_x))
        return True
    
    def assigment_complete(self, assigments: dict) -> bool:
        """
        Returns True if all variables have been assigned, otherwise False.
        """
        if len(assigments) == len(self.domains):
            return True
        return False
    
    def select_unassigned_variable(self, assigments: dict) -> Variable:
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """
        unassigned_variables = list()
        for x in self.domains.keys():
            if x not in assigments.keys():
                n_remaining = len(self.domains[x])
                neighbors = self.sodoku.get_neighbors(x)
                unassigned_neighbors = list(filter(lambda neighbor: neighbor in assigments.keys(), neighbors))
                n_neighbors = len(unassigned_neighbors)
                unassigned_variables.append((x,n_remaining,n_neighbors))
        unassigned_variables.sort(key= lambda x: x[2], reverse= True)
        unassigned_variables.sort(key= lambda x: x[1])
        return(unassigned_variables[0][0])

    def order_domain_values(self, assigments: dict, var: Variable) -> list:
        values = list()
        for x in self.domains[var]:
            n_constraint = 0
            neighbors = self.sodoku.get_neighbors(var)
            for neighbor in neighbors:
                if neighbor not in assigments.keys() and x in self.domains[neighbor]:
                    n_constraint += 1
            values.append((x,n_constraint))
        values.sort(key= lambda x: x[1])
        return(values)

    def consistent(self, assigments: dict) -> bool:
        for var_x in assigments:
            for var_y in assigments:
                if var_x.number != None and self.sodoku.are_neighbors(var_x, var_y) and var_x.number == var_y.number:
                    return False
        return True

    def backtrack(self, assigments: dict):
        if self.assigment_complete(assigments):
            return assigments
        var = self.select_unassigned_variable(assigments)
        values = self.order_domain_values(assigments, var)
        for value in values:
            if value is None:
                print("here")
            value = value[0]
            temp_assigments = self.assigments.copy()
            temp_assigments[var] = value
            if self.consistent(temp_assigments):
                self.assigments[var] = value
                queue = set()
                for neighbor in self.sodoku.get_neighbors(var):
                    queue.add((neighbor,var))
                previous_domains = self.domains.copy()
                self.ac3(queue)
                result = self.backtrack(assigments)
                if result is not None:
                    return result
                assigments.pop(var)
                self.domains = previous_domains
        return None
    
    def solve(self):
        self.ac3()
        solution = self.backtrack(self.assigments)
        print(solution)
        return(solution)

    
# sodoku = Sodoku(9)
# sodoku.change_value(0,1,6)
# sodoku.change_value(0,4,7)
# sodoku.change_value(0,7,2)
# sodoku.change_value(1,4,8)
# sodoku.change_value(1,5,3)
# sodoku.change_value(1,7,1)
# sodoku.change_value(1,8,6)
# sodoku.change_value(2,0,9)
# sodoku.change_value(2,3,4)
# sodoku.change_value(2,7,7)
# sodoku.change_value(3,2,5)
# sodoku.change_value(3,3,6)
# sodoku.change_value(3,4,4)
# sodoku.change_value(4,0,8)
# sodoku.change_value(4,1,1)
# sodoku.change_value(4,6,5)
# sodoku.change_value(5,5,2)
# sodoku.change_value(5,6,3)
# sodoku.change_value(6,1,9)
# sodoku.change_value(6,2,3)
# sodoku.change_value(6,5,1)
# sodoku.change_value(6,7,8)
# sodoku.change_value(7,1,7)
# sodoku.change_value(7,6,2)
# sodoku.change_value(8,2,4)
# sodoku.change_value(8,3,5)
# sodoku.change_value(8,4,6)
# sodoku.change_value(8,5,9)
# sodoku.change_value(8,6,1)

# solver = SodokuSolver(sodoku)
# solver.solve


        












        




