from collections import Counter, deque

def runProgram(operands, commands, reg_a):
    output = []
    i = 0
    operands[4] = reg_a
    while i < len(commands):
        cmd, operand = commands[i:i+2]
        if cmd == 0:
            operands[4] //= (1 << operands[operand])
        elif cmd == 1:
            operands[5] ^= operand
        elif cmd == 2:
            operands[5] = operands[operand] % 8
        elif cmd == 3 and operands[4]:
            i = operand
            continue
        elif cmd == 4:
            operands[5] ^= operands[6]
        elif cmd == 5:
            output.append(operands[operand] % 8)
        else:
            operands[cmd - 1] = operands[4] // (1 << operands[operand])
        i += 2
    
    return output
            

test = 'input1.txt'
with open(test, "r") as file:
    operands = list(range(4))
    registers, commands = file.read().strip().split("\n\n")
    
    registers = registers.splitlines()
    operands.extend([int(registers[0].split()[-1]), int(registers[1].split()[-1]), int(registers[2].split()[-1])])
    commands = list(map(int, commands.split()[-1].split(",")))

print(operands)
print(','.join(map(str, runProgram(operands, commands, commands[4]))))
print(operands[4])

# def find_range_start(num_digits):
#     lo = 0
#     hi = 1000000000000000
#     while lo < hi:
#         mid = (lo + hi) // 2

#         if len(runProgram(operands, commands, mid)) < num_digits:
#             lo = mid + 1
#         else:
#             hi = mid
#     return lo


# range_begin = find_range_start(len(commands))
# range_end = find_range_start(len(commands) + 1)
# print(f"Part 2: [{range_begin}, {range_end})")

# count = 0
# for reg_a in range(range_begin, range_end):
#     output = runProgram(operands, commands, reg_a)
#     if output == commands:
#         print(reg_a)
#         break

q = deque([(len(commands), 0)])
while q:
    pos, a = q.popleft()
    for i in range(8):
        n_a = (
            a << 3) + i
        o = list(map(int, runProgram(operands, commands, n_a)))
        if o == commands[pos-1:]:
            q.append((pos - 1, n_a))
            if len(o) == len(commands):
                print(n_a)