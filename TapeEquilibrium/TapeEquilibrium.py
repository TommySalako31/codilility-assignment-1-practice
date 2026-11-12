# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Calculate the total sum of the array
    total_sum = sum(A)

    # Start with an empty left side
    left_sum = 0
    min_difference = float('inf')

    # Try every valid splitting position
    for i in range(len(A) - 1):
        left_sum += A[i]
        right_sum = total_sum - left_sum

        # Calculate the absolute difference
        difference = abs(left_sum - right_sum)

        # Keep track of the smallest difference
        min_difference = min(min_difference, difference)

    return min_difference