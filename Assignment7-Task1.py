def multiplication_table():
    row = int(input("Enter the row number:"))
    col = int(input("Enter the column number:"))
    for i in range(0, row + 1):
        for j in range(0, col + 1):
            if i==0 and j==0:
                print(" ", end="\t")
            elif i==0:
                print(j,end="\t")
            elif j==0:
                print(i,end="\t")
            else:
                print(i*j,end="\t")
        print()
        
multiplication_table()