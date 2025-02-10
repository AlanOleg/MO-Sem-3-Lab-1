from simplex_method import execute_simplex

def main():
    minimize = False
    c = [4, 3, 8]
    A = [[2, 1, 1],
         [1, 3, 0],
         [0, 0.5, 4]]
    b = [8, 4, 3]
    f = 0
    print("Решение:", execute_simplex(c, A, b, f, minimize))


if __name__ == "__main__":
    main()
