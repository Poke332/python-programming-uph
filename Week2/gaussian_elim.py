def gaussian_elim(matrix: list):
    n = len(matrix)
    
    # Forward elimination
    for i in range(n):
        # Find pivot row with maximum element in current column
        max_row = i
        for j in range(i + 1, n):
            if abs(matrix[j][i]) > abs(matrix[max_row][i]):
                max_row = j
        
        # Swap rows if necessary
        if max_row != i:
            matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
        
        # Check if pivot element is zero (or very close to zero)
        if abs(matrix[i][i]) < 1e-10:
            return None  # No unique solution or singular matrix
        
        # Eliminate elements below the pivot
        for j in range(i + 1, n):
            factor = matrix[j][i] / matrix[i][i]
            for k in range(i, n + 1):
                matrix[j][k] -= factor * matrix[i][k]
    
    # Back substitution
    solution = [0] * n
    for i in range(n - 1, -1, -1):
        solution[i] = matrix[i][n]  # Right-hand side value
        for j in range(i + 1, n):
            solution[i] -= matrix[i][j] * solution[j]
        solution[i] /= matrix[i][i]
    
    return solution

matrix = list()
is_first_input = True
linear_size = str()

while True:
    if is_first_input:
        linear_size = input("How many variables exist in your linear equation? ")
        try:
            linear_size = int(linear_size)
            is_first_input = False
        except:
            print("Enter valid integer")
            continue
    
    input_count = 0
    equation_vector = []
    print(f"======= Equation {len(matrix)+1}/{linear_size} =======")
    while input_count < linear_size:
        coef = input(f"Enter coeficient number {input_count+1}: ")
        try:
            coef = int(coef)
        except:
            print("Coefficient must be a number")
            continue
            
        equation_vector.append(coef)
        
        while input_count == linear_size-1:
            constant = input("Enter equation constant: ")
            try:
                constant = int(constant)
            except:
                print("Enter valid integer for constant")
                continue
            else:
                equation_vector.append(constant)
                break    
        input_count += 1
    print()
    
    matrix.append(equation_vector)
        
    if len(matrix) == linear_size:
        break

print(gaussian_elim(matrix))