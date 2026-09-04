n = int(input("Rhombus diagonal size: "))

if n % 2 == 0:
    print("Error. Diagonals have odd length.")
else:
    for (i) in range((n+1)//2):
        spaces = int((n - ((2*i)+1))//2)
        print(" " * spaces + "*" * ((2*i)+1) + " " * spaces)
    for (i) in range((n-1)//2):
        spaces = int(i+1)
        print(" " * spaces + "*" * (n - ((2*i)+2)) + " " * spaces)
        