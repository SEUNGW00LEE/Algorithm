year = int(input())
result = 0

if year % 4 == 0 :
    if year % 100 != 0 :
        result = 1
    elif year % 400 == 0:
        result = 1
    else :
        result = 0
else :
    result = 0
print(result)

    