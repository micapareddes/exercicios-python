def is_matrix_magic_square(sm):
    size = len(sm)
    main_diagonal_sum = 0

    # Calculate sum of the main diagonal
    for i in range(size):
        main_diagonal_sum += sm[i][i]
    
    # Validate the sum of each row
    for i in range(size):
        current_row_sum = 0
        for j in range(size):
            current_row_sum += sm[i][j]
        if current_row_sum != main_diagonal_sum:
            return False
        
    # Validate the sum of each column
    for i in range(size):
        current_column_sum = 0
        for j in range(size):
            current_column_sum += sm[j][i]
        if current_column_sum != main_diagonal_sum:
            return False
    
    # Validate the sum of the secondary diagonal
    secondary_diagonal_sum = 0

    for i in range(size):
        secondary_diagonal_sum += sm[i][(size - 1) - i]

    if secondary_diagonal_sum != main_diagonal_sum:
        return False
    
    return True

# Testing code
mm = [
    [8, 0, 7],
    [4, 5, 6],
    [3, 10, 2]
]

print(is_matrix_magic_square(mm))