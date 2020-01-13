from operator import itemgetter
computers = int(input())

info = []
for x in range(computers):
    line = input().split()
    ram = int(line[1])
    cpu = int(line[2])
    diskDrive = int(line[3])
    num = 2 * ram + 3 * cpu + diskDrive
    info.append([line[0], num])

info.sort(key = itemgetter(1), reverse = True)
if computers == 1:
    print(info[0][0])  
elif computers >= 2:
    first = info.pop(0)
    second = info.pop(0)

    if first[1] != second[1]:
        print(first[0])
        print(second[0])
    else:
        if first[0][0] > second[0][0]:
            print(second[0])
            print(first[0])
        else:
            print(first[0])
            print(second[0])
