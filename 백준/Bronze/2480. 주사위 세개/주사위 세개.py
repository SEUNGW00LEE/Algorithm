a, b, c = map(int, input().split())
award = 0

if a == b == c :
  award = 10000 + a*1000
elif a == b :
  award = 1000 + 100 * a
elif b == c :
  award = 1000 + 100 * b
elif a == c :
  award = 1000 + 100 * a
else : 
  award = 100 * max(a, b, c)
  
print(award)