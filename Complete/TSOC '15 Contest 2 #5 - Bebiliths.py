import operator
def main():
    speed = int(input())
    bebilith = int(input())
    fastBeb = []
    slowBeb = []

    for x in range(bebilith):
        temp = input().split()
        temp[0] = int(temp[0])
        temp[1] = int(temp[1])
        temp[2] = int(temp[2])
        temp.append(x + 1)
        if temp[0] >= speed:
            fastBeb.append(temp)
        else:
            slowBeb.append(temp)
    
    fastBeb = sorted(fastBeb, key=operator.itemgetter(0, 2))
    slowBeb = sorted(slowBeb, key=operator.itemgetter(0, 1))
##    print(fastBeb)
##    print(slowBeb)

    report = int(input())
    fastLen = len(fastBeb)

    for x in range(report):
        dangerous = int(input())
        if dangerous > fastLen:
            dangerous -= fastLen
            print(slowBeb[dangerous * -1][3])
        else:
            print(fastBeb[dangerous * -1][3])

main()
