n = int(input("Number of rows in the triangle in range 1-9: "))

for i in range(n + 1):
    spaces = (n - i) * ' '
    numbers = (n + i) * '*'
    print(spaces + numbers)
