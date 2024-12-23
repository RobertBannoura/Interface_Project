import sys

'''
orients :
    0- North
    1- East
    2- South
    3- West
'''

def orientation(orient, turning):
    if turning == 'L':
        orient = (orient - 1) % 4  # Turn left: decrease orientation, wrap at 0
    elif turning == 'R':
        orient = (orient + 1) % 4  # Turn right: increase orientation, wrap at 3
    elif turning == 'B':
        orient = (orient + 2) % 4  # Turn backward: add 2, wrap at 3
    return orient

def updateCoordinates(x, y, orient):
    if orient == 0:  # North (y increases upwards)
        y += 1
    elif orient == 1:  # East (x increases to the right)
        x += 1
    elif orient == 2:  # South (y decreases downwards)
        y -= 1
    elif orient == 3:  # West (x decreases to the left)
        x -= 1

    return x, y



class MouseCrashedError(Exception):
    pass

def command(args, return_type=None):
    line = " ".join([str(x) for x in args]) + "\n"
    sys.stdout.write(line)
    sys.stdout.flush()
    if return_type:
        response = sys.stdin.readline().strip()
        if return_type == bool:
            return response == "true"
        return return_type(response)

def mazeWidth():
    return command(args=["mazeWidth"], return_type=int)

def mazeHeight():
    return command(args=["mazeHeight"], return_type=int)

def wallFront():
    return command(args=["wallFront"], return_type=bool)

def wallRight():
    return command(args=["wallRight"], return_type=bool)

def wallLeft():
    return command(args=["wallLeft"], return_type=bool)

def moveForward():
    response = command(args=["moveForward"], return_type=str)

    if response == "crash":
        #log(str(cells[y][x]))
        raise MouseCrashedError()

def turnRight():
    command(args=["turnRight"], return_type=str)

def turnLeft():
    command(args=["turnLeft"], return_type=str)

def setWall(x, y, direction):
    command(args=["setWall", x, y, direction])

def clearWall(x, y, direction):
    command(args=["clearWall", x, y, direction])

def setColor(x, y, color):
    command(args=["setColor", x, y, color])

def clearColor(x, y):
    command(args=["clearColor", x, y])

def clearAllColor():
    command(args=["clearAllColor"])

def setText(x, y, text):
    command(args=["setText", x, y, text])

def clearText(x, y):
    command(args=["clearText", x, y])

def clearAllText():
    command(args=["clearAllText"])

def wasReset():
    return command(args=["wasReset"], return_type=bool)

def ackReset():
    command(args=["ackReset"], return_type=str)

def log(string):
    sys.stderr.write("{}\n".format(string))
