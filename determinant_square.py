'''Runs a couple tests to recursively find the determinant of a sqaure matrix.'''

def get_minor(matrix, col_pos):
    '''Returns a duplicate matrix, less the first row and ith column.'''
    ret = []
    n = len(matrix)
    for i in range(1, n):
        ret_row = []
        for j in range(0, n):
            if j == col_pos:
                continue
            ret_row.append(matrix[i][j])
        ret.append(ret_row)
    return ret


def determinant(matrix):
    '''Recursivley solves determinants to a given square matrix. No safety/sanity checks for now...'''
    if matrix is None:
        return()
    n = len(matrix)
    if n == 1:
        return matrix[0][0]

    det = 0
    
    for i in range(0, n):
        # Recurse on the subs:
        minor = get_minor(matrix, i)
        if i % 2 == 0:
            det += matrix[0][i] * determinant(minor)
        else:
            det -= matrix[0][i] * determinant(minor)
    return det


if __name__ == "__main__":
    test1 = [[1,2,3], [4,5,6], [7,8,9]]
    result1 = determinant(test1)
    assert result1 == 0

    test2 = [[4,6],[3,8]]
    result2 = determinant(test2)
    assert result2 == 14

    test = [[6,7,8], [9,10,11], [12,13,14]]
    result = determinant(test)
    print(result)
    assert result == 0

    test = [[3,4,5,6], [7,8,9,10], [11,12,13,14], [15,16,17,18]]
    result = determinant(test)
    print(result)
    assert result == 0
