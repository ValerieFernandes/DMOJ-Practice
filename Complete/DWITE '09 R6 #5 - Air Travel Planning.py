def main():
    for x in range(5):
       flights = int(input())
       dest = dict.fromkeys(['YYZ', 'SEA'])
       dest['YYZ'] = 1
       dest['SEA'] = 2
       dist = [0, float("inf")]
       visit = set()
       edges = [[], [], []]
       for x in range(flights):
           current = input().split()
           current[2] = int(current[2])
           if current[0] not in dest:
               dist.append(float("inf"))
               dest[current[0]] = len(dist)
               edges.append([])
           
           if current[1] not in dest:
               dist.append(float("inf"))
               dest[current[1]] = len(dist)
               edges.append([])
           current[0] = dest[current[0]]
           current[1] = dest[current[1]]
           
           edges[current[0]].append([current[1], current[2]])
    
       places = len(dist)

       while True:
            minNode = None
            for x in range(1, places + 1):     
              if x not in visit:
                  if minNode == None:
                      minNode = x
                  elif dist[x - 1] <= dist[minNode - 1]:
                      minNode = x
            visit.add(minNode)
            if minNode == 2:
                break
            else:
                for x in range(len(edges[minNode])):
                    current = edges[minNode][x][0]
                    newDist = dist[minNode - 1] + edges[minNode][x][1]
                    if newDist < dist[current - 1]:
                        dist[current - 1] = newDist        
       print(dist[1])          
            
       
main()
