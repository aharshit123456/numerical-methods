import numpy as np

def gauss_elimination(a_matrix, b_matrix):

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
    j = 1 -1
    x = np.zeros(n)
    new_line = "\n"

    # Create our augemented matrix through NumPy's Concatenate feature
    augmented_matrix = np.concatenate((a_matrix,b_matrix), axis=1, dtype=float)
    print(f"The initial augmented matrix is : {new_line}{augmented_matrix}")
    print("Solve for the upper-triangular matrix: ")

    l = 0
    # Applying GE
    while i < n:
        #for p in range(i+1, n):
        #   if abs(augmented_matrix[i,i]) < abs(augmented_matrix[p,i]):
        #        augmented_matrix[[p,i]] = augmented_matrix[[i,p]]
        

        if augmented_matrix[i][i] == 0.0:
            print("Divide by zero error")
            return
        
        for j in range(i +1, n):
            l = l + 1
            print(f"Step {l}")
            scaling_factor = augmented_matrix[j][i] / augmented_matrix[i][i]
            augmented_matrix[j] = augmented_matrix[j] - (scaling_factor*augmented_matrix[i])
            print(augmented_matrix)

        i = i + 1
    
    # Backwards substituion:
    x[m] = augmented_matrix[m][n] / augmented_matrix[m][m]

    for k in range(n-2, -1, -1):
        x[k] = augmented_matrix[k][n]

        for j in range(k+1, n):
            x[k] = x[k] / augmented_matrix[k][k]

    # Displaying Solution
    print(f"The following x-vector matrix solves the above augmented matrix: ")
    for answer in range(n):
        print(f"x{answer} is {x[answer]}")




variable_matrix = np.array([[1,1,-1,-3], [0,1,3,3], [-1,0,2,3], [3,4,2,1]])
constant_matrix = np.array([[1],[3],[6],[4]])

gauss_elimination(variable_matrix, constant_matrix)