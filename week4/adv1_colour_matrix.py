##    Consider a n x m matrix, with elements decimal digits (natural numbers between 1 and 9), representing
##    colours. A connected set associated to an element is the set of elements that may be reached from this
##    element, by successive moves on a same row or column preserving the same color. It is to determine
##    the size and the colour of the biggest connected set. In case of multiple solutions, display them all.
##    Input: n = 5 m = 6 and the values within the matrix are randomised, between 1 and 9)
##    1 3 5 6 6 6
##    8 8 5 2 2 2
##    2 8 8 3 4 1
##    7 1 8 5 9 9
##    9 8 3 4 2 2
##    Output: The size of the biggest set is 5 and the colour is whichever colour you represented by 8.

import re
import random

'''For Reading from a text file'''
##file_input = open('colour_matrix.txt')
##col_mtx = file_input.read()
##file_input.close()
##
##row_finder = re.compile(r'(n) *(=) *(\d+)', re.I)
##col_finder = re.compile(r'(m) *(=) *(\d+)', re.I)
##
##rows = int(row_finder.search(col_mtx).group(3))
##cols = int(col_finder.search(col_mtx).group(3))
##
##matrix_txt = col_mtx.split('\n')[1:-1] #Will create a list of all but the first and last rows.
##
##matrix = []
##
##for row in matrix_txt:
##    #simple for loop to covert the col_mtx string into a usable matrix.
##    row = row.split(' ')
##    row = list(map(int,row))
##    matrix.append(row)

# ---For random matrix ---
rows = random.randint(3,15)
cols = random.randint(3,15)
matrix = []
for r in range(rows):
    ro = []
    for c in range(cols):
        num = random.randint(1,5)
        ro.append(num)
    roa = ro[:]
    matrix.append(roa)
    del ro[:]
# --- End of random Matrix creation --- 

print('-- The Matrix --')
for r in matrix:
    print(r)

num_set = [] #Global varaible list that will be recursivley added to

def in_mtx(r,c):
    #Boolean function to check if co-ordinate is in matrix.
    if 0 <= r < rows and 0 <= c < cols:
        return True
    return False

def can_connect(r1,c1,r2,c2):
    #check if the two positions in the matrix are the same.
    if in_mtx(r1,c1) and in_mtx(r2,c2) and (r2,c2) not in num_set:
        if matrix[r1][c1] == matrix[r2][c2]:
            #Checks to see if the location's values are the same.
            return True
    return False

def get_set(r,c):
    num_set.append((r,c))
    if can_connect(r,c,r-1,c): #check up
        get_set(r-1,c)
    if can_connect(r,c,r,c+1): #check right
        get_set(r,c+1)
    if can_connect(r,c,r+1,c): #check down
        get_set(r+1,c)
    if can_connect(r,c,r,c-1): #check left
        get_set(r,c-1)


def biggest_colour_sets():
    #Quadratic
    #Build the largest possible set from every possible index in the matrix.
    biggest_sets = [[]]
    for r in range(rows):
        for c in range(cols):
            del num_set[:]
            get_set(r,c)
            if len(num_set) > len(biggest_sets[0]):
                #If new biggest is found, disregard all previous biggests's
                del biggest_sets[:]
                biggest_sets.append(set(num_set))
            if len(num_set) == len(biggest_sets[0]) and set(num_set) not in biggest_sets:
                #set makes identicle sets equal - prevents the same set being added twice.
                biggest_sets.append(set(num_set))

    return biggest_sets

if __name__ == '__main__':
    set_list = biggest_colour_sets()
    print(len(set_list),'solution(s) of length',len(set_list[0]))
    for s in set_list:
        col_num_cord = list(set_list[0])[0]
        r,c = col_num_cord
        col_num = matrix[r][c]
    print('The size of the biggest set is',len(set_list[0]),'and the colour is whichever colour you represented by',col_num)
    for sol_list in set_list:
        print(list(sol_list))
    

