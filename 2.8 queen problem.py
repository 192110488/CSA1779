print("         192110488--subhash")

N = int(input("Enter the number of queens::"))
board = [[0]*N for _ in range(N)]                                               # here we create a chessboard                                                                               # NxN matrix with all elements set to 0
def attack(i, j):
    for k in range(0,N):                                                        #checking vertically and horizontally
        if board[i][k]=='Q' or board[k][j]=='Q':
            return True
     
    for k in range(0,N):                                                        #checking diagonally
        for l in range(0,N):
            if (k+l==i+j) or (k-l==i-j):
                if board[k][l]=='Q':
                    return True
    return False

def N_queens(n):
    if n==0:
        return True
    for i in range(0,N):
        for j in range(0,N):
            if (not(attack(i,j))) and (board[i][j]!='Q'):
                board[i][j] = 'Q'
                if N_queens(n-1)==True:
                    return True
                board[i][j] = 0

    return False

N_queens(N)
for i in board:
    print (i)
