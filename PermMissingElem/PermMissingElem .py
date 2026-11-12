# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Find the number of elements in the array
    N = len(A)

    # Calculate the expected sum from 1 to N + 1
    expected_sum = (N + 1) * (N + 2) // 2

    # Calculate the actual sum of the array
    actual_sum = sum(A)

    # The difference is the missing element
    missing = expected_sum - actual_sum

    return missing

