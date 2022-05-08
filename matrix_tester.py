from numpy import matrix
import Matrix as mat



def matrix_printer(given: mat.Matrix):
    print("[")
    for i in range(given.rows):
        print("[", end="")
        for j in range(given.columns):
            print(f'{int(given.data[i][j])}',end="")
            if(j != given.columns - 1):
                print(",",end="")
            
        print("]\n", end="")
    print("]")


def main():
    m1 = mat.Matrix(3,3)
    m1.update_column([5,1,7],1)
    m1.update_column([8,0,9],2)
    m1.update_column([4,5,3],3)
    matrix_printer(m1)
    matrix_printer(mat.matrix_multiplication(m1,m1))
    return 0

if __name__ == "__main__":
    main()