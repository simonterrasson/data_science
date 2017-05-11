import math

A = [[1, 2, 3], # A has 2 rows and 3 columns
     [4, 5, 6]]
B = [[1, 2], # B has 3 rows and 2 columns
     [3, 4],
     [5, 6]]

def shape(M):
    cnt_rows = len(M)
    cnt_cols = len(M[0]) if M else 0
    return cnt_rows,cnt_cols

def get_row(M,i):
    return M[i]

def get_column(M,j):
    return [M_i[j] for M_i in M]

def make_matrix(cnt_rows,cnt_cols,entry_fn):
    # Makes a specific cnt_rowsXcnt_cols matrix filled with entry_fn results
    # Results are calculated : entry_fn(i,j)
    return [[entry_fn(i,j)
                for j in range(cnt_cols)]
                    for i in range(cnt_rows)]

def is_diagonal(i,j):
    return 1 if i == j else 0

diag_matrix = make_matrix(5,5,is_diagonal)
print(diag_matrix)
