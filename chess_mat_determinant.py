import math
import numpy
#work on this program


def det(new_matrix,matrix,n,total): #using recursion to find determinant of 3x3 matrix
    #this evaluates location of piece
    mat_list = []
    if len(new_matrix) == 2:
        determinant = (new_matrix[0][0] * new_matrix[1][1]) - (new_matrix[0][1] * new_matrix[1][0])
        return determinant
    elif len(new_matrix) == 3:
        mat_list = []
        n = len(new_matrix) - 1
        print("n is",n)
        for i in range(n+1):
            print("loop1")
            new_matrix = []
            for x in range(1,n+1):
                print("loop2")
                new_matrix.append([])
                for y in range(0,n+1):
                    print("loop 3")
                    if y != i:
                        new_matrix[x-1].append(matrix[x][y])
                        
            print(new_matrix)
            mat_list.append(new_matrix)
    elif len(new_matrix) == 4:
        mat_list = []
        print("herdee")
        n = len(new_matrix) - 1
        print("n is",n)
        for i in range(n+1):
            print("loop1")
            new_matrix = []
            for x in range(1,n+1):
                print("loop2")
                new_matrix.append([])
                for y in range(0,n+1):
                    print("loop 3")
                    for z in range(0,n+1):
                        print("loop 4")
                        if z != i:
                            new_matrix[x-1].append(matrix[y][z])
    total_det = 0
        
    if len(matrix) % 2 == 0:
        for z in range(len(matrix)):
            total_det += ((-1)**(z+1)) * matrix[0][z] * (det(mat_list[z],matrix,n,total_det))

            print("total so far is",total_det)
    else:
        for z in range(len(matrix)):
            total_det += ((-1)**(z)) * matrix[0][z] * (det(mat_list[z],matrix,n,total_det))
            print("total so far is",total_det)
            return total_det
                
    
    return total_det
def mat_for_knights():
    pass
def mat_for_rooks():
    pass
def mat_for_queens():
    pass

def mat_for_bishops(x,y,table):
    #3 by 3 for bishops and non pawns
    for i in range(3):
        mat.append([])
        for j in range(3):
            new_i = i - 1
            new_j = j - 1
            print("new i {} new j {}".format(new_i, new_j))
            print("adding {} {}".format(x + new_i,y + new_j))
            try:
                if (x + new_i) >= 0 and (y + new_j) >= 0:
                    mat[i].append(table[x + new_i][y + new_j])
                else:
                    print("less than zero")
            except IndexError:
                print("error")
                continue
    print(mat)
    for z in range(len(mat)):
        try:
            if mat[z] == []:
                mat.pop(z)
        except IndexError:
            continue
    new_matrix = mat
    total = 0
    print(det(new_matrix,mat,len(new_matrix)-1,total))
     
#for pawns - ONLY BLACK PAWNS
def mat_for_pawns(x,y,table):
    print("here")
    mat = []
    for i in range(3):
        mat.append([])
        for j in range(3):
            new_i = i 
            new_j = j 
            print("new i {} new j {}".format(new_i, new_j))
            print("adding {} {}".format(x + new_i,y + new_j))
            try:
                if (x + new_i) >= 0 and (y + new_j) >= 0:
                    mat[i].append(table[x + new_i][y + new_j])
                else:
                    print("less than zero")
            except IndexError:
                print("error")
                continue
    print(mat)
    for z in range(len(mat)):
        try:
            if mat[z] == []:
                mat.pop(z)
        except IndexError:
            continue
    new_matrix = mat
    total = 0
    return det(new_matrix,mat,len(new_matrix)-1,total)
