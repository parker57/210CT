import numpy as np
import re

equations = '''
2x+y+3z=14
x-y+z=4
x+3y-z=2
'''
coefficientRegex = re.compile(r'-?\d*\w')
constituents = coefficientRegex.findall(equations)

coeff_matrix = []
templist = []

solutions = []

for i in (constituents):
    coeff = i[:-1]
    
    if (coeff == ''):
        coeff = 1
    elif (coeff == '-'):
        coeff = -1
    else:
        coeff = int(coeff)
    
    if (not i[-1:].isalpha()):
        coeff_matrix_row = templist[:]
        coeff_matrix.append(coeff_matrix_row)
        del templist [:]
        solutions.append([int(i)])
        continue

    templist.append( coeff )

coeff_matrix = np.matrix(coeff_matrix)
sol_matrix = np.matrix(solutions)
inv_coeff_matrix = np.linalg.inv(coeff_matrix)
print("Inverse coefficient Matrix: \n", inv_coeff_matrix)
print("Solutions Matrix: \n", sol_matrix)

var_deduction_matrix = inv_coeff_matrix * sol_matrix
#print("Variable values Matrix: \n", var_deduction_matrix)

variables = {}
variables['x'] = round(var_deduction_matrix.item(0,0))
variables['y'] = round(var_deduction_matrix.item(1,0))
variables['z'] = round(var_deduction_matrix.item(2,0))

print(variables)


