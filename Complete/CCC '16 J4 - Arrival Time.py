def main():
    depart = input()
    elapsed = 120
    hours = int(depart[:2])
    minutes = int(depart[3:])
    totalMin = 60 * hours + minutes
   
    if totalMin < 420 and elapsed > 0:
        timeLeft = 420 - totalMin
        if timeLeft >= 120:
            elapsed = 0
            totalMin = totalMin + 120
        else:
            elapsed = elapsed - timeLeft
            totalMin = totalMin + timeLeft
    
    if totalMin < 600 and elapsed > 0:
        timeLeft = 600 - totalMin
        if timeLeft >= 2 * elapsed:
            totalMin = totalMin + elapsed * 2
            elapsed = 0
        else:
            elapsed = int(elapsed - (timeLeft / 2))
            totalMin = totalMin + timeLeft
    
   
    if totalMin < 900 and elapsed > 0:
        timeLeft = 900 - totalMin
        if timeLeft >= elapsed:
            totalMin = totalMin + elapsed
            elapsed = 0
        else:
            elapsed = elapsed - timeLeft
            totalMin = totalMin + timeLeft
        
        
    if totalMin < 1140 and elapsed > 0:
        timeLeft = 1140 - totalMin
        if timeLeft >= 2 * elapsed:
            totalMin = totalMin + elapsed * 2
            elapsed = 0
        else:
            elapsed = int(elapsed - (timeLeft / 2))
            totalMin = totalMin + timeLeft
        

    if elapsed > 0:
        totalMin = totalMin + elapsed

    hours = totalMin // 60
    minutes = int(totalMin - (60 * hours))
    hours = int((hours + 24) % 24)
    if hours < 10:
        hours = '0' + str(hours)
    else:
        hours = str(hours)
    if minutes < 10:
        minutes = '0' + str(minutes)
    else:
        minutes = str(minutes)
    print(hours + ':' + minutes)
main()
        
    

