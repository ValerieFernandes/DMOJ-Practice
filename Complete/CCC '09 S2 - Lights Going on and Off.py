
def main():
    rows = int(input())
    lights = int(input())
    grid = []
    choices = [[] for a in range(rows)]
    for x in range(rows):
        line = input().split()
        line = [int(x) for x in line]
        choices[x].append(line)
        
    for x in range(rows - 1):
        for x2 in range(len(choices[x])):
            new = []
            for x3 in range(lights):
                if choices [x][x2][x3] != choices[x + 1][0][x3]:
                    new.append(1)
                else:
                    new.append(0)
            choices[x + 1].append(new)
        choices[x + 1] = set(tuple(i) for i in choices[x + 1])
        choices[x + 1] = list(choices[x + 1])

    print(len(choices[rows - 1]))
        
main()  
    


