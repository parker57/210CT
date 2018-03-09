##     Adapt the Quick Sort algorithm to find the mth smallest element out of a list of n integers, where m is
##    read from the standard input.
##    For example, when m = 5, your version of Quick Sort will output the 5th smallest element out of your
##    input list.

import random

def quickselect(array, m):

    def sort(array, left, right, index):
        if left == right:
            return array[left] #Found/ base case.
        #If return array is only one long, will leave stack

        pivot = left #Primitive pivot selection/ not ideal.

        wall = pivot
        for i in range(left+1, right+1):
            if array[i] < array[left]:
                wall += 1
                array[wall], array[i] = array[i], array[wall]

        array[wall], array[left] = array[left], array[wall]

        if index>wall:
            #If index is greater than wall, sort larger
            return sort(array, wall+1, right, index)
        elif index<wall:
            #If index is less than wall, sort smaller
            return sort(array, left, wall-1, index)
        else:
            #If index is equal to wall, mth smallest found.
            return array[wall]

    if len(array) < 1:
        return

    if m not in range(0, len(array)):
        raise IndexError('Index searched is out of range, remember index uses zero-based numbering')

    return sort(array, 0, len(array) - 1, m)

if __name__ == '__main__':
    array_size = int(input('How many integers should the list be? '))
    m = int(input('Finding the Mth smallest, what is m? '))
    test_list = [random.randint(0,99) for i in range(array_size)]
    print('List: ',test_list)
    print(m,'th element is: ',quickselect(test_list,m))
    print('Sorted list: ',sorted(test_list))
