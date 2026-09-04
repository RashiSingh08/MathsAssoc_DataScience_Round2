def print_pascal_triangle(n):
    triangle = []

    for i in range(n):
        row = [1] * (i + 1)

        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

        padding = " " * (n - 1 - i)
        row_str = " ".join(map(str, row))
        print(padding + row_str)

n = int(input("Enter the number of rows for Pascal's Triangle: "))
print_pascal_triangle(n)