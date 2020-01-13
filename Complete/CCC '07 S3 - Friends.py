import queue
def circle(pairs, x, y):
    distance = [-1 for x in range(10000)]
    current = queue.Queue()
    current.put(x)

    while current.qsize() > 0:
        temp = current.get()
        for x2 in range(len(pairs[temp])):
            if pairs[temp][x2] == y:
                return 'Yes', distance[temp] + 1
            
            elif distance[pairs[temp][x2]] == -1:
                current.put(pairs[temp][x2])
                distance[pairs[temp][x2]] = distance[temp] + 1
    return 'No'

def main():
    students = int(input())
    pairs = [[] for x in range(10000)]
 
    for x in range(students):
        temp = input().split()
        v = int(temp[0])
        y = int(temp[1])
        pairs[v].append(y)

    while True:
        line = input().split()
        x = int(line[0])
        y = int(line[1])
        if x == 0:
            break
        else:
            result = circle(pairs, x, y)

            if result == 'No':
                print('No')
            else:
                print(result[0], result[1])
main()
