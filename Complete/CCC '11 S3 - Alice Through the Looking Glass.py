
def is_crystal(m,x):
    if m >= 1:
        exponent = 5 ** (m-1)
        placement = x // exponent
        if placement == 0 or placement == 4:
            return 0
        elif placement == 1 or placement == 3:
            return exponent + is_crystal(m - 1, x % exponent)
        elif placement == 2:
            return 2 * exponent + is_crystal(m - 1, x % exponent)
        return maxheightatx
    return 0

import sys
def main():

    data = sys.stdin.read().split('\n')
    test = int(data[0])
    coord = []
    for x in range(test):
        case = data[x + 1].split()
        case[0] = int(case[0])
        case[1] = int(case[1])
        case[2] = int(case[2])

        if case[2] < is_crystal(case[0], case[1]):
            print('crystal')
        else:
            print('empty')
        
main()
