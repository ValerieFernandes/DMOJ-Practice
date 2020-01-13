maxWeight = int(input())
cars = int(input())
weights = [0, 0, 0]
last = True
for x in range(cars):
    weights.append(int(input()))

for x in range(3, cars + 3):
    if weights[x] + weights[x - 1] + weights[x - 2] + weights[x - 3] > maxWeight:
        last = False
        break
if last:
    print(x - 2)
else:
    print(x - 3)
