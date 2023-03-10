
total = int(input())
t = int(input())
sum = 0
for _ in range(t):
  price, quantity = map(int, input().split())
  sum += price * quantity

if total == sum  :
  print("Yes")
else :
  print("No")