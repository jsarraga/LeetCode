# Approach:
# track movements along both axes
# keep an x counter for horizontal movements, and y counter for vertical movements
# add to counter for one way, subtract if it's the opposite
# if x = 0 and y = 0, then the robot has returned to it's origin



def judgeCircle(moves):
    x = 0
    y = 0

    for move in moves:
        if move == "U":
            y -= 1
        elif move == "D":
            y += 1
        elif move == "L":
            x -= 1
        elif move == "R":
            x += 1
    
    return x == 0 and y ==0