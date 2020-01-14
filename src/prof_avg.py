# Return the "centered" average of an array of ints, which we'll say is the mean
# average of the values, except ignoring the largest and smallest values in the array.

# centered_average([1, 2, 3, 4, 100]) → 3
# centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
# centered_average([-10, -4, -2, -4, -2, 0]) → -3

[1, 5, 5, 8, 7] // 5

[-4, -2, -4, -2]



def centered_avg(ints):
    ints_copy = ints.copy()
    # Sort the ints
    ints_copy.sort()
    # Slice off the first and last value
    ints_copy = ints_copy[1:-1]
    # Sum the remaining values and divide by the length of the list
    return sum(ints_copy) // len(ints_copy)


def centered_avg_semi_optimized(ints):
    # Find the max and min value
    smallest = min(ints)
    largest = max(ints)
    # remove max and min
    ints.remove(smallest)
    ints.remove(largest)
    # Find sum of new array // length of new array
    return sum(ints) // len(ints)



def centered_avg_optimized(ints):
    largest = ints[0]
    smallest = ints[0]
    total = 0
    # for integer in ints
    for i in ints:
        # If the integer is smaller than min, set min to the int
        if i < smallest:
            smallest = i
        # If the integer is larger than max, set max to the int
        if i > largest:
            largest = i
        # Keep a running total of the sum
        total += i
    # Return the sum minus largest and smallest divided by the length - 2
    return (total - largest - smallest) // (len(ints) - 2)

#
# return (sum(nums) - min(nums) -  max(nums)) // (len(nums) - 2)
#


centered_avg_optimized([1, 2, 3, 4, 100])
centered_avg_optimized([1, 1, 5, 5, 10, 8, 7])
centered_avg_optimized([-10, -4, -2, -4, -2, 0])






def mult_2(n):
    n *= 2
    return n



n = 5
mult_2(n)
print(n)
