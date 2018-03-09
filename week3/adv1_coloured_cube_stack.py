import re

file_input = open('cubes.txt')

cube_text = file_input.read()

file_input.close()

#Regex ----
cube_quan_re = re.compile(r'(n) *(=) *(\d+)', re.I)
cube_quan_search = cube_quan_re.search(cube_text)
cube_quan = int(cube_quan_search.group(3))

cube_col_re = re.compile(r'colour (\w*)', re.I)
cube_cols = cube_col_re.findall(cube_text)

cube_len_re = cube_col_re = re.compile(r'length (\d*)', re.I)
cube_lens = cube_col_re.findall(cube_text)
# ----

class Cube:
    def __init__ (self,colour,length):
        self.colour = colour.upper()
        self.length = int(length)

    def __str__(self):
        return ('Length: ' + str(self.length) + ', Colour: ' + str(self.colour))


cubes = []

for i in range(len(cube_cols)):
    cube = Cube(cube_cols[i], cube_lens[i])
    cubes.append(cube)
    
cubes.sort(key=lambda c: c.length, reverse=True)

def print_cl(cl):
    '''simple helper function to print a list of cube objects'''    
    for c in cl:
        print(c)

def total_length(cube_list = cubes):
    total = 0
    for cube in cube_list:
        total += cube.length
    return total

def can_stack(c1, c2):
    '''checks to see if c1 can be placed on c2
    c1 is cube 1, c2 is cube 2.
    returns bool value'''
    if c1.colour != c2.colour and c2.length >= c1.length:
        return True
    return False

tallest_tower = []

def recursive_build(up,p):
    '''
    Recursive function, both lists [up = unplaced, p = placed]
    No/void return type - instead the function updates a non-local list if taller tower builds are found.
    O(n!)
    '''
    #assigning to nonlocal tallest_tower
    if total_length(p) > total_length(tallest_tower):
        tallest_tower[:] = p

    #There's no known base case so search is exhuastive
    for cube in up:
        if can_stack(cube,p[-1]):
            up.remove(cube)
            p.append(cube)

            recursive_build(up,p)



def build_max_tower():
    '''
    Function to build tallest tower from all feasable starting blocks.
    Recursivley build all possible towers that start with the big cubes.
    This is neccessary because sorting may result in a situation such that starting with the first largest block is not optimal,
    e.g) Blue (10), Yellow (10), Yellow (10), Blue (9) [optimal solutions can only occur when the starting block is yellow.
    '''
    big_cube = max(c.length for c in cubes)
    #Find the length of the longest cube(s)
    big_cubes = [c for c in cubes if c.length == big_cube]
    #Create list of all cubes with this length
    for bc in big_cubes:
        #Recursivley build all possible towers that start with the big cubes.
        placed = [bc]
        unplaced = cubes[:]
        unplaced.remove(bc)

        recursive_build(unplaced,placed)

    print('Total length of all blocks:',total_length(cubes))
    print('Tallest feasable length',total_length(tallest_tower))
    print('---Solution---')
    print_cl(tallest_tower)
        

if __name__ == "__main__":
    build_max_tower()
  
