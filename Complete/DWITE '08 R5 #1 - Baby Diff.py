def main():
    for x in range(5):
        first = input()
        second = input()
        same = 0
        small = min(len(first), len(second))
        for x in range(small):
            if first[x] == second[x]:
                same += 1
            else:
                break
        print(same)
main()
