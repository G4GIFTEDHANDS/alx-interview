def pascal_triangle(n):
    if n <= 0:
        return []

    pascal = [[1]]  # Initialize Pascal's triangle with the first row containing just 1

    for i in range(1, n):
        row = [1]  # Each row starts with 1
        prev_row = pascal[i - 1]

        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])  # Calculate the next value in the row

        row.append(1)  # Each row ends with 1
        pascal.append(row)

    return pascal

