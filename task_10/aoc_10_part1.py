"""
Program that checks parity of brackets and returns syntax error score according to a table at AoC website
AoC 2021 - task 10, part 1

Tomasz Karlubik
"""

def main():
    input_file = open("syntax_errors.txt")

    lines = input_file.read().splitlines()

    # testing purposes
    # print(lines)
    print(calculate_syntax_score(lines))

# method that catches first corrupted chunk and returns the corrupted char or None if string is ok
def is_corrupted(string):
    openers = '([{<'
    closers = ')]}>'

    pairs = {'(':')', '[':']', '{':'}', '<':'>'}

    # stack-based implementation of parity check for brackets
    stack = []
    
    for ch in string:
        if ch in openers:
            stack.append(ch)

        # on `closer` encounter, check if the last char on our stack matches
        # if yes, pop last char and proceed, if not, return the mismatched bracket
        if ch in closers:
            if ch == pairs[stack[-1]]:
                stack.pop()
            
            else:
                return ch

    return None


def calculate_syntax_score(lines):
    syntax_score = 0

    error_scores = {')':3, ']':57, '}':1197, '>':25137}

    for line in lines:
        tempChar = is_corrupted(line)
        if tempChar is not None:
            syntax_score = syntax_score + error_scores[tempChar]
    
    return syntax_score


            

if __name__ == "__main__":
    main()
