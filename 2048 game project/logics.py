import random

def start_game():
    mat = []
    for i in range(4):
        mat.append([0] * 4)
    return mat

def add_new_2(mat):
    r = random.randint(0, 3)
    c = random.randint(0, 3)
    while(mat[r][c] != 0):
        r = random.randint(0, 3)
        c = random.randint(0, 3)
    mat[r][c] = 2

def get_current_state(mat):
    for row in range(4):
        for col in range (4):
            if(mat[row][col] == 2048):
                return "WON"
            
    for row in range(4):
        for col in range (4):
            if(mat[row][col] == 0):
                return "GAME NOT OVER"

    for row in range(3):
        for col in range(3):
            if(mat[row][col] == mat[row+1][col] or mat[row][col] == mat[row][col+1]):
                return "GAME NOT OVER"

        #Last row
        for col in range(3):
            if(mat[3][col] == mat[3][col+1]):
                return "GAME NOT OVER"

        #Last Column
        for row in range(3):
            if(mat[row][3] == mat[row + 1][3]):
                return "GAME NOT OVER"
    return "LOST"

def compress(mat):
    flag = False
    new_mat = []
    for row in range(4):
        new_mat.append([0]*4)
        
    for row in range(4):
        idx = 0
        for col in range(4):
            if (mat[row][col] != 0):
                new_mat[row][idx] = mat[row][col]
                if col != idx:
                    flag = True
                idx += 1
    return new_mat, flag

def reverse(mat):
    new_mat = []
    for row in range(4):
        new_mat.append([])
        for col in range(4):
            new_mat[row].append(mat[row][4-col-1])
    return new_mat

def transpose(mat):
    new_mat = []
    for row in range(4):
        new_mat.append([])
        for col in range(4):
            new_mat[row].append(mat[col][row])
    return new_mat

def merge(mat):
    flag = False
    for row in range(4):
        for col in range(3):
            if (mat[row][col] == mat[row][col +1] and mat[row][col] != 0):
                mat[row][col] = mat[row][col] * 2
                mat[row][col + 1] = 0
                flag = True
    return mat, flag

def move_up(mat):
    transposed_mat = transpose(mat)
    new_mat, flag1 = compress(transposed_mat)
    new_mat, flag2 = merge(new_mat)
    flag = flag1 or flag2
    new_mat, temp = compress(new_mat)
    final_mat = transpose(new_mat)
    return final_mat, flag


def move_down(mat):
    transposed_mat = transpose(mat)
    reversed_mat = reverse(transposed_mat)
    new_mat, flag1 = compress(reversed_mat)
    new_mat, flag2 = merge(new_mat)
    flag = flag1 or flag2
    new_mat, temp = compress(new_mat)
    final_reversed_mat = reverse(new_mat)
    final_mat = transpose(final_reversed_mat)
    return final_mat, flag

def move_right(mat):
    reversed_mat = reverse(mat)
    new_mat, flag1 = compress(reversed_mat)
    new_mat, flag2 = merge(new_mat)
    flag = flag1 or flag2
    new_mat, temp = compress(new_mat)
    final_mat = reverse(new_mat)
    return final_mat, flag

def move_left(mat):
    new_mat, flag1 = compress(mat)
    new_mat,flag2 = merge(new_mat)
    flag = flag1 or flag2
    new_mat,temp = compress(new_mat)
    return new_mat, flag

