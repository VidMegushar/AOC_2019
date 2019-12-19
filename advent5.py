from itertools import permutations 

def execute_opcode(sez, inputs=None):
    pointer = 0
    while pointer < len(sez):
        opcode, mode1, mode2, mode3 = get_modes(sez[pointer])
        if opcode == 99:
            return sez

        elif opcode == 3:
            if inputs is None:
                print('input:')
                n = int(input())
            else:
                n = inputs.pop()
            target = sez[pointer+1]
            sez[target] = n
            pointer += 2

        elif opcode == 4:
            target = sez[pointer+1]
            out = sez[target]
            return out
            pointer += 2

        elif opcode == 5:
            n1 = sez[pointer+1] if mode1 == 1 else sez[sez[pointer+1]]
            n2 = sez[pointer+2] if mode2 == 1 else sez[sez[pointer+2]]
            if n1 != 0:
                pointer = n2
            else:
                pointer += 3

        elif opcode == 6:
            n1 = sez[pointer+1] if mode1 == 1 else sez[sez[pointer+1]]
            n2 = sez[pointer+2] if mode2 == 1 else sez[sez[pointer+2]]
            if n1 == 0:
                pointer = n2
            else:
                pointer += 3

        elif opcode == 7:
            n1 = sez[pointer+1] if mode1 == 1 else sez[sez[pointer+1]]
            n2 = sez[pointer+2] if mode2 == 1 else sez[sez[pointer+2]]
            n3 = sez[pointer+3]
            if n1 < n2:
                sez[n3] = 1
            else:
                sez[n3] = 0
            pointer += 4
        
        elif opcode == 8:
            n1 = sez[pointer+1] if mode1 == 1 else sez[sez[pointer+1]]
            n2 = sez[pointer+2] if mode2 == 1 else sez[sez[pointer+2]]
            n3 = sez[pointer+3]
            if n1 == n2:
                sez[n3] = 1
            else:
                sez[n3] = 0
            pointer += 4

        else:
            n1 = sez[pointer+1] if mode1 == 1 else sez[sez[pointer+1]]
            n2 = sez[pointer+2] if mode2 == 1 else sez[sez[pointer+2]]
            target = sez[pointer+3]

            if opcode == 1:
                # addition
                result = n1 + n2
                sez[target] = result
                pointer += 4
            elif opcode == 2:
                # multiplication
                result = n1 * n2
                sez[target] = result
                pointer += 4

def get_modes(n):
    opcode = n % 100
    n = n // 100
    mode1 = n % 10
    n = n // 10
    mode2 = n % 10
    n = n // 10
    mode3 = n % 10
    return opcode, mode1, mode2, mode3


s = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
in2 = 0
maxim = 0
for per in permutations([5,6,7,8,9]):
    in2 = 0
    for _ in range(9):
        for i in per:
            tmp = s.copy()
            in2 = execute_opcode(tmp,[in2,i])
        if in2 > maxim:
            maxim = in2

print(maxim)