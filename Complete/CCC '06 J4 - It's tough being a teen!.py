import queue
def schedule(entry):
    done = set()
    order = ''
    visit = queue.Queue()
    count = 0
    for x in range(1, 8):
        if entry[x] == []:
            visit.put(x)
            done.add(x)
            order += str(x) + ' '
            break
 
    while visit.qsize() > 0:
        temp = visit.get()
        for x in range(1, 8):
            if temp in entry[x]:
                entry[x].remove(temp)

        for x in range(1, 8):
            if entry[x] == [] and x not in done:
                visit.put(x)
                done.add(x)
                order += str(x) + ' '
                break
            
                
            
    if len(order) != 14:

        return 'Cannot complete these tasks. Going to bed.'
    else:
        return order[:-1]
            
            
        
        
def main():
    order = [[0], [2], [], [], [1, 3], [3], [], [1]]
    while True:
        before = int(input())
        after = int(input())
        if before == 0:
            break
        order[after].append(before)

    print(schedule(order))
        



    
main()
