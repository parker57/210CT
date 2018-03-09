def rec_lin(lst, x, indx=0):
    if lst[indx] == x:
        return indx
    return rec_lin(lst, x, indx+1)

if __name__ == '__main__':
    letters = ['a','b','c','d','e']
    print(letters)
    user_inp = str(input('Ented the letter you want to find to get it\'s index: '))[0]
    print(rec_lin(letters, user_inp))
