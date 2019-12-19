mapping = {}
f = open('advent6.txt','r')
for line in f:
    line = line.strip()
    obj1, obj2 = line.split(')')
    if obj1 not in mapping.keys():
        mapping[obj1] = []
    if obj2 not in mapping.keys():
        mapping[obj2] = []
    mapping[obj2].append(obj1)

total_orbits = 0
you = []
santa = []
checked_planets = ['SAN']
while len(checked_planets) > 0:
    dir_orbits = mapping[checked_planets.pop()]
    for i in dir_orbits:
        santa.append(i)
        checked_planets.append(i)

checked_planets = ['YOU']
while len(checked_planets) > 0:
    dir_orbits = mapping[checked_planets.pop()]
    for i in dir_orbits:
        you.append(i)
        checked_planets.append(i)

n = len(santa)
i = 0
while i < len(santa):
    if santa[i] in you:
        you.remove(santa[i])
        santa.remove(santa[i])
    else:
        i += 1
print(len(you) + len(santa))
