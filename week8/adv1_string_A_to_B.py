##    No code is directly copied but I did google the task and learn about Levenshtein distances.
##    I looked at some of the implementations.
##
##    Title: Algorithm Implementation/Strings/Levenshtein distance
##    Authors: Various
##    Date: 22/11/2017
##    Availability: https://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Levenshtein_distance
##
##    Title: Levenshtein Distance
##    Author: Brend Klein
##    Date: 22/11/2017
##    Availability: https://www.python-course.eu/levenshtein_distance.php


operation_cost = {'Delete': 3, 'Insert': 4, 'Replace': 5}

def crude_print(A, B, cost_matrix):
    #Crudely prints a cost matrix, will not resize so high costs and large strings will both decrease readability
    A_title = list(A)
    header = 'A->' + (' ' * 3) #A ->
    for ltr in A_title:
        header += (ltr + '  ')
    B_index = -1
    print(header)
    for cost in cost_matrix:
        if B_index >= 0:
            print(B[B_index],cost)
        else:
            print(' ',cost)
        B_index += 1

def levenshtein(A,B):
    #Levenshtein distances are not symmetrical and asymmetry is amplified by varying costs.
    # A -> B will not necessarily cost the same as B -> A
    A_axis = len(A) + 1 #Column titles will correspond to letters in A
    B_axis = len(B) + 1 #Row titles will correspond to letters in B

    cost_mtx = [[0 for ltr in range(A_axis)] for ltr in range(B_axis)]

    #The cost to turn an empty string into any given string is given by multiplying the size of that string by the cost of insertion.
    for ltr in range(1,A_axis):
        cost_mtx[0][ltr] = operation_cost['Delete'] * ltr
    for ltr in range(1,B_axis):
        cost_mtx[ltr][0] = operation_cost['Insert'] * ltr

    for b_ltr in range(1, B_axis):
        for a_ltr in range(1, A_axis):
            if A[a_ltr-1] == B[b_ltr-1]:
                #If the at the same index are identicle there will be no change to cost
                cost_mtx[b_ltr][a_ltr] = cost_mtx[b_ltr-1][a_ltr-1]
            else:    
                deleted = cost_mtx[b_ltr-1][a_ltr] + operation_cost['Delete']
                inserted = cost_mtx[b_ltr][a_ltr-1] + operation_cost['Insert']
                replaced = cost_mtx[b_ltr-1][a_ltr-1] + operation_cost['Replace']
                #Taking the minimum number is tantramoung to the cheapest operation.
                cost_mtx[b_ltr][a_ltr] = min(deleted,inserted,replaced)
    return cost_mtx

def string_conversion_cost():
    string_A = str(input('Input the first string: '))
    string_B = str(input('Input the second string: '))
    cost_matrix = levenshtein(string_A,string_B)
    print(cost_matrix[-1][-1])
    answer = '.'
    while answer not in ['y','n']:
        answer = str(input('Show cost matrix? [y/n]: ')).lower()[0]
        if answer == 'y':
            crude_print(string_A, string_B, cost_matrix)
    
if __name__ == '__main__':
    string_conversion_cost()




