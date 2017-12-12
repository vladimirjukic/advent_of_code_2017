def mazeJumperPartOne(data):
    maze = map(int, data.splitlines())
    currentPosition = 0
    jump = 0
    result = 0
    while (currentPosition < len(maze)):
        jump = maze[currentPosition]
        maze[currentPosition] += 1
        currentPosition += jump
        
        result += 1

    print "Exit in jumps part one: ", result

def mazeJumperPartTwo(data):
    maze = map(int, data.splitlines())
    currentPosition = 0
    jump = 0
    result = 0
    while (currentPosition < len(maze)):
        jump = maze[currentPosition]
        if jump >= 3:
            maze[currentPosition] -= 1
        else: 
            maze[currentPosition] += 1
        currentPosition += jump
        
        result += 1

    print "Exit in jumps part two: ", result

f = open('input.txt', 'r')
content = f.read()
f.close()

mazeJumperPartOne(content)
mazeJumperPartTwo(content)