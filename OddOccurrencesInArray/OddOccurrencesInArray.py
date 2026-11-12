# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Start with zero as the result
    unpaired = 0

    # XOR each element with the current result
    for number in A:
        unpaired = unpaired ^ number

    # The remaining value is the unpaired element
    return unpaired
