import tkinter as tk



def rgb_to_hex(r, g, b):
    r_int = int(r * 255)
    g_int = int(g * 255)
    b_int = int(b * 255)
    return f'#{r_int:02x}{g_int:02x}{b_int:02x}'

def print_maze(maze):
    for i in range(len(maze) - 1):
        print('| ', end='')
        for j in range(len(maze[0]) - 1):
            if maze[i][j] == 1:
                print()

def add_square(canvas, x, y, size=50, color="black", outline=''):
    canvas.create_rectangle(x, y, x + size, y + size, fill=color, outline=outline)

def add_circle(canvas, x1, y1, x2, y2, width=1, fill="black"):
    canvas.create_oval(x1, y1, x2, y2, outline="black", width=width, fill=fill)

def make_square_grid(maze, num_of_squares, canvas):
    global border, maze_array, square_size, square_width

    square_size = square_width / num_of_squares
    
    red = blue = green = 0.5

    for i in range(num_of_squares):
        for j in range(num_of_squares):
            if maze[i][j] == 1:
                red = green = blue = 0.0
            elif maze[i][j] == 0:
                red = green = blue = 1.0
            add_square(canvas, border + (square_size * j), border + (square_size * i), size=square_size, color=rgb_to_hex(red, green, blue))


def render_maze(maze, start, end):
    global border, canvas, grid_size, maze_array, pt_start, pt_end, square_width, window_size

    root = tk.Tk()
    root.title("My Maze")

    # Set up the window to display to the user
    root.geometry(f"{window_size}x{window_size}")
    root.resizable(False, False)

    # Create the canvas
    canvas = tk.Canvas(root, width=window_size, height=window_size)
    canvas.pack(fill="both", expand=True)
    canvas_bg = 0.1
    add_square(canvas, 0, 0, size=window_size, color=rgb_to_hex(canvas_bg, canvas_bg, canvas_bg))

    # Set up the canvas to display our maze
    maze_array = maze
    maze_array[3][1] == 2
    grid_size = len(maze)
    pt_start = start
    pt_end = end
    # add_circle(canvas, x=(border + start[0]), y=(border + start[1]), size=square_width, color="green")
    

    make_square_grid(maze, grid_size, canvas)

    add_circle(canvas, border, border, border + square_size, border + square_size, fill="green")
    add_circle(canvas, window_size - border, window_size - border, window_size - border - square_size, window_size - border - square_size, fill="red")

    root.mainloop()

#-----------------------------Global variables-----------------------------
window_size = 800
border = (window_size - (window_size * 0.8)) / 2
square_width = window_size * 0.8
maze_array = [[0 for _ in range(2)] for _ in range(2)]
pt_start = (0, 0)
pt_end = (1, 1)
grid_size = 6
square_size = square_width / grid_size

canvas = None