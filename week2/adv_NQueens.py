##    Write a program to solve the problem of the eight queens: i.e. find their placement on the chess board so that
##    they have do not have the possibility to attack each other (read more about it here:
##    https://en.wikipedia.org/wiki/Eight_queens_puzzle). Decide whether you want to find only one correct
##    scenario in which the queens are not attacking each other or all correct scenarios (more difficult). Please feel
##    free to represent the board as you wish. What is the efficiency of all different functions in the program (or
##    overall if not using more than one function)?

import numpy
import logging
import time
from tkinter import *

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s -%(message)s')

#In many instances it seemed to make more sense to refer to columns in matricies as such, and in some x seemed better.
#x will denote column as why denotes row - and in both instances vice versa.


class Board_canvas():

    qualitative_cols = ["#913cca", "#004d00", "#f40017", "#ffbf00", "#dc49e0", "#00cd25", "#0055f3", "#00cab2", "#d26b30", "#000000"]
    col1 = "#CCCCCC"
    
    def __init__(self, parent, N=8, square_size = 50):
        '''Class which can render the board state (Board class) as a Tkinter canvas.

        __init__ arguments:
        parent -- the parent of this widget, typically grid or root.
        N -- Board size (always square so only needs 1 dimension)
        square_size -- pixel size of one chess square.
        '''
        self.bdw = 5 #border_width
        self.sq_size = square_size
        self.rows, self.columns = N, N
        self.parent = parent
        canvas_width = self.columns * self.sq_size
        canvas_height = self.rows * self.sq_size
        self.canvas = Canvas(parent, width=canvas_width,
                             height = canvas_height,
                             bd=self.bdw-1, relief=RIDGE, background="#EEEEEE")
        self.draw_board()

    def draw_board(self):
        #Creates board and colours squares.
        #Could iterate every other item (1:-1:2) instead
        for r in range(self.rows):
            for c in range(self.columns):
                if ((r + c) % 2 == 0): 
                    x1 = (c*self.sq_size) + self.bdw
                    y1 = ((self.rows-r-1) * self.sq_size) + self.bdw
                    x2 = x1 + self.sq_size
                    y2 = y1 + self.sq_size
                    self.canvas.create_rectangle(x1, y1, x2, y2,
                                                 fill=self.col1, tags="dark chess squares",
                                                 width=0)
    def add_spot(self,col,row):
        '''Adds a red spot at specified coordinate - initially used to show which points a Queen attacked.'''
        padding = int(self.sq_size/4)
        
        x1 = (col*self.sq_size) + self.bdw + padding
        y1 = (row * self.sq_size) + self.bdw + padding
        x2 = x1 + int(self.sq_size/2) 
        y2 = y1 + int(self.sq_size/2)
        self.canvas.create_oval(x1,y1,x2,y2, fill='red', outline="")
        
    def show_placements(self, queen_locations, colours = False):
        '''Method which renders in their coordinates as parsed with the queen_locations arguments, colours will give each queen a unique colour which can make for easier differentiation.
        '''
        c_index = 0 # colour index, only used if colours = True.
        text_col = "#000000"
        if colours:
            text_col = self.qualitative_cols [c_index]
            
        for queen in queen_locations:
            added = int(self.sq_size/2)
            x = (queen[1] * self.sq_size) + self.bdw + added
            y = (queen[0] * self.sq_size) + self.bdw + added
            self.canvas.create_text(x,y,text='\u265b', font=("bold", 20), fill = text_col, tag="queen" )#+str(board_state.queens.index([spot[0],spot[1]])+1)
            c_index += 1
            c_index %= len(self.qualitative_cols)

            if colours:
                text_col = self.qualitative_cols [c_index]
                                    
                                    

class Board():
    def __init__(self, N=8):
        '''Board class, creates Board Matrix of size N

        N -- Dimensions of board & amount of queens that need to be placed in mutually safe places to constitute a solution.
        '''
        self.matrix = numpy.zeros(shape=(N,N))
        self.queens = []
        self.size = N
        self.solutions = 0
        self.solutions_list = []
        
    def size(self):
        return self.size
    
    def safe(self,col,row):
        '''Method to see if matrix position is safe (not in the path of an existing queen).

        Row and Col are reversed (relative to normal format) which is confusing
        col -- column position of query
        row -- row position of query
        '''
        if int(self.matrix[col][row])==0:
            return True
        return False


    def place(self,col,row):
        #Warning: No safety check is taken place is this function, manually placing queens can result in mutual check.
        #Row and Col are reversed which is confusing
        self.queens.append([col,row])
        NE_SW_diag = col + row
        NW_SE_diag = col - row

        for c in range(self.size):
            if int(self.matrix[c][row]) == 0:
                self.matrix[c][row] = len(self.queens) 
            for r in range(self.size):
                if int(self.matrix[col][r]) == 0:
                    self.matrix[col][r] = len(self.queens) 
                if r+c == NE_SW_diag or r-c == NW_SE_diag:
                    if int(self.matrix[r][c]) == 0:
                        self.matrix[r][c] = len(self.queens)
        self.matrix[col][row] = len(self.queens)


    def remove_last_queen(self):
        #removes last queen and all her associated numbers (coordinates of places she alone endangered).
        self.queens.pop()
        last_queen = self.matrix.max()
        for c in range(self.size):
            for r in range(self.size):
                if self.matrix[c][r] == last_queen:
                    self.matrix[c][r] = 0

    def next_queen(self):
        return len(self.queens) +1

    def solve_all(self, row=0):
        '''
        Finds the first solution in a similar way to solve but cascades() through the (LIFO) stack exhuasting all possabilities. Don't define row as anything but 0.
        
        Most recent called (last in) is the active frame on top of stack
        First the greedy first solution to board size N is found.
        Using the stack additional solutions are searched for using the same first placed queen coordinate, then (N-1) queens then (N-2) all the way down to (N-N) or 0
        At which point the same proccess occurs again just iterated in the first employment of the for loop i in range(self.size)
        '''
        if self.next_queen()>self.size:
            
            locations = ''
            for x in self.queens:
                locations += str(x)
            logging.debug('Queen locations:' + locations)
            
            sol = self.queens[:] #pass by value copying of list (important for storing solution).
            self.solutions_list.append(sol)
            self.solutions += 1 
            
            return #Returns to *
        
        for i in range(self.size):
            if self.safe(row,i):
                self.place(row,i)
                self.solve_all(row+1) # *
                #^If this funciton runs it's course it well return void, and the last queen will be removed.
                self.remove_last_queen() #removes last queen even if solved.
                

    
    def solve(self, row=0, col=0):
        #Recursivley place queens in there first viable position by iterating through rows and columns
        #Until 8 are safely placed.
        #O(n!) - solve in worse case will be called 8 times, then 7, then 6...
        wrap = self.size
        if self.next_queen() > self.size:
            self.show()
            return True
        
        for c in range(self.size):
            #will check next col first
            nqx = (col + c) % wrap #new queen x
            if self.safe(row,nqx):
                self.place(row,nqx)

                if self.solve( (row + 1) % wrap,col) == True:
                    return True

                #else?
                self.remove_last_queen()

        return False

    def show(self):
        board = self.matrix
        b_width = 2*self.size+1
        
        print('\u2554'+('\u2550'*b_width)+'\u2557')
        for row in range(self.size):
            print('\u2551',end='')
            for column in range(self.size):
                if [row,column] in self.queens:
                    print(' \u265b',end='')
                else:
                    print(' \u25a1',end='')
            print(' \u2551')
            
        print('\u255a'+('\u2550'*b_width)+'\u255d')

    def clear(self):
        del self.queens[:]
        self.solutions = 0
        for r in range(self.size):
            for c in range(self.size):
                self.matrix[r][c] = 0

    def animate(self, frame_time = 1, colours = False):
        if( self.solutions<1):
            self.solve_all()
        root = Tk()
        solution_num = 0
        root.title(str(self.size)+' Queens Problem, Solution: '+str(solution_num)+' of '+str(self.solutions))
        GUI_board = Board_canvas(root, self.size)
        GUI_board.canvas.grid(row=0, column=0, padx=25, pady=25)

        #A few seconds of first solution before animation begins.
        root.title(str(self.size)+' Queens Problem.')
        GUI_board.show_placements(self.solutions_list[0], colours)
        GUI_board.canvas.update()

        time.sleep(2)
        
        for queen_coordinates in self.solutions_list:
            solution_num += 1
            root.title(str(self.size)+' Queens Problem, Solution: '+str(solution_num)+' of '+str(self.solutions))
            GUI_board.show_placements(queen_coordinates, colours)
            GUI_board.canvas.update()
            time.sleep(frame_time)
            GUI_board.canvas.delete("queen") #Delete all elements drawn by this iterable

        time.sleep(2)    
        root.destroy()
    

logging.disable(logging.DEBUG)

'''
for N in range(4,13):
    print('Board of size',N)
    standard_chess_board = Board(N)
    standard_chess_board.solve(0,0)
    del standard_chess_board
'''
animated_board = Board()
animated_board.solve_all()
animated_board.animate(0.1,True)

print(animated_board.solutions)
animated_board.clear()
animated_board.solve(0,5)
#animated_board.show()

##        self.solutions = 0
##        self.solutions_list = []
##print('N Queens problem solver.\n')
##print('Full list of solutions:')
##solution = 1
##for coordinates in animated_board.solutions_list:
##    print(animated_board.size,'\u265b\'s solution #'+str(solution),coordinates)
##    solution += 1

