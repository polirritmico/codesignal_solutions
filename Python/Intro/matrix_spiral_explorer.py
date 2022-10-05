from numpy import full

def get_new_direction():
    while True:
        yield "→"
        yield "↓"
        yield "←"
        yield "↑"


def next_coord(current_pos, direction):
    if direction == "→":
        vector = (0, 1)
    elif direction == "↓":
        vector = (1, 0)
    elif direction == "←":
        vector = (0, -1)
    elif direction == "↑":
        vector = (-1, 0)
    else:
        raise Exception("Bad direction")

    return (current_pos[0] + vector[0], current_pos[1] + vector[1])


def check_valid_coord(check_position, matrix_map):
    rows = len(matrix_map)
    cols = len(matrix_map[0])

    if check_position[0] < 0 or check_position[0] >= rows:
        return False
    elif check_position[1] < 0 or check_position[1] >= cols:
        return False

    return matrix_map[check_position[0]][check_position[1]]


def matrix_spiral_explorer(matrix):
    output = []
    rows = len(matrix)
    if rows == 0:
        return output
    cols = len(matrix[0])
    elements = rows * cols

    matrix_map = full((rows, cols), True)

    direction = get_new_direction()
    current_direction = next(direction)
    current_pos = [0, 0]
    for _ in range(0, elements):
        output.append(matrix[current_pos[0]][current_pos[1]])
        matrix_map[current_pos[0]][current_pos[1]] = False

        next_pos = next_coord(current_pos, current_direction)
        if not check_valid_coord(next_pos, matrix_map):
            current_direction = next(direction)
            next_pos = next_coord(current_pos, current_direction)
        current_pos = next_pos

    return output

