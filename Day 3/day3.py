# scan for mul( and end at the next ) ?? maybe?
# check to see if it follows mul(number,number) and discard the rest
# do the actual math and add up what's remaining

import re

def extract_mul_calls(text):
    # Use parentheses () inside the regex to capture the two numbers separately
    pattern = r"(do\(\))|(don't\(\))|(mul\((\d+),(\d+)\))"
    status = True
    results = []
    for match in re.finditer(pattern, text):
        if match.group(1):  # do()
            status = True
        elif match.group(2):  # dont()
            status = False
        elif match.group(3):  # mul(a,b)
            if status:

                a = int(match.group(4))
                b = int(match.group(5))
                results.append(a * b)
    return results

def main():

    with open("Python-Advent-2024/Day 3/input.txt", "r") as file:
        content = file.read()

    matches = extract_mul_calls(content)

    print(len(matches))

    total = sum(matches)

    print(total)

if __name__ == "__main__":
    main()