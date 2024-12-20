# Part 1
def possible(target, words):
    n = len(target)
    can_form = [False] * (n + 1)
    can_form[0] = True # can form empty string with no words
    
    for i in range(1, n + 1):
        for j in reversed(range(i)):
            if can_form[j] and target[j:i] in words:
                can_form[i] = True
                break
    
    return can_form[n]

# Part 2
def getWays(target, words):
    n = len(target)
    num_ways = [0] * (n + 1)
    num_ways[0] = 1 # one way to form empty string -> no words
    
    for i in range(1, n + 1):
        for j in reversed(range(i)):
            if target[j:i] in words:
                num_ways[i] += num_ways[j]
    
    return num_ways[n]

test = 'input.txt'
with open(test, "r") as file:
    operands = list(range(4))
    words, targets = file.read().strip().split("\n\n")
    
    targets = targets.splitlines()
    words = set(words.split(', '))

count = sum(possible(target, words) for target in targets)
ways = sum(getWays(target, words) for target in targets)
print(ways)
