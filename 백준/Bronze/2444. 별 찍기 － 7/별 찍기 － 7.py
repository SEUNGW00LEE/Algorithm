count  = int(input())

s = count 

for i in range(1,count+1):
  print(" " * (count-i) + "*" * (i * 2 - 1))
  i += 1

for t in range(1,count):
  print(" " * t + "*" * (s * 2 - 3))
  s -= 1