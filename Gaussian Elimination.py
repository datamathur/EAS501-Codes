def rref(A):
# RREF  This function performs Gaussian Elimination using pivoting to convert a matrix A into I.
# 
#   Input:
#       A - A m*n dimensional matrix.

#   Output
#       R - An indentity matrix of dimension m*n.
 
#   Initializing the indexing variables.
    R = A
    [i,j] = [0, 0]
    [m, n] = [len(A), len(A[0])]

    while i<m and j<n:
#       PIVOTING
#       Finding the largest value in column j below row i.
        kmax = R[i][j]
        for k in range(i,m):
            if R[k][j]>kmax:
                kmax = R[k][j]
                knew = k
            else:
                continue
#       Swapping row k and row i. 
        for a in range(0,n):
            R[i][a], R[k][a] = R[k][a], R[i][a]

#       RREF MAIN STEPS
        if abs(R[i][j]) > pow(10,-16):
#           Normalizing row i.
            a = R[i][j]
            for k in range(j,n):
                R[i][k] /= a 
#           Eliminating values in column j other than row i.
            for k in range(0,m):
                a = R[k][j]
                if(k==i):
                    continue
                else:
                    for l in range(j,n):
                        R[k][l] -= a*R[i][l]
#       Preparing Next Steps
            i += 1
            j += 1
        else:
            j += 1
    
    return R

if "__main__":
    A = [[2, 1, -1], [3, -1, 2], [-2, 1, 2]]
    R = rref(A)
    print(R)


