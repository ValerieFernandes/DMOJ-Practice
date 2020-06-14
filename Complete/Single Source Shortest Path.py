#Solution for https://dmoj.ca/problem/sssp
def main():
    line = input().split()
    vertices = int(line[0])
    edgeNum = int(line[1])
    adj = [[] for x in range(vertices + 1)]
    dist = [0]
    visit = set()
    for x in range(vertices - 1):
        dist.append(float("inf"))
    for x in range(edgeNum):
        edge = input().split()
        edge = [int(x) for x in edge]
        adj[edge[0]].append([edge[1], edge[2]])
        adj[edge[1]].append([edge[0], edge[2]])
    
    for x2 in range(vertices):
        minNode = None
        for x in range(1, vertices + 1):     
          if x not in visit:
                if minNode == None:
                    minNode = x
                elif dist[x - 1] <= dist[minNode - 1]:
                    minNode = x
        visit.add(minNode)
 
        for x in range(len(adj[minNode])):
            current = adj[minNode][x][0]
            newDist = dist[minNode - 1] + adj[minNode][x][1]
            if newDist < dist[current - 1]:
                dist[current - 1] = newDist        
    for x in range(vertices):
        if dist[x] == float("inf"):
            print(-1)
        else:
            print(dist[x])
main()
