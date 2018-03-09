import random
import time
import copy

'''
BST - we will assume ID's can not have identicle values and use that as the point of comparison
'''

#Date/Time Fucntions, to return random dates.

def time_proportion(start, end, format, proportion):
    #return a formatted time, a proportion form start and end.
    start_time = time.mktime(time.strptime(start, format))
    end_time = time.mktime(time.strptime(end, format))

    proportion_time = start_time + proportion * (end_time - start_time)

    return time.strftime(format, time.localtime(proportion_time))


def randomBirth(proportion = random.random()):
    proportion = random.random()
    start = '1/1/1980'
    end = '20/12/2000'
    return time_proportion(start, end, '%d/%m/%Y', proportion)

def randomEnrolment():
    enrolment = '01/09/20'
    enrolment += str(random.randint(15,18))
    return enrolment


firstnames = ['Amanda','Daniel','Charlie','Amelia','Emily','Evie','Sophia','Hollie','Lucas','Dylan','Isaac','Mason']
surnames = ['Smith','Jones','Williams','Taylor','Davies','Brown','Wilson','Evans','Wright','Thompson']
streetnames = ['High Street','Station Road','Main Street','Park Road','Church Road','Church Street','London Road','Victoria Street']
classes = ['MECH','STAT','HIST','COMP','MEDC','LITR','POLT','GEOG']

def makeName():
    return(random.choice(firstnames) +' '+ random.choice(surnames))

def makeAddress():
    return str(random.randint(1,500)) +' '+ random.choice(streetnames)
    
class Student:
    next_ID = 1
    def __init__ (self, name,
                  birth,
                  address,
                  class_id,
                  enrollment,
                  status):
                  
        self.student_id = copy.copy(Student.next_ID)
        self.name = name
        self.birth = birth
        self.address = address
        self.class_id = class_id
        self.enrolled = enrollment
        self.status = status
        Student.next_ID += 1

    def update(self):
        print('UPDATING STUDENT WITH ID -',self.student_id,'\n   --Old Stats--')
        print(self)
        print('\n  --New Stats--')
        self.name = str(input('Name: '))
        self.birth = str(input('Birth (format 20/12/1990): '))
        self.address = str(input('Address: '))
        self.class_id = str(input('Class ID: ')).upper()
        self.enrolled = str(input('Enrolled (format 20/12/2015): '))
        self.status = str(input('Status: '))
        if self.class_id not in classes:
            classes.append(self.class_id)
        print('\n  --Updated--')
        

    def __str__ (self):
        name = ('Student ID: ' + str(self.student_id) +
                '\nName: ' + self.name +
                '\nBirth: ' + self.birth +
                '\nAddress: ' + self.address +
                '\nClass ID: ' + str(self.class_id) +
                '\nEnrolled: ' + self.enrolled +
                '\nStatus: ' + str(self.status) )
                
        return(name)

    def __gt__ (self, other):
        if self.student_id > other.student_id:
            return True
        return False
    
    def __lt__ (self, other):
        if self.student_id < other.student_id:
            return True
        return False


def makeStudent():
    return(Student(makeName(),randomBirth(),makeAddress(),
                   random.choice(classes),randomEnrolment(),
                   random.choice(['undergrad','graduate'])))


#Node and Binary Search Tree (BST) Implementation.


class Node:
    
    def __init__ (self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        
    def children(self):
        children = []
        if self.left:
            children.append(self.left.data)
        if self.right:
            children. append(self.right.data)
        return children
        
    def show(self):
        #Only prints nicely for single digit integers.
        print('',self.data)
        print('/ \\')
        children = ''
        if self.left:
            children += str(self.left.data)
        else:
            children += 'N'
        children += '  '
        if self.right:
            children += str(self.right.data)
        else:
            children += 'N'
        print(children)

    def wipe(self):
        #cut all connections, helpful for inserting nodes into trees without them linking to extraneous data
        wiped = copy.copy(self)
        wiped.parent = None
        wiped.left = None
        wiped.right = None
        return wiped

    def hard_wipe(self):
        #Same as wipe but will erase connections on both ends.
        if self.parent:
            if self < self.parent:
                self.parent.left = None
            elif self > self.parent:
                self.parent.right = None
        if self.right:
            self.right.parent = None
        if self.left:
            self.left.parent = None
        self.parent = None
        self.left = None
        self.right = None

    def sever(self):
        #sever the node from it's parent only if it has any.
        if self.parent:
            if self < self.parent:
                self.parent.left = None
            elif self > self.parent:
                self.parent.right = None

    def __str__(self):
        return str(self.data)

    def __gt__ (self, other):
        if self.data > other.data:
            return True
        return False
    def __lt__ (self, other):
        if self.data < other.data:
            return True
        return False


class BST:
    def __init__ (self, root = None):
        self.root = root
        #Have a population?
        
    def insert(self, node):
        if type(node) != Node:
            node = Node(node)
        if not self.root:
            self.root = node
        else:
            self.append(self.root, node)

    def append(self, cursor_Node, node):
        #Bigger data on the right, smaller on the left.
        #Standard append, placed based on standatd comparisons (student id)
        if type(node) != Node:
            node = Node(node)
        if cursor_Node == node:
            print('Already exists, can not add.')
            return
        elif node < cursor_Node:
            if cursor_Node.left:
                self.append(cursor_Node.left, node)
            else:
                node.parent = cursor_Node
                cursor_Node.left = node
        elif node > cursor_Node:
            if cursor_Node.right:
                self.append(cursor_Node.right, node)
            else:
                node.parent = cursor_Node
                cursor_Node.right = node
        else:
            print('not placed')

    def insert_by_name(self, node):
        if type(node) != Node:
            node = Node(node)
        if not self.root:
            self.root = node
            node.parent = None
        else:
            self.append_by_name(self.root, node)

    def append_by_name(self, cursor_Node, node):
        #Same as append but will go by name not ID.
        #Bigger data on the right, smaller on the left.
        #Standard append, placed based on standatd comparisons (student id)
        if type(node) != Node:
            node = Node(node)
        elif node.data.name <= cursor_Node.data.name:
            if cursor_Node.left:
                self.append_by_name(cursor_Node.left, node)
            else:
                node.parent = cursor_Node
                cursor_Node.left = node
        elif node.data.name > cursor_Node.data.name:
            if cursor_Node.right:
                self.append_by_name(cursor_Node.right, node)
            else:
                node.parent = cursor_Node
                cursor_Node.right = node
        else:
            print('not placed')

    def find(self, student_id):
        return self.search(self.root, student_id).data
    
    def search(self, cursor, student_id):
        #Will return the reference of the node containing the ID.
        if cursor == None:
            raise IndexError('Not a valid index for this BST') 
        #print(cursor.data.student_id)
        if cursor.data.student_id == student_id:
            return cursor
        elif cursor.data.student_id < student_id:
            return self.search(cursor.right, student_id)
        elif cursor.data.student_id > student_id:
            return self.search(cursor.left, student_id)
        else:
            print('Search failed.')

    def update(self, data):
        #find the node by ID and update the node calling the node update method.
        if len(self) > 0 and len(self) >= data:
            self.find(data).update()
        else:
            print(len(self),' items in the tree.', data, 'is out of range.')

    def branch_up(self, root):
        #Recursivley navigate a stack, print bottom right first.
        if root:
            self.branch_up(root.left)
            self.branch_up(root.right)
            print(root.data,'\n')

    def root_down(self, root):
        #Similar to branch up, will print by student_id, attribute by which the tree is ordered (in order) root down
        if root:
            self.root_down(root.left)
            print(root.data,'\n')
            self.root_down(root.right)
            
    def list_populate(self, root , students):
        if root:
            self.list_populate(root.left, students)
            if root not in students:
                students.append(root) # list of student data insead
            self.list_populate(root.right, students)
        return students

    def list(self, root):
        std = []
        return self.list_populate(self.root, std)
    

    def __len__(self):
        #In lieu of a population variable counting students on the tree, len is overridden.
        #Computationally expensive, create list of all nodes in tree.
        return len(self.list(self.root))
        

    def print_by_class(self):
        """Method pulls nodes from the main tree (self) and strips them. 
    They are then placed in there own BSTs by subject. Students are inserted in lexicographic order.
    The tree is displayed and the proccess iterates through all subjects (also alphabetically)."""
    
        students = self.list(self.root)
        for student_class in sorted(classes):
            class_tree = BST()
            for student in students:
                if student.data.class_id == student_class:
                    student = student.wipe()
                    class_tree.insert_by_name(student)
            print('  --',student_class,'--')
            class_tree.root_down(class_tree.root)
            del class_tree

    def print_by_name(self):
        lexicographic_by_name = BST()
        for student in self.list(self.root):
            student = student.wipe()
            lexicographic_by_name.insert_by_name(student)
        lexicographic_by_name.root_down(lexicographic_by_name.root)

    def print_graduates(self, root):
        if root:
            self.print_graduates(root.left)
            if root.data.status == 'graduate':
                print(root.data, '\n')
            self.print_graduates(root.right)

    def print_undergrad_by_class(self):
        students = self.list(self.root)
        for student_class in sorted(classes):
            class_tree = BST()
            for student in students:
                if student.data.class_id == student_class and student.data.status =='undergrad':
                    student = student.wipe()
                    class_tree.insert_by_name(student)
            print('  --',student_class,'--')
            class_tree.root_down(class_tree.root)
            del class_tree
            
    def delete_by_id(self, student_id):
        del_node = self.search(self.root, student_id)

        #Delete root node, just delete root and combine subtrees.
        if not del_node.parent:
            right = del_node.right
            left = del_node.left
            self.root = None
            if right:
                right.parent = None
                self.insert(right)
            if left:
                left.parent = None
                self.insert(left)

        #Delete node with no children
        elif del_node.left is None and del_node.right is None:
            
            if del_node.parent > del_node:
                del_node.parent.left = None
            else:
                del_node.parent.right = None

        #if there is a left child
        elif del_node.left is not None and del_node.right is None:
            if del_node.parent > del_node:
                del_node.parent.left = None
            else:
                del_node.parent.right = None
            del_node.left.parent = None
            self.insert(del_node.left)
            #print(len(self),'left')

        #if there is a right child
        elif del_node.right is not None and del_node.left is None:
            if del_node.parent > del_node:
                del_node.parent.left = None
            else:
                del_node.parent.right = None
            del_node.right.parent = None
            self.insert(del_node.right)
            #print(len(self),'right')

        #Two children
        else:
            if del_node.parent > del_node:
                del_node.parent.left = None
            else:
                del_node.parent.right = None

            self.insert(del_node.right)
            self.insert(del_node.left)
            #print(len(self),'both')

        #print(len(self))

    def delete_graduates(self, root):
        if root:
            self.delete_graduates(root.left)
            self.delete_graduates(root.right)
            #print(root.data,'\n')
            if root.data.status == 'graduate':
                self.delete_by_id(root.data.student_id)
        

if __name__ == '__main__':
    #Creates and populates a tree with students.
    tree = BST()
    intake = []
    for i in range(25):
        intake.append(makeStudent())

    while len(intake) > 0:
        student = random.choice(intake)
        tree.insert(student)
        intake.remove(student)

    #tree.update(20) #TASK 1 
    #tree.print_by_class() #TASK 2 
    #tree.print_by_name() #TASK 3
    #tree.print_graduates(tree.root) #TASK 4
    #tree.print_undergrad_by_class() #TASK 5
    #tree.delete_by_id(20) #Task 6
    #tree.delete_graduates(tree.root) #Task 7

    #tree.root_down(tree.root) #- Main print function - Will print by order of student ID.
    #tree.branch_up(tree.root) #- Second pring, recursivley navigating a stack, printing bottom right first.




    
