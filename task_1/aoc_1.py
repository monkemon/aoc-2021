"""
Program that calculates number of increases in values from a list.
AoC 2021 - task 1, part 2

Tomasz Karlubik
"""


def main():
    input_file = open("depth_report.txt")

    depths = [int(x) for x in input_file]

    # testing purposes
    # print(depths)

    print(f"Number of increases: {countIncreases(depths)}")

def countIncreases(list):
    increase_count = 0

    # we will iterate from 1 to n - 2 so i can set `previous` now
    previous = list[0] + list[1] + list[2]
    current = 0

    for i in range(1, len(list) - 2):
        current = list[i] + list[i + 1] + list[i + 2]

        if current > previous:
            increase_count = increase_count + 1

        # set previous for next iteration 
        previous = current
    
    return increase_count


if __name__ == "__main__":
    main()
