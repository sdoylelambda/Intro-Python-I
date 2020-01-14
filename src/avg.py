# Return the "centered" avg of an array of ints, or mean avg of values,
# except ignoring smallest and largest

# centered_average([1,2,3,4,100]) # return 3

def centered_average(ints):
    # sort the ints
    ints.sort()
    # Slice off 1st and last
    ints = ints[1:-1]
    # sum of remaining values and divide by the length of list
    avg = sum(ints) // len(ints)
    print(avg)
    return avg

centered_average([1,2,3,4,100])


# review - optimize

def centered_average_optimize(ints):
    # Find the max and min value
    smallest = min(ints)
    largest = max(ints)
    ints.remove(smallest)
    ints.remove(largest)
    x = sum(ints) // len(ints)
    print(x)
    return x

centered_average_optimize([1, 2, 3, 4, 100])



def centered_average_optimize_more(ints):
    largest = float('-inf')
    smallest = float('inf')
    total = 0
    for i in ints:
        if i < smallest:
            smallest = i
        if i > largest:
            largest = i
        total  += 1
    x = (total - largest - smallest) // (len(ints) - 2)
    print(x)
    return x

centered_average_optimize_more([1, 2, 3, 4, 100])