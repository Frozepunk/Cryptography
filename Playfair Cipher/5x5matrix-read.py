rows = 5
columns = 5
matrix = []
print("Enter the entries row-wise -->")
for i in range(rows):          
    row = [] 
    for j in range(columns):     
        element = input(f"Enter element for row {i+1}, column {j+1} --> ")
        row.append(element)
    matrix.append(row)
print("\nThe resulting matrix is \n")
for i in range(rows):
    for j in range(columns):
        print(matrix[i][j], end=" ")
    print()
