import re
from copy import copy
#Insert pg_words into list of doubly lists, making alphabetical comparisons
file = open('tolkein.txt','r')
paragraph = file.read()
file.close()

paragraph = re.sub('[^a-z \n]','',paragraph.lower()) #Take off punctuation, replace all that is not a lowercase letter or space

pg_words = paragraph.split() #pg_words = paragraph_words

pg_words = list(set(pg_words))

class Word():
    def __init__(self, text, last = None, after = None):
        self.text = text
        self.last = last
        self.next = after
        
    def __lt__(self,other):
        return self.text < other.text
    def __gt__(self,other):
        return self.text > other.text
     
    def show(self):
        last = None
        after = None
        if self.last:
            last = self.last.text
        if self.next:
            after = self.next.text
        print(last,'-',self.text,'-',after)
        

class DoublyList():
    def __init__ (self, word = None):
        self.size = 0
        self.first_word = word
        self.last_word = word
        if word:
            self.size = 1

    def append(self, word):
        word = Word(word)
        if self.size == 0:
            self.first_word = word
            self.last_word = word
            self.size += 1
        else:
            word.last = self.last_word
            word.next = None
            self.last_word.next = word # THINK ABOUT THIS.
            self.last_word = word
            self.size += 1

    def pop(self):
        #may run into difficulties with circular lists
        if self.size > 1:
            old_last = self.last_word
            new_last = self.last_word.last
            new_last.next = None
            
            self.last_word = old_last.last
            old_last.last = None #sever connection to rest of words.
            
            self.size -= 1
            
            return old_last

        elif self.size == 0:
            self.first_word = None
            self.last_word = None
            self.size -= 1
        
        else:
            print('Double-Linked list is empty.')

    def show(self):
        if self.size > 1:
            cur_word = self.first_word
            #print(self.size)
            print(cur_word.text,'<->',end=' ')
            while cur_word.next:
                print(cur_word.next.text,end=' ')
                cur_word = cur_word.next
                if cur_word.next:
                    print('<->',end=' ')
        else:
            print(self.first_word.text, end='')
        print()

    def __getitem__ (self, key):
        if key > self.size or key < 0:
            raise IndexError
        #key -= 1 #indexing from 0
        cur_word = self.first_word
        if key == 0:
            #cur_word.show()
            return cur_word
        else:
            for i in range(key):
                cur_word = cur_word.next
            #cur_word.show()
            return cur_word

    def remove(self, key):
        #print('removing',key,'size:',self.size)
        if key > self.size or key < 0:
            raise IndexError
        cur_word = self.first_word
        cur_word = cur_word.next
        if key == 0:
            cur_word.prev = None
            self.first_word = cur_word
            self.size -= 1
        elif key == self.size-1:
            self.last_word = self.last_word.last
            self.last_word.next = None
            self.size -= 1
        else:
            for i in range(key-1):
                cur_word = cur_word.next
            cur_word.last.next =  cur_word.next
            #del cur_word
            self.size -= 1

    def insert(self, key, new_word): #delete and insert together should be sufficient for sorting.
        #insert befor index
        if key > self.size or key < 0:
            raise IndexError
        if key == 0:
            #self.first_word.prev = Word(new_word, none, self.first_word)
            new_word = Word(new_word, None, self.first_word)
            self.first_word = new_word
            self.first_word.next.last = self.first_word

            self.size += 1
        else: #Growing list?
            cur_word = self.first_word
            for i in range(key):
                cur_word = cur_word.next
            insert_word = Word(new_word, cur_word.last, cur_word)
            cur_word.last.next = insert_word
            cur_word.last = insert_word

            self.size += 1

    def swap(self, key):
        #Key is index of first element, will swap with one in front.
        #Can only implement from penultimate node at the latest.
        if key-1 > self.size or key < 0:
            raise IndexError
        cur_word = self.first_word
        for i in range(key):
            cur_word = cur_word.next
            
        inserted_word = cur_word.next.text

        self.insert(key, inserted_word) 
        self.remove(key+2)
        if key != self.size - 2:
            cur_word.next.last = cur_word

    def sinksort(self):
        swap_limit = self.size - 2
        for h in range(swap_limit, -1, -1):
            for i in range(h,-1,-1):
                if self[i+1] < self[i]:
                    self.swap(i)

    def quicksort(self):
        for i in range(self.size-1):
            for i in range(self.size-1):
                if self[i] > self[i+1]:
                    self.swap(i)

    def verbose(self):
        cursor = self.first_word
        print(cursor.last, cursor.text, cursor.next.text)
        cursor = cursor.next
        while cursor.next != None:
            print(cursor.last.text, cursor.text, cursor.next.text)
            cursor = cursor.next
        print(cursor.last.text, cursor.text, cursor.next)
    

def double_list_list(word_list):
    #creates a list of doubly linked list, each item being a doubly linked list of words (all of the same length).
    double_list_list = []
    
    for word in word_list:
        added = False
        for l in double_list_list:
            if len(l[0].text) == len(word):
                l.append(word)
                added = True
        if not added:
            double_list_list.append(DoublyList(Word(word)))

    return double_list_list
        

if __name__ == '__main__':

    dub_list = double_list_list(pg_words)
    dub_list = sorted(dub_list, key = lambda d_ll : len(d_ll[0].text))
    for word_list in dub_list:
        word_list.quicksort()
        word_list.show()

    
