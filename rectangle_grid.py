testcases = int(input("How many testcases would you like to perform? "))
print("")

while testcases > 0:
    n = int(input("Enter number of rectangles: "))
    print("")
    x_cor = []
    y_cor = []

    for i in range(n * 4-1):
        x, y = map(int, input("Enter coordinates, separated with a space: ").split())
        print(x, y)
        x_cor.append(x)
        y_cor.append(y)

    j = 0
    check1 = None
    check2 = None
    while j < len(x_cor):
        comp1 = x_cor.count(x_cor[j])
        if comp1 % 2 != 0 and x_cor[j] != check1:
            check1 = x_cor[j]

        comp2 = y_cor.count(y_cor[j])
        if comp2 % 2 != 0 and y_cor[j] != check2:
            check2 = y_cor[j]

        j += 1
    print("The coordinate solution is (",check1,",",check2,")")

    testcases -= 1

