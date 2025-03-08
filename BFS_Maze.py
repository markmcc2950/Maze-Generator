import queue
import Create_Maze as cm
import Render_Maze as rm

def shortest_path_in_maze(maze, start, dest):
    if start == dest:
        return -1  # Edge case: already at destination

    rows, cols = len(maze), len(maze[0])

    # Track visited positions
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    visited[start[0]][start[1]] = True

    # Dictionary to store the parent of each visited node
    parent = {}

    # Allowed movement directions: Down, Up, Left, Right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # BFS queue
    q = queue.Queue()
    q.put((start[0], start[1], 0))  # (row, col, distance)

    while not q.empty():
        q_rows, q_cols, distance = q.get()

        # If we reached the destination, start backtracking
        if (q_rows, q_cols) == dest:
            x, y = dest
            while (x, y) in parent:
                maze[x][y] = 2  # Mark the path in the maze
                x, y = parent[(x, y)]  # Move to the parent
            maze[start[0]][start[1]] = 2  # Ensure the start is marked as part of the path
            return distance  # Return shortest distance
        
        # Explore all 4 possible directions
        for dx, dy in directions:
            new_rows, new_cols = q_rows + dx, q_cols + dy

            # Check if within bounds and is a valid path
            if 0 <= new_rows < rows and 0 <= new_cols < cols and maze[new_rows][new_cols] == 0 and not visited[new_rows][new_cols]:
                visited[new_rows][new_cols] = True
                q.put((new_rows, new_cols, distance + 1))
                parent[(new_rows, new_cols)] = (q_rows, q_cols)  # Store parent for backtracking

    return -1  # If no path is found

# Generic 10x10 maze, 34 moves to complete in shortest path
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
    new_maze = cm.create_maze(maze, 500)
    shortest_path = shortest_path_in_maze(new_maze, (0,0), (len(new_maze) - 1, len(new_maze[0]) - 1))
    # valid_maze = True
    if shortest_path != -1 and shortest_path != (len(new_maze) * 2) - 2:
    # if shortest_path != -1:
        end_pt =  (len(maze) - 1, len(maze[0]) - 1)
        valid_maze = True

print(f'Shortest path in maze = {shortest_path}')

rm.render_maze(new_maze, start_pt, end_pt)
