import queue
def tangled(entry, one, two):
   current = queue.Queue()
   visit = set()
   current.put(one)
   visit.add(one)
   found = False
   while current.qsize() > 0:
       knot = current.get()
       for x in range(len(entry[knot])):
           if entry[knot][x] == two:
               found = True
               break
           if entry[knot][x] not in visit:
               visit.add(entry[knot][x])
               current.put(entry[knot][x])
       if found == True:
           break
   if found == True:
       return 'Tangled'
   else:
       return 'Not Tangled'
               
           
   
def main():
   connections = int(input())
   strings = [[] for x in range(connections + 1)]
   for x in range(connections):
       temp = input().split()
       y = int(temp[0])
       z = int(temp[1])
       strings[y].append(z)
   last = input().split()
   one = int(last[0])
   two = int(last[1])
   print(tangled(strings, one, two))
main()
