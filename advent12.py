import math

class Moon():

    def __init__(self, pos):
        self.pos = pos
        self.vel = [0,0,0]
        self.init_pos = pos.copy()
        self.init_vel = [0,0,0]
    
    def change_position(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.pos[2] += self.vel[2]
    
    def change_x(self):
        self.pos[0] += self.vel[0]

    def change_y(self):
        self.pos[1] += self.vel[1]

    def change_z(self):
        self.pos[2] += self.vel[2]



def use_gravity(moon1,moon2):
    if moon1.pos[0] > moon2.pos[0]:
        moon1.vel[0] -= 1
        moon2.vel[0] += 1
    elif moon1.pos[0] < moon2.pos[0]:
        moon1.vel[0] += 1
        moon2.vel[0] -= 1

    if moon1.pos[1] > moon2.pos[1]:
        moon1.vel[1] -= 1
        moon2.vel[1] += 1
    elif moon1.pos[1] < moon2.pos[1]:
        moon1.vel[1] += 1
        moon2.vel[1] -= 1

    if moon1.pos[2] > moon2.pos[2]:
        moon1.vel[2] -= 1
        moon2.vel[2] += 1
    elif moon1.pos[2] < moon2.pos[2]:
        moon1.vel[2] += 1
        moon2.vel[2] -= 1

def use_gravity_x(moon1,moon2):
    if moon1.pos[0] > moon2.pos[0]:
        moon1.vel[0] -= 1
        moon2.vel[0] += 1
    elif moon1.pos[0] < moon2.pos[0]:
        moon1.vel[0] += 1
        moon2.vel[0] -= 1

def use_gravity_y(moon1,moon2):
    if moon1.pos[1] > moon2.pos[1]:
        moon1.vel[1] -= 1
        moon2.vel[1] += 1
    elif moon1.pos[1] < moon2.pos[1]:
        moon1.vel[1] += 1
        moon2.vel[1] -= 1

def use_gravity_z(moon1,moon2):
    if moon1.pos[2] > moon2.pos[2]:
        moon1.vel[2] -= 1
        moon2.vel[2] += 1
    elif moon1.pos[2] < moon2.pos[2]:
        moon1.vel[2] += 1
        moon2.vel[2] -= 1

moon1 = Moon([13,9,5])
moon2 = Moon([8,14,-2])
moon3 = Moon([-5,4,11])
moon4 = Moon([2,-6,1])

moons = [moon1,moon2,moon3,moon4]

stop = False
stepsx = 0
while not stop:
    stepsx += 1
    for i in range(len(moons)):
        for j in range(i,len(moons)):
            use_gravity_x(moons[i],moons[j])
    stop = True
    for m in moons:
        m.change_x()
        if m.pos[0] != m.init_pos[0] or m.vel[0] != 0:
            stop=False
print('steps x:',stepsx)

stop = False
stepsy = 0
while not stop:
    stepsy += 1
    for i in range(len(moons)):
        for j in range(i,len(moons)):
            use_gravity_y(moons[i],moons[j])
    stop = True
    for m in moons:
        m.change_y()
        if m.pos[1] != m.init_pos[1] or m.vel[1] != 0:
            stop=False
print('steps y:', stepsy)

stop = False
stepsz = 0
while not stop:
    stepsz += 1
    for i in range(len(moons)):
        for j in range(i,len(moons)):
            use_gravity_z(moons[i],moons[j])
    stop = True
    for m in moons:
        m.change_z()
        if m.pos[2] != m.init_pos[2] or m.vel[2] != 0:
            stop=False
print('steps z:', stepsz)

lcm_temp = stepsx*stepsy//math.gcd(stepsx,stepsy)
lcm = lcm_temp*stepsz/math.gcd(lcm_temp,stepsz)

print("steps:",lcm)