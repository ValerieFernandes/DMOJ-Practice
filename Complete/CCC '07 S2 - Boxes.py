import sys
import operator
 
def main():

    data = sys.stdin.read().split('\n')
    available = int(data[0])
    choice = []

    for x in range (available):
        box = data[x + 1].split()
        box[0] = int(box[0])
        box[1] = int(box[1])
        box[2] = int(box[2])
        box.sort()
        box.append(box[0]*box[1]*box[2])
        choice.append(box)

    #print(choice)
    choice = sorted(choice, key=operator.itemgetter(3))
    #print(choice)

    newitem = int(data[x + 2])
    
    #print(newitem)
    
    for count in range(newitem):
        item = data[available + 2 + count].split()
        item[0] = int(item[0])
        item[1] = int(item[1])
        item[2] = int(item[2])
        item.sort()
        #print(item)

        boxNum = -1

        for x in range(available):

            #print(item)
            #print(choice)
    
            if  item[0] <= choice[x][0]:
                #print('a')
                if item[1] <= choice[x][1]:
                    #print('b')
                    if item[2] <= choice[x][2]:
                        #print('c')
                        boxNum = x
                        break

        if boxNum == -1:
            print('Item does not fit.')
        else:
            print(choice[boxNum][3])
                
        
main()
