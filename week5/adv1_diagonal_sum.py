##    Find the smallest sum of n integer numbers taken from different diagonals parallel with the main
##    diagonal, and including the main diagonal of a matrix A of size m × m. Note: Do not consider diagonals
##    with less than n elements in it!
##    Example input m = 5 and n = 4:
##    3 1 5 6 9
##    2 4 1 9 7
##    3 5 2 8 10
##    4 2 1 6 8
##    1 4 7 9 1
##    Output: 10 (sum of 3,4,2, and 1 on the main diagonal). Please remember you do not need to check
##    anything parallel to the other diagonal, but only the main diagonal (starting top left and ending bottom
##    right).

import random

#Random Matrix Creation
matrix_size = random.randint(3,9)
rows = matrix_size
cols = matrix_size #Task demands m x m matrix.
matrix = []
for r in range(rows):
    #Makes rows full of random numbers and append those rows.
    ro = []
    for c in range(cols):
        num = random.randint(1,9)
        ro.append(num)
    roa = ro[:]
    matrix.append(roa)
    del ro[:]
#End of Random Matrix Creation
    
print('-- Random Matrix --')
for r in matrix:
    print(r)

n = 0
while n not in range(1, matrix_size + 1):
    n = int(input('What is \'n\'? \n'))
    if n not in range(1, matrix_size + 1) or type(n) != int:
        print('n must between 1 and', matrix_size)

via_dia = matrix_size-n #via_dia = VIABLE DIAGONALS
#The amount of diagonals worth checking, starting from index 0,0
#and iterating the starting point both horizontally and vertically.

def get_diagonal_list (mtx, start_row, start_col):
    '''three arguments: the matrix, the starting indexes for 2D matrix.
    Returns a list of all numbers in line with start (including start)
    with that line being a diagonal drawn from start SE.'''
    diags = [mtx[start_row][start_col]]
    mtx_size = len(mtx)
    dia_row = start_row + 1
    dia_col = start_col + 1
    while dia_row < mtx_size and dia_col < mtx_size:
        diags.append(mtx[dia_row][dia_col])
        dia_row += 1
        dia_col += 1
    return diags
    

via_diag_lists = [get_diagonal_list(matrix, 0, 0)]
for i in range(1, via_dia+1):
    via_diag_lists.append(get_diagonal_list(matrix, 0, i))
    via_diag_lists.append(get_diagonal_list(matrix, i, 0))

smallest_sum = via_diag_lists[0] #Posisble but unlikely, suitable UB.

for lst in via_diag_lists:
    sorted_list = sorted(lst)
    smallest_n = sorted_list[:n]
    #print(sum(smallest_sum))
    if sum(smallest_n) <= sum(smallest_sum):
        smallest_sum = smallest_n
        on_diag = lst


print('Smallest list is',smallest_sum,'with a sum of',sum(smallest_sum))
print('Part of diagonal (parallel to) main',on_diag)
    
