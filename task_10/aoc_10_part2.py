"""
Program that checks parity of brackets
AoC 2021 - task 10, part 1

Tomasz Karlubik
"""

def main():
    input_file = open("syntax_errors.txt")
    lines = input_file.read().splitlines()

    result = calculate_syntax_scores(lines)
    result.sort()
    index = (len(result) - 1) // 2

    print(result[index])


# method that checks wether a line is incomplete, if yes, returns remainder of the stack
def is_incomplete(string):
    openers = '([{<'
    closers = ')]}>'

    pairs = {'(':')', '[':']', '{':'}', '<':'>'}

    # stack-based implementation of parity check for brackets
    stack = []
    
    for ch in string:
        if ch in openers:
            stack.append(ch)

        # on `closer` encounter, check if the last char on our stack matches
        # if yes, pop last char and proceed
        if ch in closers:
            if stack and ch == pairs[stack[-1]]:
                stack.pop()

            # line is corrupted
            else:
                return (False, [])

    # line OK
    if not stack:
        return (False, [])
    # line incomplete, reverse list, then reverse brackets
    else:
        stack.reverse()
        stack = [pairs[x] for x in stack]
        return (True, stack)


def calculate_syntax_scores(lines):
    scores = []
    syntaxScore = 0

    closerCharScores = {')':1, ']':2, '}':3, '>':4}

    for line in lines:
        syntaxScore = 0
        checkResult = is_incomplete(line)

        # is result incomplete?
        if checkResult[0] == True:
            # characters that need to be appended to match all brackets
            for char in checkResult[1]:
                syntaxScore = syntaxScore * 5
                syntaxScore = syntaxScore + closerCharScores[char]
            scores.append(syntaxScore)

    return scores
            

if __name__ == "__main__":
    main()