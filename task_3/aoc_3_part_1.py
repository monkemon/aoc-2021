"""

Tomasz Karlubik
"""

def main():
    input_file = open("binary_diagnostic.txt")

    # get rid of newlines
    records = input_file.read().splitlines()

    run_diagnosis(records)


def run_diagnosis(list):

    gamma_rate = 0
    epsilon_rate = 0
    mask = 0

    # iterate thru every position
    for i in range(0, len(list[0])):
        # list with all values from which we'll count all 0s and 1s
        bits = [ word[i] for word in list]

        zeros = bits.count('0')
        ones  = bits.count('1')

        # setting up a bit mask for later xoring to get epsilon rate
        mask = mask | 1

        # set the rightmost bit correspondingly to ones/zeros count
        if ones > zeros:
            gamma_rate = gamma_rate | 1

        # shift only if we're not at the last index of a word
        if i < len(list[0]) -1:
            gamma_rate = gamma_rate << 1
            mask = mask << 1

    # inverting only the masked part of `gamma_rate`
    epsilon_rate = gamma_rate ^ mask
        
    print(gamma_rate)
    print(epsilon_rate)


if __name__ == "__main__":
    main()
