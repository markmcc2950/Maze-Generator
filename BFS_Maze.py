import queue
import Create_Maze as cm
import Render_Maze as rm

def shortest_path_in_maze(maze, start, dest):
    if start == dest:
        return -1
    
    rows = len(maze)
    cols = len(maze[0])

    # Create a 2D Array of size of our maze, initialized all to unvisited. Set starting point as visited
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    visited[start[0]][start[1]] = True

    # Stores the directions we are allowed to move (down, up, left, right)
    directions = [
        [-1, 0],
        [1, 0],
        [0, -1],
        [0, 1]
    ]

    q = queue.Queue()
    q.put((start[0], start[1], 0))

    while not q.empty():
        q_val = q.get()

        q_rows = q_val[0]
        q_cols = q_val[1]
        distance = q_val[2]

        if q_rows == dest[0] and q_cols == dest[1]:
            return distance
        
        for direction in directions:
            new_rows = q_rows + direction[0]
            new_cols = q_cols + direction[1]

            if new_rows >= 0 and new_rows < rows and new_cols >= 0 and new_cols < cols and maze[new_rows][new_cols] == 0 and not visited[new_rows][new_cols]:
                visited[new_rows][new_cols] = True

                q.put((new_rows, new_cols, distance + 1))

    return -1


maze = [
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 0]
]

# maze = cm.create_maze(maze, 10)

# print(f'Maze length = {len(maze)}')

# start_pt = (0, 0)
# end_pt = (len(maze) - 1, len(maze[0]) - 1)

# print(f'Maze rows: {len(maze)}\nMaze columns: {len(maze[0])}')

# shortest_path = shortest_path_in_maze(maze, start_pt, end_pt)
# print(shortest_path)
# print('Shortest path in maze =', shortest_path if shortest_path >= 0 else 'INVALID MAZE')

# rm.render_maze(maze, start_pt, end_pt)

valid_maze = False
start_pt = (0, 0)
end_pt = (1, 1)

while not valid_maze:
    new_maze = cm.create_maze(maze, 50)
    shortest_path = shortest_path_in_maze(new_maze, (0,0), (len(new_maze) - 1, len(new_maze[0]) - 1))
    if shortest_path != -1:
        end_pt =  (len(maze) - 1, len(maze[0]) - 1)
        valid_maze = True

print(f'Shortest path in maze = {shortest_path}')

rm.render_maze(new_maze, start_pt, end_pt)
