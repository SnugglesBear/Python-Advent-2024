# Plan:
# Get an array of arrays
# find the length of each one
# create a test (true/false) for all increasing or all decreasing
# create a test (true/false) for difference of 0 < x < 4
# if an index passes both tests, add to running sum

def read_file_as_array_of_arrays(file_path):
    with open(file_path, 'r') as file:
        return [
            list(map(int, line.strip().split()))
            for line in file if line.strip()
        ]
    
def test_increase_or_decrease(arr):
    return all(arr[i] < arr[i+1] for i in range(len(arr)-1)) or \
           all(arr[i] > arr[i+1] for i in range(len(arr)-1))
    

def test_required_range(arr):
    return all(0 < abs(arr[i] - arr[i+1]) < 4 for i in range(len(arr)-1))
    
def is_safe(arr):
    return test_increase_or_decrease(arr) and test_required_range(arr)

def main():
    input = read_file_as_array_of_arrays("Python-Advent-2024/Day 2/input.txt")
    print(len(input))

    total = 0

    for x in input:
        if is_safe(x):
            total += 1
        else:
            # Try removing one element at a time
            for i in range(len(x)):
                new_arr = x[:i] + x[i+1:]
                if is_safe(new_arr):
                    total += 1
                    break  # Only count once


    print(total)




if __name__ == "__main__":
    main()