import random
#uhuuuuuul
print("Please, type in your chosen height:")
input_height = int(input())
print("PLease, type in your chosen width:")
input_width= int(input())

def create_maze(height, width):  #creates grid and returns object with maze information
    maze = []
    for i in range(height * 2 + 1):
        row = []
        maze.append(row)
        for j in range(width * 2 + 1):
            if i % 2 == 0 :
                maze[i].append("w")
            elif j % 2 == 0:
                maze[i].append("w")
            else:
                maze[i].append("u") #u stands for unvisited cell
    maze_object = {"maze": maze, "height": height, "width": width}

    return maze_object

maze_object = create_maze(input_height, input_width)
maze = maze_object["maze"]
height = maze_object["height"]  #height and width are properties of a theoretical maze whose walls are 2d lines
width = maze_object["width"]
practical_height = height * 2 + 1  #practical_heigth and pratical_width describe the real resulting maze, where the walls themselves occupy a point in space
practical_width = width * 2 + 1

def transform(dimension):  #this function returns the real latitude or longitude given the theoretical ones 
    return dimension * 2 + 1

def print_maze():  #prints maze to the screen
    for i in range(practical_height):
        for j in range(practical_width):
            if i > 0 and j == 0:
                print("\n" + maze[i][j], end = " ")
            else:
                print(maze[i][j], end = " ")

def adjacent(y, x):    # returns a list of all adjacent blocks to the given coordinates that are not already (visited) cells
    adjacent_blocks = []
    if y > 0 and maze[transform(y-1)][transform(x)] != "c":
        adjacent_blocks.append([y - 1, x])

    if x < width - 1 and maze[transform(y)][transform(x+1)] != "c":
        adjacent_blocks.append([y, x + 1])

    if y < height - 1 and maze[transform(y+1)][transform(x)] != "c":
        adjacent_blocks.append([y + 1, x])
   
    if x > 0 and maze[transform(y)][transform(x-1)] != "c":
        adjacent_blocks.append([y, x - 1])

    return adjacent_blocks

def random_adjacent_cell(y,x):  #returns a random adjacent (visited) cell
    adjacent_cells = []
    if y > 0 and maze[transform(y-1)][transform(x)] == "c":
        adjacent_cells.append([y-1,x])

    if x < width - 1 and maze[transform(y)][transform(x+1)] == "c":
        adjacent_cells.append([y,x+1])

    if y < height - 1 and maze[transform(y+1)][transform(x)] == "c":
        adjacent_cells.append([y+1,x])

    if x > 0 and maze[transform(y)][transform(x-1)] == "c":
        adjacent_cells.append([y,x-1])

    random_index = int(random.random() * len(adjacent_cells))

    return adjacent_cells[random_index]



starting_height = int(random.random() * height)
starting_width = int(random.random() * width)  #random starting point for the algorithm


maze[transform(starting_height)][transform(starting_width)] = "c"  #starting point is marked as visited
frontier = [] #a list of all blocks that are currently considered as frontiers (includes all previous frontiers)
frontier = adjacent(starting_height, starting_width)
for i in range(len(frontier)):
    maze[transform(frontier[i][0])][transform(frontier[i][1])] = "f"  #now all the adjacent blocks are marked as frontier




def steps(frontier):  #main function
    
    while frontier:  #steps will run until there are no frontiers left
        rand_frontier = frontier[int(random.random() * len(frontier))]  #pick a random frontier from the list
        maze[transform(rand_frontier[0])][transform(rand_frontier[1])] = "c"  #mark it as visited
        frontier.remove(rand_frontier)  #remove it from the list
        adjacent_cell = random_adjacent_cell(rand_frontier[0],rand_frontier[1])  #grab a random adjacent cell
        tracker = [adjacent_cell[0] - rand_frontier[0], adjacent_cell[1] - rand_frontier[1]]
        if tracker[0] == 0:  #this means the adjacent cell is at the same height as rand_frontier(either to its left or to its right)
            if tracker[1] == 1:  #right
                maze[transform(rand_frontier[0])][transform(rand_frontier[1]) + 1] = "p" 
            else:  #left
                maze[transform(rand_frontier[0])][transform(rand_frontier[1]) - 1] = "p"
        
        if tracker[0] == 1:  #this means the adjacent cell is directly above rand_frontier
            maze[transform(rand_frontier[0]) + 1 ][transform(rand_frontier[1])] = "p"
        
        elif tracker[0] == -1:  #the opposite
            maze[transform(rand_frontier[0]) - 1][transform(rand_frontier[1])] = "p"
        #this will have marked the wall between rand_frontier and the random adjacent cell as p(open passage)

        frontier += adjacent(rand_frontier[0],rand_frontier[1])  #add all adjacent unvisited blocks to the list
        
        while rand_frontier in frontier:   #why in the actual fuck do I need this??
            frontier.remove(rand_frontier)
        
        for i in range(len(frontier)):
            maze[transform(frontier[i][0])][transform(frontier[i][1])] = "f"  #mark every block in frontier as f


steps(frontier)


for i in range(practical_height):  #replace c's and p's with open spaces for better visuals
    for j in range(practical_width):
        if maze[i][j] == "c" or maze[i][j] == "p":
            maze[i][j] = " "

print_maze()





