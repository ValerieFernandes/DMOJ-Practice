def main():
    prices = input().split()
    a = int(prices[0])
    b = int(prices[1])
    c = int(prices[2])
    
    time = [0 for x in range(101)]
    
    truckOne = input().split()
    truckTwo = input().split()
    truckThree = input().split()
    
    arriveOne = int(truckOne[0])
    departOne = int(truckOne[1])
    arriveTwo = int(truckTwo[0])
    departTwo = int(truckTwo[1])
    arriveThree = int(truckThree[0])
    departThree = int(truckThree[1])
    
    for x in range(arriveOne, departOne):
        time[x] += 1

    for x in range(arriveTwo, departTwo):
        time[x] += 1
        
    for x in range(arriveThree, departThree):
        time[x] += 1

    total = 0
    for item in time:
        if item == 1:
            total += a
        if item == 2:
            total += b * 2
        if item == 3:
            total += c * 3
    print(total)
main()
            
