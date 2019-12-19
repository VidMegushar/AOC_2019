import math

f = open('ad14.txt', 'r')
recepti = dict()
for line in f:
    vhod, izhod = line.split('=>')
    izhod = izhod.strip().split(' ')
    recepti[izhod[1]] = []
    recepti[izhod[1]].append(izhod[0])
    
    vhod = vhod.split(',')
    vhod = [(x.strip().split(' ')[1], x.strip().split(' ')[0]) for x in vhod]
    recepti[izhod[1]].append(vhod)

all_ORE = 1000000000000
fuel = 0
excess = dict()
excess['FUEL'] = 0
pr = all_ORE // 10000000000
while all_ORE > 0:
    print(all_ORE)
    needs_res = ['FUEL']
    needs = dict()
    needs['FUEL'] = 1
    ORE = 0

    while needs_res != []:
        needed_res = needs_res.pop()
        needed_amount = needs[needed_res]
        if needed_res == 'ORE':
            ORE += needed_amount
            needs['ORE'] = 0
        else:    

            # check if we have any extra resource
            if needed_res in excess:
                temp_extras = excess[needed_res]
                excess[needed_res] = 0
            else:
                temp_extras = 0
                excess[needed_res] = 0

            recept = recepti[needed_res]
            result_amount = int(recept[0])
            input_res = recept[1]
            # If we have enough resources left, just use them
            if temp_extras > result_amount:
                excess[needed_res] = temp_extras - result_amount
            # We generate new resources
            else:
                needed_amount -= temp_extras
                #first calculate number of times the reaction has to be made
                repetitions = math.ceil(needed_amount/result_amount)
                excess[needed_res] = result_amount*repetitions - needed_amount
                for res in input_res:
                    if res[0] in needs_res:
                        needs[res[0]] += int(res[1])*repetitions
                    else:
                        needs_res.append(res[0])
                        needs[res[0]] = int(res[1])*repetitions
        needs[needed_res] = 0
    all_ORE -= ORE
    fuel += 1
            
print(all_ORE)
print(fuel)


