from itertools import permutations 

class Intcode():

    def __init__(self, inic, sez):
        self.inic = inic
        self.sez = sez
        self.pointer = 0
        self.output = None
        self.stop = False
        print('executing op')
        self.execute_opcode(self.inic)

    def execute_opcode(self, aug_inputs=None):
        while self.pointer < len(self.sez):
            opcode, mode1, mode2, mode3 = get_modes(self.sez[self.pointer])
            if opcode == 99:
                print('stop', self.inic)
                self.stop = True
                return

            elif opcode == 3:
                if aug_inputs is None:
                    print('Waiting for input', self.inic)
                    return 
                else:
                    # always in position mode
                    par1 = self.get_parameter(1, 1)
                    self.sez[par1] = aug_inputs
                    aug_inputs = None
                    self.pointer += 2

            elif opcode == 4:
                par1 = self.get_parameter(1, mode1)
                self.pointer += 2
                self.output = par1
                print('Setting self.output =',self.output,', amp_no:', self.inic)
                return

            elif opcode == 5:
                par1 = self.get_parameter(1, mode1)
                par2 = self.get_parameter(2, mode2)

                if par1 != 0:
                    self.pointer = par2
                else:
                    self.pointer += 3

            elif opcode == 6:
                par1 = self.get_parameter(1, mode1)
                par2 = self.get_parameter(2, mode2)

                if par1 == 0:
                    self.pointer = par2
                else:
                    self.pointer += 3

            elif opcode == 7:
                par1 = self.get_parameter(1, mode1)
                par2 = self.get_parameter(2, mode2)
                par3 = self.get_parameter(3, 1)

                if par1 < par2:
                    self.sez[par3] = 1
                else:
                    self.sez[par3] = 0
                self.pointer += 4
            
            elif opcode == 8:
                par1 = self.get_parameter(1, mode1)
                par2 = self.get_parameter(2, mode2)
                par3 = self.get_parameter(3, 1)

                if par1 == par2:
                    self.sez[par3] = 1
                else:
                    self.sez[par3] = 0
                self.pointer += 4

            elif opcode == 1:
                par1 = self.get_parameter(1, mode1)
                par2 = self.get_parameter(2, mode2)
                par3 = self.get_parameter(3, 1)

                self.sez[par3] = par1 + par2
                self.pointer += 4

            elif opcode == 2:
                par1 = self.get_parameter(1, mode1)
                par2 = self.get_parameter(2, mode2)
                par3 = self.get_parameter(3, 1)

                self.sez[par3] = par1 * par2
                self.pointer += 4
    
    def get_parameter(self, n, mode):
        if mode == 0: # position mode
            target = self.sez[self.pointer+n]
            parameter = self.sez[target]
        else: #immediate mode
            parameter = self.sez[self.pointer+n]
        return parameter


def get_modes(n):
    opcode = n % 100
    n = n // 100
    mode1 = n % 10
    n = n // 10
    mode2 = n % 10
    n = n // 10
    mode3 = n % 10
    return opcode, mode1, mode2, mode3


s = [3,8,1001,8,10,8,105,1,0,0,21,34,55,68,85,106,187,268,349,430,99999,3,9,1001,9,5,9,1002,9,5,9,4,9,99,3,9,1002,9,2,9,1001,9,2,9,1002,9,5,9,1001,9,2,9,4,9,99,3,9,101,3,9,9,102,3,9,9,4,9,99,3,9,1002,9,5,9,101,3,9,9,102,5,9,9,4,9,99,3,9,1002,9,4,9,1001,9,2,9,102,3,9,9,101,3,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,99]
max_out = 0
for perm in permutations([9,8,7,6,5]):

    # initiate Amps
    ampA = Intcode(perm[0],s.copy())
    ampB = Intcode(perm[1],s.copy())
    ampC = Intcode(perm[2],s.copy())
    ampD = Intcode(perm[3],s.copy())
    ampE = Intcode(perm[4],s.copy())

    ampA.execute_opcode(0)
    ampB.execute_opcode(ampA.output)
    ampC.execute_opcode(ampB.output)
    ampD.execute_opcode(ampC.output)
    ampE.execute_opcode(ampD.output)
    while not ampA.stop and not ampB.stop and not ampC.stop and not ampD.stop and not ampE.stop:
        ampA.execute_opcode(ampE.output)
        ampB.execute_opcode(ampA.output)
        ampC.execute_opcode(ampB.output)
        ampD.execute_opcode(ampC.output)
        ampE.execute_opcode(ampD.output)
        
    if ampE.output > max_out:
        max_out = ampE.output
print(max_out)