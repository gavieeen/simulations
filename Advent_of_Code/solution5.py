from functools import cache

keypad = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    [None, "0", "A"]
]

control = [
    [None, '^', 'A'],
    ['<', 'v', '>']
]

num_to_coord = {
    keypad[r][c]: (r, c)
    for r in range(len(keypad))
    for c in range(len(keypad[r]))
    if keypad[r][c] is not None
}

dir_to_coord = {
    control[r][c]: (r, c)
    for r in range(len(control))
    for c in range(len(control[r]))
    if control[r][c] is not None
}

def is_ok(grid, i, j, cmd_seq):
    for cmd in cmd_seq:
        if cmd == '^':
            i -= 1
        elif cmd == 'v':
            i += 1
        elif cmd == '<':
            j -= 1
        elif cmd == '>':
            j += 1
        if not (0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] is not None):
            return False
    return True

# Part 1
@cache
def get_sequence_to_move(is_num, start, end):
    # get the sequence to move a bot from start to end
    grid = keypad if is_num else control
    i, j = start
    i2, j2 = end
    i_seq = 'v' * (i2 - i) if i2 > i else '^' * (i - i2)
    j_seq = '>' * (j2 - j) if j2 > j else '<' * (j - j2)
    # either i first or j first
    cmd1 = i_seq + j_seq
    cmd2 = j_seq + i_seq
    cmds = []
    if is_ok(grid, i, j, cmd1):
        cmds.append(cmd1)
    if is_ok(grid, i, j, cmd2):
        cmds.append(cmd2)
    return cmds

def find_min_sequence(code, num_bots=2):
    @cache
    def solve(seq, i):
        # me pressing the buttons myself
        if i == num_bots + 1:
            return len(seq)
        # the bot always start at A
        start = dir_to_coord['A'] if i > 0 else num_to_coord['A']
        total = 0
        for c in seq:
            end = dir_to_coord[c] if i > 0 else num_to_coord[c]
            soln = float('inf')
            # find sequence to emit c
            for sub_seq in get_sequence_to_move(i == 0, start, end):
                soln = min(soln, solve(f'{sub_seq}A', i+1))
            start = end
            total += soln
        return total

    return solve(code, 0)

test = 'input.txt'
with open(test, "r") as file:
    codes = list(map(str, file.read().strip().split("\n")))

print(sum(int(code[:-1]) * find_min_sequence(code) for code in codes))

# Part 2
print(sum(int(code[:-1]) * find_min_sequence(code, 25) for code in codes))