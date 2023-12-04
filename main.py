import re


def day1():
    with open("inputs/day1.txt", "r") as input_file:
        total_sum = 0
        for line in input_file.readlines():
            result = re.findall(r'\d', line)
            if len(result) == 0:
                continue
            total_sum += int(f"{result[0]}{result[-1]}")
        print("Total sum is:", total_sum)


if __name__ == "__main__":
    day1()
