##    The factorial for a non-negative integer n, n!, is defined as: 0! = 1 n! = n * (n-1)! (n > 0). The input to
##    your program consists of several lines, each containing two non-negative integers, n and m, both less
##    than 2^31. For each input line, output a line stating whether or not m divides n!.
##    Example input:
##    6 9
##    6 27
##    20 10000
##    20 100000
##    Example output:
##    9 divides 6!
##    27 does not divide 6!
##    10000 divides 20!
##    100000 doe not divide 20!

import os
import re

#this_dir = os.path.abspath('.')
file_input = open('adv1.txt') 
text_input = file_input.read()
file_input.close()

n_and_m_finder = re.compile(r'(\d+ *)(\d+)')

input_stream = n_and_m_finder.findall(text_input)

def factorial(n):
    '''
    Receive Factorial of n
    One argument: integer
    Return type: interger
    '''
    fact = 1
    for i in range(2,n+1):
        fact*=i
    return fact

def is_divisible(a,b):
    '''Funtion to see if the second argument divided by the frist returns an integer
    Two arguments: integers.
    Return type: boolean.
    '''
    #This function is only appropriate for small values of n.
    if (b%a == 0):
        return True
    return False


def m_divides_by_n_factorial(n, m):
    #Function to use for numbers less than 2^31 as opposed to 231
    fact = 1
    for i in range(2,n+1):
        fact *= i
        if fact > m and fact%m == 0:
            return True
    return False

def adv1(n,m):
    '''Can't think of a good variable name, combinaion of is_divisible and factorial.
    Two arguments: integers.
    Return type: void (print statements).
    '''
    #n_fact = factorial(n)
    if (m_divides_by_n_factorial(n, m)):
        print(m, ' divides ', n, '!')
    else:
        print(m, ' does not divide ', n, '!')

for line in input_stream:
    adv1(int(line[0]), int(line[1]))

'''
if __name__ == "__main__":
    import sys
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    adv1(n,m)
'''
  
