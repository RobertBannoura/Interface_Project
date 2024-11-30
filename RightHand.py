#!/usr/bin/env python3

import API
import sys


def right_hand_algorithm():
    # Initialize mouse's starting position and orientation
    x, y = 0, 0  # Assume starting at the top-left corner of the maze
    orient = 0  # Facing East (e.g., 0=East, 1=South, 2=West, 3=North)

    try:
        while True:
            API.log(f"Current cell: ({x}, {y})")

            if not API.wallRight():  # If no wall on the right
                API.turnRight()
                orient = API.orientation(orient, 'R')
                API.moveForward()
                x, y = API.updateCoordinates(x, y, orient)
            elif not API.wallFront():  # If no wall in front
                API.moveForward()
                x, y = API.updateCoordinates(x, y, orient)
            elif not API.wallLeft():  # If no wall on the left
                API.turnLeft()
                orient = API.orientation(orient, 'L')
            else:  # All directions blocked
                API.turnRight()
                orient = API.orientation(orient, 'R')
                API.turnRight()
                orient = API.orientation(orient, 'R')
    except API.MouseCrashedError:
        API.log("Mouse crashed into a wall.")
    except KeyboardInterrupt:
        API.log("Algorithm stopped manually.")


# Call the algorithm
right_hand_algorithm()
