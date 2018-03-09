##    A lorry can carry at most n kilograms. The name of the materials, the amount of material in kilograms
##    and the material price per kilo are known. Compute a load composition in such a way that the value
##    (price) of the load is maximum.
##    Input:
##    2
##     N = 10
##     Copper 7kg 65
##     Plastic 15 kg 50
##     Gold 4kg 100
##    Output:
##     Load composition value = 790
##     4 kg of gold and 6 kg of copper

import re

file_input = open('adv2_ex2.txt')
#adv2_ex2 & adv_ex1 in this directory, both different inventories
inventory = file_input.read()
#readlines() might make more sense, file_input.readlines() returns a list of lines.
file_input.close()

print(inventory)

class Material: #capitalization is convention PEP 8
    '''Material Data type, instantiated with string, string, int)
    Quantity can be read as string because weights could use different units.
    '''
    def __init__(self, name, quantity, value):
        self.name = name
        self.quan = quantity 
        self.val = int(value)


lorry_capacity = re.compile(r'(N) *(=) *(\d+)', re.I)
material_row = re.compile(r'(\w+) *(\d+kg) *(\d+)', re.I)

material_inv = material_row.findall(inventory) 
lorry_line = lorry_capacity.search(inventory)

load = int(lorry_line.group(3)) #third item found should be lorry capacity/load

material_list = [] #Local list of Material types found using Regex.


for item in material_inv:
    #for loop to add all instances that match material_row regex to the material_list
    material_type = Material(item[0],int(item[1][:-2]),item[2])
    material_list.append(material_type)


def total_quantity(material_list):
    '''Helper function to view the quantity of remaining materials in a local/runtime list.
    1 argument: list of Materials, defined by Material class.
    returns int (the total weight of resources left)
    '''
    total = 0
    for m in material_list:
        total += m.quan
    return total
    
def printMatList(material_list):
    '''Helper function to view the contents of a local/runtime list containing Material types.
    1 argument: list of Materials, defined by Material class.
    returns print statements breakdown (void).
    '''
    for i in material_list:
        print(i.name,i.quan,i.val)

def sortList_Expensive_First (material_list):
    material_list.sort(key=lambda mtrl:mtrl.val, reverse=True) #sorts resources by value, most expensive first.


def load_lorry (capacity, material_list):
    '''function to load lorry, greedy packing - to get the most valuable load call sortList_Expensive_First -
    function first then use that list to load_lorry.
    2 arguments: int(capacity of lorry), list(of Material data type to be loaded into the lorry)
    returns list (Material data types and quantity that should go into lorry to maximize value)
    O(n) - linear when material_list argument is sorted list.
    '''
    loaded = []
    
    for mtrl in material_list:
        load_amount = min(capacity, mtrl.quan)
        load = Material(mtrl.name, load_amount, mtrl.val)  
        loaded.append(load)
        capacity = capacity - load_amount
        mtrl.quan = mtrl.quan - load_amount

        if mtrl.quan>0 or capacity==0: 
            break

    return loaded

def material_list_value(material_list):
    value = 0
    for item in material_list:
        value = value + (item.quan * item.val)
    return value

def print_lorry_load(lorry_load):
    for loaded_material in lorry_load[:-1]:
        print(loaded_material.quan, 'kg of', loaded_material.name+', ', end='')
    print('and', lorry_load[-1].quan, 'kg of', lorry_load[-1].name)
        

print('Total Value of items:',material_list_value(material_list))
print('Total Weight of of items:',total_quantity(material_list),"KGs")

print('\nThe Lorrry can hold ',load,'KGs\n')
sortList_Expensive_First(material_list)
loaded_lorry = load_lorry(load,material_list)
print('   using:',total_quantity(loaded_lorry),'of',load,'KGs\n')

print('Load composition value = ',material_list_value(loaded_lorry))
print_lorry_load(loaded_lorry)


    


