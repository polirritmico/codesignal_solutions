 
def add_frame(matrix) -> list:
    out_width = len(matrix[0]) + 2
    border = []
    output = []
    for i in range(out_width):
        border.append(False)
    output.append(border)
    for row in matrix:
        framed_row = [False]
        for element in row:
            framed_row.append(element)
        framed_row.append(False)
        output.append(framed_row)
    output.append(border)
    return output


def sum_inner_frame(center_coords, matrix) -> int:
    center_element = 1 if matrix[center_coords[0]][center_coords[1]] else 0
    surrounding_sum = 0
    for row in range(center_coords[0] - 1, center_coords[0] + 2:
        for col in range(center_coords[1] - 1, center_coords[1] + 2):
            surrounding_sum += 1 if matrix[row][col] else 0
    surrounding_sum = surrounding_sum - center_element
    return surrounding_sum


def solution(matrix):
    output = []
    # Add surrounding frame of Falses
    matrix_with_frame = add_frame(matrix)
    # Sum inner 3x3 frame minus current
    last_row = len(matrix_with_frame) - 1
    last_col = len (matrix_with_frame[0]) + 1
    for row in range(1, last_row):
        new_row = []
        for col in range(1, last_col):
            current_coord = (row, col)
            surrounding_sum = sum_inner_frame(current_coord, matrix_with_frame)
            new_row.append(surrounding_sum)
        output.append(new_row)
    return output
