hour, minute = map(int, input().split())
time = int(input())

minute = minute + time

if minute >= 60 :
    while minute >= 60 :
        hour += 1
        if hour == 24 :
            hour = 0
        minute -= 60
print(hour, minute)
    
