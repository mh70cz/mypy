"""
Bite 98. Code your way out of a grid 


https://codechalleng.es/bites/098
"""


DOWN, UP, LEFT, RIGHT = '⇓', '⇑', '⇐', '⇒'
START_VALUE = 1


def print_sequence_route(grid, start_coordinates=None):
    """Receive grid string, convert to 2D matrix of ints, find the
       START_VALUE coordinates and move through the numbers in order printing
       them.  Each time you turn append the grid with its corresponding symbol
       (DOWN / UP / LEFT / RIGHT). See the TESTS for more info.
    """
    matrix = to_matrix(grid)
    flat_with_dir = to_flat(matrix)
    
    
    line = "1"
    direction_prev = flat_with_dir[0][1]
    new_line = False

    for f in flat_with_dir[1:]:
        direction = f[1]
        if new_line:
            new_line = False
        else:
            line += " "        
        if direction == direction_prev: 
                line += str(f[0])
        else:
            line += str(f[0]) + " " + direction + "\n"
            new_line = True
        direction_prev = direction
    
    if not new_line:
        line += " "       
    line +=  str(len(flat_with_dir)+1)
    print(line)
 
   
def to_matrix(grid):
    
    num_lines = grid.split("\n")[1::2]
    return [[int(r) for r in line.split(" ") if r.isnumeric()] for line in num_lines]
    

def to_flat(matrix):
    flat = dict()
    
    matrix_size = len(matrix)
    for row in range(matrix_size):
        for col in range(matrix_size):
            cell = matrix[row][col]        
            flat[cell] = (row,col)
    flat_with_dir = []
    flat_len = len(flat)
    for i in range(1, flat_len):
        cell = flat[i]
        cell_next = flat[i+1]
        direction =  get_direction(cell, cell_next)
        flat_with_dir.append((i, direction))    
    return flat_with_dir

def get_direction(cell, cell_next):
    if cell_next[0] > cell[0] :
        return DOWN
    if cell_next[0] < cell[0] :
        return UP
    if cell_next[1] > cell[1] :
        return RIGHT
    if cell_next[1] < cell[1]:
        return LEFT


        