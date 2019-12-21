class Intcode():

    def __init__(self, inic, sez):
        self.inic = inic
        self.sez = sez
        self.pointer = 0
        self.output = None
        self.stop = False
        self.relative_base = 0
        self.execute_opcode(self.inic)

    def execute_opcode(self, aug_inputs=None):
        while self.pointer < len(self.sez):
            opcode, mode1, mode2, mode3 = get_modes(self.sez[self.pointer])
            if opcode == 99:
                print('stopping!!')
                self.stop = True
                return

            elif opcode == 3:
                if aug_inputs is None:
                    #print('Waiting for input!!')
                    return 
                else:
                    target = self.get_parameter(1, mode1)
                    self.sez[target] = aug_inputs
                    #print("Input:",aug_inputs)
                    aug_inputs = None
                    self.pointer += 2

            elif opcode == 4:
                target = self.get_parameter(1, mode1)
                self.pointer += 2
                self.output = self.sez[target]
                #print("output:", self.output)
                return

            elif opcode == 5:
                target1 = self.get_parameter(1, mode1)
                par1 = self.sez[target1]
                target2 = self.get_parameter(2, mode2)
                par2 = self.sez[target2]

                if par1 != 0:
                    self.pointer = par2
                else:
                    self.pointer += 3

            elif opcode == 6:
                target1 = self.get_parameter(1, mode1)
                par1 = self.sez[target1]
                target2 = self.get_parameter(2, mode2)
                par2 = self.sez[target2]

                if par1 == 0:
                    self.pointer = par2
                else:
                    self.pointer += 3

            elif opcode == 7:
                target1 = self.get_parameter(1, mode1)
                par1 = self.sez[target1]
                target2 = self.get_parameter(2, mode2)
                par2 = self.sez[target2]
                target3 = self.get_parameter(3, mode3)

                if par1 < par2:
                    self.sez[target3] = 1
                else:
                    self.sez[target3] = 0
                self.pointer += 4
            
            elif opcode == 8:
                target1 = self.get_parameter(1, mode1)
                par1 = self.sez[target1]
                target2 = self.get_parameter(2, mode2)
                par2 = self.sez[target2]
                target3 = self.get_parameter(3, mode3)

                if par1 == par2:
                    self.sez[target3] = 1
                else:
                    self.sez[target3] = 0
                self.pointer += 4

            elif opcode == 1:
                target1 = self.get_parameter(1, mode1)
                par1 = self.sez[target1]
                target2 = self.get_parameter(2, mode2)
                par2 = self.sez[target2]
                target3 = self.get_parameter(3, mode3)

                self.sez[target3] = par1 + par2
                self.pointer += 4

            elif opcode == 2:
                target1 = self.get_parameter(1, mode1)
                par1 = self.sez[target1]
                target2 = self.get_parameter(2, mode2)
                par2 = self.sez[target2]
                target3 = self.get_parameter(3, mode3)

                self.sez[target3] = par1 * par2
                self.pointer += 4
            
            elif opcode == 9:
                target1 = self.get_parameter(1, mode1)
                par1 = self.sez[target1]
                self.relative_base += par1
                self.pointer += 2


    
    def get_parameter(self, n, mode):
        if mode == 0: # position mode
            target = self.sez[self.pointer+n]
        elif mode == 1:
            target = self.pointer + n
        elif mode == 2:
            target = self.relative_base + self.sez[self.pointer + n]
        
        if target >= len(self.sez):
            self.sez += [0 for _ in range(target-len(self.sez) + 2)]
        
        return target


def get_modes(n):
    opcode = n % 100
    n = n // 100
    mode1 = n % 10
    n = n // 10
    mode2 = n % 10
    n = n // 10
    mode3 = n % 10
    return opcode, mode1, mode2, mode3
  
s = [109,424,203,1,21101,11,0,0,1105,1,282,21102,1,18,0,1106,0,259,1201,1,0,221,203,1,21101,0,31,0,1106,0,282,21101,0,38,0,1105,1,259,21002,23,1,2,21201,1,0,3,21101,0,1,1,21101,0,57,0,1106,0,303,2102,1,1,222,21002,221,1,3,20102,1,221,2,21102,259,1,1,21101,0,80,0,1105,1,225,21102,1,118,2,21102,91,1,0,1105,1,303,2102,1,1,223,21001,222,0,4,21102,259,1,3,21101,0,225,2,21101,225,0,1,21101,0,118,0,1105,1,225,20101,0,222,3,21102,1,72,2,21102,133,1,0,1106,0,303,21202,1,-1,1,22001,223,1,1,21102,1,148,0,1105,1,259,1201,1,0,223,20101,0,221,4,20101,0,222,3,21101,22,0,2,1001,132,-2,224,1002,224,2,224,1001,224,3,224,1002,132,-1,132,1,224,132,224,21001,224,1,1,21102,1,195,0,106,0,108,20207,1,223,2,20101,0,23,1,21102,-1,1,3,21102,214,1,0,1105,1,303,22101,1,1,1,204,1,99,0,0,0,0,109,5,1201,-4,0,249,22101,0,-3,1,22101,0,-2,2,22101,0,-1,3,21101,0,250,0,1105,1,225,21202,1,1,-4,109,-5,2105,1,0,109,3,22107,0,-2,-1,21202,-1,2,-1,21201,-1,-1,-1,22202,-1,-2,-2,109,-3,2106,0,0,109,3,21207,-2,0,-1,1206,-1,294,104,0,99,22102,1,-2,-2,109,-3,2105,1,0,109,5,22207,-3,-4,-1,1206,-1,346,22201,-4,-3,-4,21202,-3,-1,-1,22201,-4,-1,2,21202,2,-1,-1,22201,-4,-1,1,22101,0,-2,3,21101,0,343,0,1106,0,303,1105,1,415,22207,-2,-3,-1,1206,-1,387,22201,-3,-2,-3,21202,-2,-1,-1,22201,-3,-1,3,21202,3,-1,-1,22201,-3,-1,2,21202,-4,1,1,21101,384,0,0,1106,0,303,1106,0,415,21202,-4,-1,-4,22201,-4,-3,-4,22202,-3,-2,-2,22202,-2,-4,-4,22202,-3,-2,-3,21202,-4,-1,-2,22201,-3,-2,1,21201,1,0,-4,109,-5,2106,0,0]

velikost = 200

"""
mapa = [[None for _ in range(velikost)] for _ in range(velikost)]
affected = 0
laser1 = Intcode(None,s)
for i in range(velikost):
    if i % 10 == 0:
        print("i:", i)
    for j in range(velikost):
        laser = Intcode(None, s.copy())
        laser.execute_opcode(i)
        laser.execute_opcode(j)
        pull = laser.output
        if pull == 1:
            mapa[i][j] = "#"
            affected += 1
        else:
            mapa[i][j] = "."
        laser = None
"""
def test_fit(s,position):
    laser1 = Intcode(None, s.copy())
    laser1.execute_opcode(position[0]+99)
    laser1.execute_opcode(position[1])
    laser2 = Intcode(None, s.copy())
    laser2.execute_opcode(position[0])
    laser2.execute_opcode(position[1]-99)
    laser3 = Intcode(None, s.copy())
    laser3.execute_opcode(position[0]+99)
    laser3.execute_opcode(position[1]-99)

    if laser1.output == 1 and laser2.output == 1 and laser3.output == 1:
        return True
    return False
    

pos = [416,589]
#pos = [6,8]
path = []
for i in range(1000):
    finish = test_fit(s,pos)
    if finish:
        print(pos)
        break
    laser = Intcode(None, s.copy())
    laser.execute_opcode(pos[0])
    laser.execute_opcode(pos[1]+1)
    if laser.output == 1:
        pos[1] += 1
    else:
        pos[0] += 1
    laser = None
    path.append(pos.copy())

if not finish:
    print(path)
