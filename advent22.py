def deal_into_new(sez):
    sez.reverse()
    return sez

def cut(sez,n):
    new_s = sez[n:]
    new_s += sez[:n]
    return new_s

def deal_with_increment(sez, inc):
    new_s = [None for _ in sez]
    count = 0
    pointer = 0
    while count < len(sez):
        new_s[pointer] = sez[count]
        count += 1
        pointer += inc
        if pointer >= len(sez):
            pointer -= len(sez)
    return new_s


s = [0,1,2,3,4,5,6,7,8,9]
#s = [i for i in range(119315717514047)]
#print(s[2020])
'''
f = open("input22.txt","r")
for line in f:
    line = line.split(" ")
    if line[0] == "cut":
        s = cut(s,int(line[1]))
    elif line[1] == "into":
        s = deal_into_new(s)
    elif line[1] == "with":
        s = deal_with_increment(s,int(line[3]))

print(s[2020])
'''

s1 = s.copy()
s1 = deal_with_increment(s1,3)
s1 = deal_into_new(s1)

s2 = s.copy()
s2 = deal_into_new(s2)
s2 = deal_with_increment(s2,3)

print(s1)
print(s2)