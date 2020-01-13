def main():
    length = int(input())
    array = []

    total = 0
    for x in range(length):
        array.append(int(input()))


    for x in range(length):
        total += array[x]
    print(int(min((total - max(array)), (total/2))))
main()
