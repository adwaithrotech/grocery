# # row = 1

# # while row <= 5:
# #     col = 1
    
# #     while col <= 5:
# #         print(row * col, end='\t')
# #         col += 1
    
# #     print()  # Move to the next line for the next row
# #     row += 1



# row = 1

# while row <= 5:
#     col = 1
    
#     while col <= row:
#         print('*', end=' ')
#         col += 1
    
#     print()  # Move to the next line for the next row
#     row += 1



students = [
    ["Alice", 90, 88, 94],
    ["Bob", 75, 82, 80],
    ["Charlie", 88, 95, 78] ]

for student in students:
    print(f"{student[0]}'s grades: {student[1:]}")

