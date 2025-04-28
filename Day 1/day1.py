# Thought process:
# function to read in input.txt file and split into two lists: left and right
# fucntion to order the list in numerical order (doesn't matter if ascending or descending, as long as both lists are the same)
# function to walk through through lists and find the distance between each index. Store the total distance


def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read all lines and split them into individual numbers (assuming two numbers per line)
            lines = file.readlines()
            left = []
            right = []
            for line in lines:
                num1, num2 = line.split()
                left.append(int(num1))
                right.append(int(num2))
            return left, right
    except FileNotFoundError:
        print("File not found.")
        return [], []

def main():
    file_path = "Python-Advent-2024/Day1/input.txt"
    left, right = read_file(file_path)

    left.sort()
    right.sort()

    diff = [
        abs(x - y)
        for x, y in zip(left, right)
    ]

    # print(len(diff))

    # print(left[0])
    # print(right[0])
    # print(diff[0])

    total = sum(diff)

    print(total)

    # part 2

    similarity_count = [
        right.count(x)
        for x in left
    ]

    similarity_score = [
        x * y
        for x, y in zip (left, similarity_count)
    ]

    similarity_total = sum(similarity_score)
    print(similarity_total)

if __name__ == "__main__":
    main()