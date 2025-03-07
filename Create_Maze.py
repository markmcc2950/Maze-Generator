import random

def set_maze_rows(maze):
    size = len(maze)

    curr_col = 0
    curr_row = 0

    rand_stop = 0
    rand_row_stop = random.randint(0, int(size/4)) + 3

    while (curr_col < size):
        if curr_row < size:
            rand_stop = random.randint(0, size)

            for i in range(curr_row, rand_stop):
                curr_row = i
                maze[curr_row][curr_col] = 0
                if random.randint(0, 4) == 0:
                    rand_col = random.randint(curr_col, size - 1)
                    for i in range(curr_col, rand_col):
                        curr_col = i
                        maze[curr_row][curr_col] = 0

            rand_row = random.randint(0, 2) + 2
            curr_row += rand_row
        else:
            rand_col = random.randint(0, 3) + 2
            curr_row = 0
            curr_col += rand_col

def set_maze_columns(maze):
    size = len(maze)

    curr_col = 0
    curr_row = 0

    rand_stop = 0

    while curr_row < size:
        if curr_row <= 3:
            if curr_col < size:
                rand_stop = random.randint(0, size)

                for i in range(curr_col, rand_stop):
                    curr_col = i
                    maze[curr_row][curr_col] = 0

                rand_col = random.randint(0, 2) + 2
                curr_col += rand_col

            else:
                rand_row = random.randint(0, 3) + 2
                curr_col = 0
                curr_row += rand_row

        else:
            if curr_col < size:
                rand_stop = random.randint(0, size)

                for i in range(curr_col, rand_stop):
                    curr_col = i
                    maze[curr_row][curr_col] = 0

                rand_col = random.randint(0, 2) + 2
                curr_col += rand_col
            else:
                rand_row = random.randint(0, 3) + 2

                curr_col = random.randint(0, size)
                curr_row += rand_row
                if curr_row == size - 2:
                    curr_row = size - 1
    
    rand_stop = random.randint(0, int(size / 2))

    for i in range(size - 1, size - rand_stop, -1):
        maze[size - 1][i] = 0


def set_maze_dimensions(size):
    new_maze = [[1 for _ in range(size)] for _ in range(size)]
    return new_maze

def create_maze(maze, size):
    print(f'Size = {size}')
    new_maze = set_maze_dimensions(size)
    set_maze_columns(new_maze)
    set_maze_rows(new_maze)

    return new_maze