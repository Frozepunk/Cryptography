rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
matrix = []
print("Enter the entries row-wise:")

for i in range(rows):          
    row = [] 
    for j in range(columns):     
        element = input(f"Enter element for row {i+1}, column {j+1}: ")
        row.append(element)
    matrix.append(row)
print("\nThe resulting matrix is:")
for i in range(rows):
    for j in range(columns):
        print(matrix[i][j], end=" ")
    print()
