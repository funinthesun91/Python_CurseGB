def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows+1):
        for j in range(1, num_columns+1):
            print("{:6.2f}".format(operation(i, j)), end=" ")
        print()