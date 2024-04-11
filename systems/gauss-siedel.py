import numpy as np

def gauss_siedel(a_matrix, b_matrix):

    if a_matrix.shape[0] != a_matrix.shape[1]:
        print("ERROR: Square matrix not given!")
        return
    
    if b_matrix.shape[1] > 1 or b_matrix.shape[0] != a_matrix.shape[0]:
        print("ERROR: Constant vector incorrectly sized")
        return
    
    # Initialisation of necessary variables
    n = len(b_matrix)
    m = n - 1
    i = 0
    j = i -1
    x = np.ones(n)
    new_line = "\n"
    
    k=0
    while k != 26:
        for i in range(n):
            sum = 0
            for j in range(n):
                if j != i:
                    sum = sum + (a_matrix[i][j]*x[j])

            x[i] = (b_matrix[i] - sum)/a_matrix[i][i]
        
        print(x)
        k = k + 1



    



'''variable_matrix = np.array([[1,1,-1,-3], [0,1,3,3], [-1,0,2,3], [3,4,2,1]])
constant_matrix = np.array([[1],[3],[6],[4]])'''
A = np.array([[2,1,4],[5,7,5],[3,4,5]])
b = np.array([[11],[13],[32]])

gauss_siedel(A, b)