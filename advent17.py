class Intcode():

    def __init__(self, inic, sez):
        self.inic = inic
        self.sez = sez
        self.pointer = 0
        self.output = None
        self.stop = False
        self.relative_base = 0
        self.execute_opcode(self.inic)
        self.need_input = False

    def execute_opcode(self, aug_inputs=None):
        while self.pointer < len(self.sez):
            opcode, mode1, mode2, mode3 = get_modes(self.sez[self.pointer])
            if opcode == 99:
                print('stop', self.inic)
                self.stop = True
                return

            elif opcode == 3:
                if aug_inputs is None:
                    #print('Waiting for input!!')
                    self.need_input = True
                    return 
                else:
                    target = self.get_parameter(1, mode1)
                    self.sez[target] = aug_inputs
                    #print("got input", aug_inputs)
                    aug_inputs = None
                    self.pointer += 2
                    self.need_input = False

            elif opcode == 4:
                target = self.get_parameter(1, mode1)
                self.pointer += 2
                self.output = self.sez[target]
                #print("Output:", self.output)
                #print("Out:",chr(self.output))

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
    

s = [2,330,331,332,109,3914,1101,0,1182,15,1102,1,1457,24,1002,0,1,570,1006,570,36,1002,571,1,0,1001,570,-1,570,1001,24,1,24,1106,0,18,1008,571,0,571,1001,15,1,15,1008,15,1457,570,1006,570,14,21102,1,58,0,1105,1,786,1006,332,62,99,21102,333,1,1,21101,0,73,0,1105,1,579,1101,0,0,572,1101,0,0,573,3,574,101,1,573,573,1007,574,65,570,1005,570,151,107,67,574,570,1005,570,151,1001,574,-64,574,1002,574,-1,574,1001,572,1,572,1007,572,11,570,1006,570,165,101,1182,572,127,1002,574,1,0,3,574,101,1,573,573,1008,574,10,570,1005,570,189,1008,574,44,570,1006,570,158,1106,0,81,21102,1,340,1,1105,1,177,21102,477,1,1,1106,0,177,21102,1,514,1,21101,0,176,0,1105,1,579,99,21102,1,184,0,1105,1,579,4,574,104,10,99,1007,573,22,570,1006,570,165,102,1,572,1182,21101,375,0,1,21101,0,211,0,1106,0,579,21101,1182,11,1,21102,1,222,0,1105,1,979,21102,388,1,1,21101,0,233,0,1106,0,579,21101,1182,22,1,21102,244,1,0,1106,0,979,21101,0,401,1,21101,255,0,0,1105,1,579,21101,1182,33,1,21101,266,0,0,1106,0,979,21101,0,414,1,21102,277,1,0,1105,1,579,3,575,1008,575,89,570,1008,575,121,575,1,575,570,575,3,574,1008,574,10,570,1006,570,291,104,10,21102,1182,1,1,21101,0,313,0,1106,0,622,1005,575,327,1102,1,1,575,21101,327,0,0,1105,1,786,4,438,99,0,1,1,6,77,97,105,110,58,10,33,10,69,120,112,101,99,116,101,100,32,102,117,110,99,116,105,111,110,32,110,97,109,101,32,98,117,116,32,103,111,116,58,32,0,12,70,117,110,99,116,105,111,110,32,65,58,10,12,70,117,110,99,116,105,111,110,32,66,58,10,12,70,117,110,99,116,105,111,110,32,67,58,10,23,67,111,110,116,105,110,117,111,117,115,32,118,105,100,101,111,32,102,101,101,100,63,10,0,37,10,69,120,112,101,99,116,101,100,32,82,44,32,76,44,32,111,114,32,100,105,115,116,97,110,99,101,32,98,117,116,32,103,111,116,58,32,36,10,69,120,112,101,99,116,101,100,32,99,111,109,109,97,32,111,114,32,110,101,119,108,105,110,101,32,98,117,116,32,103,111,116,58,32,43,10,68,101,102,105,110,105,116,105,111,110,115,32,109,97,121,32,98,101,32,97,116,32,109,111,115,116,32,50,48,32,99,104,97,114,97,99,116,101,114,115,33,10,94,62,118,60,0,1,0,-1,-1,0,1,0,0,0,0,0,0,1,0,16,0,109,4,2102,1,-3,586,21001,0,0,-1,22101,1,-3,-3,21102,0,1,-2,2208,-2,-1,570,1005,570,617,2201,-3,-2,609,4,0,21201,-2,1,-2,1106,0,597,109,-4,2106,0,0,109,5,2102,1,-4,629,21001,0,0,-2,22101,1,-4,-4,21102,1,0,-3,2208,-3,-2,570,1005,570,781,2201,-4,-3,653,20101,0,0,-1,1208,-1,-4,570,1005,570,709,1208,-1,-5,570,1005,570,734,1207,-1,0,570,1005,570,759,1206,-1,774,1001,578,562,684,1,0,576,576,1001,578,566,692,1,0,577,577,21101,0,702,0,1106,0,786,21201,-1,-1,-1,1106,0,676,1001,578,1,578,1008,578,4,570,1006,570,724,1001,578,-4,578,21101,731,0,0,1106,0,786,1106,0,774,1001,578,-1,578,1008,578,-1,570,1006,570,749,1001,578,4,578,21101,0,756,0,1105,1,786,1106,0,774,21202,-1,-11,1,22101,1182,1,1,21101,774,0,0,1105,1,622,21201,-3,1,-3,1106,0,640,109,-5,2105,1,0,109,7,1005,575,802,21002,576,1,-6,21002,577,1,-5,1105,1,814,21101,0,0,-1,21102,1,0,-5,21102,1,0,-6,20208,-6,576,-2,208,-5,577,570,22002,570,-2,-2,21202,-5,63,-3,22201,-6,-3,-3,22101,1457,-3,-3,2101,0,-3,843,1005,0,863,21202,-2,42,-4,22101,46,-4,-4,1206,-2,924,21102,1,1,-1,1106,0,924,1205,-2,873,21102,35,1,-4,1106,0,924,1202,-3,1,878,1008,0,1,570,1006,570,916,1001,374,1,374,1201,-3,0,895,1102,2,1,0,1202,-3,1,902,1001,438,0,438,2202,-6,-5,570,1,570,374,570,1,570,438,438,1001,578,558,921,21001,0,0,-4,1006,575,959,204,-4,22101,1,-6,-6,1208,-6,63,570,1006,570,814,104,10,22101,1,-5,-5,1208,-5,39,570,1006,570,810,104,10,1206,-1,974,99,1206,-1,974,1102,1,1,575,21102,1,973,0,1106,0,786,99,109,-7,2105,1,0,109,6,21101,0,0,-4,21101,0,0,-3,203,-2,22101,1,-3,-3,21208,-2,82,-1,1205,-1,1030,21208,-2,76,-1,1205,-1,1037,21207,-2,48,-1,1205,-1,1124,22107,57,-2,-1,1205,-1,1124,21201,-2,-48,-2,1105,1,1041,21101,-4,0,-2,1106,0,1041,21102,-5,1,-2,21201,-4,1,-4,21207,-4,11,-1,1206,-1,1138,2201,-5,-4,1059,2101,0,-2,0,203,-2,22101,1,-3,-3,21207,-2,48,-1,1205,-1,1107,22107,57,-2,-1,1205,-1,1107,21201,-2,-48,-2,2201,-5,-4,1090,20102,10,0,-1,22201,-2,-1,-2,2201,-5,-4,1103,2101,0,-2,0,1106,0,1060,21208,-2,10,-1,1205,-1,1162,21208,-2,44,-1,1206,-1,1131,1105,1,989,21102,439,1,1,1106,0,1150,21101,0,477,1,1105,1,1150,21101,0,514,1,21101,1149,0,0,1105,1,579,99,21101,1157,0,0,1105,1,579,204,-2,104,10,99,21207,-3,22,-1,1206,-1,1138,2102,1,-5,1176,2101,0,-4,0,109,-6,2105,1,0,46,11,52,1,9,1,52,1,9,1,52,1,9,1,12,7,33,1,9,1,12,1,5,1,33,1,9,1,12,1,5,1,9,1,23,1,9,1,12,1,5,1,9,1,23,1,9,1,12,1,5,1,9,1,23,1,9,1,12,1,5,1,9,1,23,1,9,1,12,1,5,13,19,13,12,1,15,1,1,1,19,1,1,1,22,1,15,13,5,7,22,1,17,1,9,1,5,1,3,1,24,1,17,1,9,1,5,1,3,1,24,1,17,1,9,1,5,1,3,1,18,7,17,13,3,1,1,9,46,1,1,1,3,1,1,1,1,1,5,1,46,13,3,1,48,1,3,1,1,1,1,1,1,1,3,1,48,1,3,13,46,1,5,1,1,1,1,1,3,1,1,1,46,9,1,1,3,13,42,1,3,1,5,1,9,1,42,1,3,1,5,1,9,1,42,1,3,1,5,1,9,1,40,7,5,1,9,1,40,1,1,1,9,1,9,1,30,13,9,1,9,1,30,1,9,1,11,1,9,1,30,1,9,1,11,1,9,1,30,1,9,1,11,1,9,1,30,1,9,1,11,11,30,1,9,1,52,1,9,1,52,1,9,1,52,1,9,1,52,1,9,1,52,11,22]
"""
robot = Intcode(None,s)
all_scafs = []
scaffold = ""
while not robot.need_input:
  if robot.output == 35:
    scaffold += "#"
  elif robot.output == 46:
    scaffold += "."
  elif robot.output == 60:
    scaffold += "<"
  elif robot.output == 60:
    scaffold += ">"
  elif robot.output == 94:
    scaffold += "^"
  elif robot.output == 10:
    all_scafs.append(scaffold)
    scaffold = ""
  robot.execute_opcode()


new_l = ["." for _ in range(len(all_scafs[0])+2)]
new_line = ""
for ss in new_l:
  new_line += ss

new_scafs = []
new_scafs.append(new_line)
for s in all_scafs[:-1]:
  new_s = "."
  new_s += s
  new_s += "."
  new_scafs.append(new_s)

new_scafs.append(new_line)


for p in new_scafs:
  print(p)

all_scafs = new_scafs


robot_pos = [17,1]
# gor, dol, levo, desno
dirs = [(-1,0),(1,0),(0,-1),(0,1)]
temp_dir = dirs[3]
visited = [robot_pos.copy()]
intersections = []




stop = False
while not stop:
  if all_scafs[robot_pos[0] + temp_dir[0]][robot_pos[1] + temp_dir[1]] == "#":
    robot_pos[0] += temp_dir[0]
    robot_pos[1] += temp_dir[1]
    #print(robot_pos)
    if robot_pos in visited:
      intersections.append(robot_pos.copy())
      print("inters:",intersections)
    visited.append(robot_pos.copy())
  else:
    stop = True
    for dire in dirs:
      #print(dire)
      if dire[0] != temp_dir[0]*(-1) and dire[1] != temp_dir[1]*(-1):
        #print("dir, temp_dir",dire, temp_dir)
        if all_scafs[robot_pos[0] + dire[0]][robot_pos[1] + dire[1]] == "#":
          stop = False
          temp_dir = dire
          break

result = 0
for i in intersections:
  result += (i[0]-1)*(i[1]-1)
print(result)


def get_rotation(dir1,dir2):
    if dir1 == (1,0): #down
        if dir2 == (0,-1): #left
            return "R"
        else:
            return "L"
    if dir1 == (-1,0): #up
        if dir2 == (0,-1): #left
            return "L"
        else:
            return "R"
    if dir1 == (0,-1): #left
        if dir2 == (-1,0): #up
            return "R"
        else:
            return "L"
    if dir1 == (0,1): #right
        if dir2 == (-1,0): #up
            return "L"
        else:
            return "R"
stop = False
count = 0
path = []
while not stop:
  if all_scafs[robot_pos[0] + temp_dir[0]][robot_pos[1] + temp_dir[1]] == "#":
    count += 1
    robot_pos[0] += temp_dir[0]
    robot_pos[1] += temp_dir[1]
  else:
    stop = True
    for dire in dirs:
      if dire[0] != temp_dir[0]*(-1) and dire[1] != temp_dir[1]*(-1):
        if all_scafs[robot_pos[0] + dire[0]][robot_pos[1] + dire[1]] == "#":
          stop = False
          rot = get_rotation(temp_dir, dire)
          path.append(count)
          path.append(rot)
          temp_dir = dire
          count = 0
          break
"""
robot = Intcode(None,s)
while not robot.need_input:
  robot.execute_opcode()



MOVE = ["A",",","A",",","B",",","C",",","B",",","C",",","B",",","C",",","B",",","A"]
MOVE = [ord(c) for c in MOVE]
MOVE.append(10)

A = ["R",",","6",",","L",",","1","2",",","R",",","6"]
A = [ord(c) for c in A]
A.append(10)

B = ["L",",","1","2",",","R",",","6",",","L",",","8",",","L",",","1","2"]
B = [ord(c) for c in B]
B.append(10)

C = ["R",",","1","2",",","L",",","1","0",",","L",",","1","0"]
C = [ord(c) for c in C]
C.append(10)


orders = []
orders += MOVE
orders += A
orders += B
orders += C
orders.append(ord("n"))
#orders.append(10)
counter = 0
#print(orders)

while counter < len(orders):
  robot.execute_opcode()
  if robot.need_input:
    robot.execute_opcode(orders[counter])
    counter += 1

robot.execute_opcode(10)

all_scafs = []
scaffold = ""
while not robot.stop:
  if robot.output == 35:
    scaffold += "#"
  elif robot.output == 46:
    scaffold += "."
  elif robot.output == 60:
    scaffold += "<"
  elif robot.output == 60:
    scaffold += ">"
  elif robot.output == 94:
    scaffold += "^"
  elif robot.output == 10:
    #all_scafs.append(scaffold)
    print(scaffold)
    scaffold = ""
  else:
    scaffold += "d"
  robot.execute_opcode()


print("REAL OUTPUT",robot.output)
