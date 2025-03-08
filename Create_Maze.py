import random

def remove_some_maze(maze):
    size = len(maze)
    for i in range(2,size):
        rand_val = random.randint(0, int(size / 5))
        if rand_val == 0:
            random_side = random.randint(0, size);
            inc_val = 0
            min_val = 0
            max_val = size
            if random_side <= int(size / 2):
                min_val = 0
                max_val = random.randint(0, size)
                inc_val = 1
            else:
                min_val = size
                max_val = random.randint(0, size)
                inc_val = 1
            for j in range(min_val, random.randint(0, max_val), inc_val):
                maze[i][j] = 1


def set_maze_columns(maze):
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

                rand_chance = random.randint(0, len(maze))
                if rand_chance == 0:
                    rand_col = random.randint(curr_col, size - 1)
                    temp_col = curr_col
                    for i in range(temp_col, rand_col):
                        temp_col = i
                        if curr_row - 1 > 0 and curr_row + 1 < len(maze) and maze[curr_row - 1][temp_col] == 1 and maze[curr_row + 1][temp_col] == 1 :
                            maze[curr_row][temp_col] = 0

            rand_row = random.randint(0, 2) + 2
            curr_row += rand_row
        else:
            rand_col = random.randint(0, 3) + 2
            curr_row = 0
            curr_col += rand_col

def set_maze_rows(maze):
    size = len(maze)

    curr_col = 0
    curr_row = 0

    rand_stop = 0

    while curr_row < size:
        if curr_row <= int(len(maze) / 4):
            if curr_col < size:
                rand_stop = random.randint(0, size)

                for i in range(curr_col, rand_stop):
                    curr_col = i
                    maze[curr_row][curr_col] = 0

                    if i - 1 > 0 and i + 1 < len(maze) and maze[curr_row][i - 1] == 1 and maze[curr_row][i + 1] == 1:
                        rand_chance = random.randint(0, len(maze[0]))
                        if rand_chance == 0:
                            temp_rand = random.randint(curr_row, size)
                            temp_row = curr_row
                            
                            for j in range(temp_row, temp_rand):
                                temp_row = j
                                maze[temp_row][curr_col] = 0

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

                    if i - 1 > 0 and i + 1 < len(maze) and maze[curr_row][i - 1] == 1 and maze[curr_row][i + 1] == 1:
                        rand_chance = random.randint(0, len(maze[0]))
                        if rand_chance == 0:
                            temp_rand = random.randint(curr_row, size)
                            temp_row = curr_row
                            
                            for j in range(temp_row, temp_rand):
                                temp_row = j
                                maze[temp_row][curr_col] = 0

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

        rand_chance = random.randint(0, int(len(maze) / 4))
        if rand_chance == 0 and curr_row < len(maze):
            temp_rand = random.randint(int((size - 1) / 2), curr_row)
            temp_row = curr_row
            for i in range(temp_rand, temp_row):
                temp_row = i
                if curr_col - 1 > 0 and curr_col + 1 < len(maze) and maze[temp_row][curr_col] == 1 and maze[temp_row][curr_col] == 1 :
                    maze[temp_row][curr_col] = 0


def set_maze_dimensions(size):
    new_maze = [[1 for _ in range(size)] for _ in range(size)]
    return new_maze

def create_maze(maze, size):
    # print(f'Size = {size}')
    new_maze = set_maze_dimensions(size)
    set_maze_rows(new_maze)
    set_maze_columns(new_maze)
    remove_some_maze(new_maze)

    return new_maze