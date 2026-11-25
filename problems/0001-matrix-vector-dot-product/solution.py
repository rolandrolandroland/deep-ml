def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    # Return a list where each element is the dot product of a row of 'a' with 'b'.
    # If the number of columns in 'a' does not match the length of 'b', return -1.
    if len(a[0]) != len(b):
        out = -1
    else:
        out = []
        for a_row in a:
            val = sum(x*y for x,y in zip(a_row, b))
            out.append(val)
    return out