##def aWord(entry):
##    if entry == 'A':
##        return True
##
##    elif len(entry) >= 3 and entry[0] == 'B' and monkey(entry[1:-2]) and entry[-1] == 'S':
##        return True
##    else:
##        return False
##
##
##
##def monkey(entry):
##    if aWord(entry):
##        return True
##
##    else:
##        found = False
##        for x in range(2, len(entry)):
##            found = found or (aWord(entry) and entry[x] == 'N' and monkey(entry[x:]))
##    return found
##    
##def main():
##    
##    while True:
##        temp = input()
##        if temp == 'X':
##            break
##        if monkey(temp):
##            print('YES')
##        else:
##            print('NO')
##main()

def monkey(entry):


    while True:
        entry = entry.replace('ANA', 'A')
        entry = entry.replace('BAS', 'A')
        if ('ANA' not in entry) and ('BAS' not in entry):
            break


    if entry == 'A':
        return True
    else:
        return False


def main():
    
    while True:

        temp = input()

        if temp == 'X':
            break
        
        if monkey(temp):
            print('YES')
        else:
            print('NO')
            
main()

                    




























