def bug_dies(old_panel,i,j):
    num_bugs = 0
    for adj in [(0,1),(0,-1),(1,0),(-1,0)]:
        new_i = i + adj[0]
        new_j = j + adj[1]
        if new_i < 0 or new_i > 4 or new_j < 0 or new_j > 4:
            continue
        else:
            if old_panel[new_i][new_j] == "#":
                num_bugs += 1
    if num_bugs == 1:
        return "#"
    else:
        return "."

def becomes_infested(old_panel,i,j):
    num_bugs = 0
    for adj in [(0,1),(0,-1),(1,0),(-1,0)]:
        new_i = i + adj[0]
        new_j = j + adj[1]
        if new_i < 0 or new_i > 4 or new_j < 0 or new_j > 4:
            continue
        else:
            if old_panel[new_i][new_j] == "#":
                num_bugs += 1
    if num_bugs == 1 or num_bugs == 2:
        return "#"
    else:
        return "."

s = "#....#...###.##....##.##."
old_panel = []
for i in range(5):
    old_panel.append(list(s[5*i:5*(i+1)]))
all_states = []
all_states.append(old_panel[:])
stop = False

count = 0
while not stop:
    if count % 50 == 0:
        print(count)
    new_panel = [[None for _ in range(5)] for _ in range(5)]
    for i in range(5):
        for j in range(5):
            if old_panel[i][j] == "#":
                new_panel[i][j] = bug_dies(old_panel,i,j)
            elif old_panel[i][j] == ".":
                new_panel[i][j] = becomes_infested(old_panel,i,j)

    old_panel = new_panel
    for state in all_states:
        if new_panel == state:
            stop = True
    all_states.append(new_panel[:])
    count += 1

biodev = 0
for i in range(5):
    for j in range(5):
        if new_panel[i][j] == "#":
            biodev += 2**(5*i + j)

print(biodev)
