'''
Written function that takes an input list (1 Arg) of numbers
Returns a list of those numbers which are also Kaprekar numbers

Kaprekar number: Non-negative integer which can be represented conventionally
    AND as the sum of two parts derived from itself squared.

    Example: 45 is Kaprekar, 45^2 = 2025 & 45 = 20+25.
    Numbers can lead with is a zero but the right hand number can not equal 0.
      1 is Kaprekar, 1^2 = 1 or 01, 1 = 0+1.
      10 is not Kaprekar, 10^2 = 100, 10+0 = 100 but RHS can not be 0.
    
'''

def is_kaprekar (num):
    '''Check to see if a number is a Kaprekar number
    1 Argument: integer. Returns Boolean
    O(2 log(n))
    '''
    
    if (num < 1):
        return False
    if (num == 1):
        return True
    
    num_squared = num * num
    ns_string = str(num_squared)
    ns_length = len(ns_string)

    
    for i in range(1, ns_length ):
        
        first_val = ns_length - i
        sec_val = int(ns_string[-first_val:])
        
        added = int(ns_string[:i]) + sec_val

        if ( added == num and sec_val != 0 ):
            return True

    return False 
                   

def kaprekar_list (num_list):
    '''Create list of all integers in the list that are Kaprekar numbers
    1 Argument: list. Returns list
    O(n)
    '''
    kaprekar_nums = []
    for n in (num_list):
        if (is_kaprekar(n)):
            kaprekar_nums.append(n)
    return kaprekar_nums


#Test first 10 000 numbers
for i in range(10000):
    if (is_kaprekar(i)):
        print(i)

    

