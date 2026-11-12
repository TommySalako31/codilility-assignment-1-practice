# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    # Calculate the distance the frog needs to travel
    distance = Y - X

    # Calculate the number of complete jumps
    jumps = distance // D

    # Add one jump if there is remaining distance
    if distance % D != 0:
        jumps += 1

    # Return the minimum number of jumps
    return jumps

