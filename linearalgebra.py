
# Student: Sude Irem Boylan 241041090

import numpy as np
from sympy import Matrix, pprint

def read_matrix(name):
    rows = int(input(f"Enter number of rows for matrix {name}: "))
    cols = int(input(f"Enter number of columns for matrix {name}: "))
    print(f"Enter the elements of matrix {name} (row by row, separated by spaces):")
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        matrix.append(row)
    return matrix

def read_vector():
    vector = list(map(float, input("Enter vector elements (space separated): ").split()))
    return np.array(vector)

print("Enter data for matrix and vector operations.")
A = read_matrix("A")
B = read_matrix("B")
v = read_vector()
np_A = np.array(A)
np_B = np.array(B)
sym_A = Matrix(A)

def show_menu():
    print("\n*** LINEAR ALGEBRA OPERATIONS MENU ***")
    print("1. Norm of the vector")
    print("2. Determinant of matrix A")
    print("3. Inverse of matrix A")
    print("4. Row echelon form of matrix A")
    print("5. Eigenvalues of matrix A")
    print("6. Eigenvectors of matrix A")
    print("7. Matrix multiplication A x B")
    print("8. Inner product of A and B")
    print("9. Cross product of A and B")
    print("10. Rank of matrix A")
    print("11. Transpose of matrix A")
    print("12. Adjoint of matrix A")
    print("13. Cofactor matrix of A")
    print("14. Minor matrix of A")
    print("15. Matrix addition (A + B)")
    print("16. Matrix subtraction (A - B)")
    print("0. Exit")

while True:
    show_menu()
    choice = input("Select an operation number:")

    if choice == "0":
        print("Exiting program...")
        break

    elif choice == "1":
        print("\n--- Vector Norm ---")
        print("||v|| =", np.linalg.norm(v))

    elif choice == "2":
        print("\n--- Determinant of A ---")
        if len(A) == len(A[0]):
            print("det(A) =", sym_A.det())
        else:
            print("Determinant can only be computed for square matrices.")

    elif choice == "3":
        print("\n--- Inverse of A ---")
        if len(A) == len(A[0]):
            try:
                inv = sym_A.inv()
                pprint(inv)
            except:
                print("Matrix is singular; no inverse exists.")
        else:
            print("Inverse can only be computed for square matrices.")

    elif choice == "4":
        print("\n--- Row Echelon Form ---")
        rref = sym_A.rref()[0]
        pprint(rref)

    elif choice == "5":
        print("\n--- Eigenvalues of A ---")
        if len(A) == len(A[0]):
            pprint(sym_A.eigenvals())
        else:
            print("Eigenvalues can only be computed for square matrices.")

    elif choice == "6":
        print("\n--- Eigenvectors of A ---")
        if len(A) == len(A[0]):
            for val, mult, vects in sym_A.eigenvects():
                print(f"\nEigenvalue: {val}")
                print("Eigenvector(s):")
                for v in vects:
                    pprint(v)
        else:
            print("Eigenvectors can only be computed for square matrices.")

    elif choice == "7":
        print("\n--- Matrix Multiplication A x B ---")
        try:
            result = np.matmul(np_A, np_B)
            print(result)
        except:
            print("Incompatible dimensions; multiplication not possible.")

    elif choice == "8":
        print("\n--- Inner Product of A and B ---")
        try:
            print("Inner product =", np.inner(np_A.flatten(), np_B.flatten()))
        except:
            print("Inner product could not be computed.")

    elif choice == "9":
        print("\n--- Cross Product of A and B ---")
        try:
            if np_A.shape == (3,) and np_B.shape == (3,):
                print("A x B =", np.cross(np_A, np_B))
            elif np_A.shape[1:] == (3,) and np_B.shape[1:] == (3,) and len(np_A) == 1 and len(np_B) == 1:
                print("A x B =", np.cross(np_A[0], np_B[0]))
            else:
                print("Cross product is only defined for 3-dimensional vectors.")
        except:
            print("Cross product could not be computed.")

    elif choice == "10":
        print("\n--- Rank of A ---")
        print("rank(A) =", sym_A.rank())

    elif choice == "11":
        print("\n--- Transpose of A ---")
        transpose = sym_A.transpose()
        pprint(transpose)

    elif choice == "12":
        print("\n--- Adjoint of A ---")
        try:
            adj = sym_A.adjugate()
            pprint(adj)
        except:
            print("Adjoint could not be computed.")

    elif choice == "13":
        print("\n--- Cofactor Matrix of A ---")
        try:
            cof = sym_A.cofactor_matrix()
            pprint(cof)
        except:
            print("Cofactor matrix could not be computed.")

    elif choice == "14":
        print("\n--- Minor Matrix of A ---")
        try:
            minor = sym_A.minor_matrix()
            pprint(minor)
        except:
            print("Minor matrix could not be computed.")

    elif choice == "15":
        print("\n--- Matrix Addition: A + B ---")
        try:
            result = np_A + np_B
            print("A + B =\n", result)
        except:
            print("Addition failed. Dimensions might be incompatible.")

    elif choice == "16":
        print("\n--- Matrix Subtraction: A - B ---")
        try:
            result = np_A - np_B
            print("A - B =\n", result)
        except:
            print("Subtraction failed. Dimensions might be incompatible.")

    else:
        print("Invalid choice. Please enter a number between 0 and 16.")
