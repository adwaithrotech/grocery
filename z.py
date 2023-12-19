row = 1

while row <= 5:
    col = 1
    
    while col <= 5:
        print(row * col, end='\t')
        col += 1
    
    print()  # Move to the next line for the next row
    row += 1