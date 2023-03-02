A=int(input())
B=int(input())

print(A *(B % 10))

print(A *((B // 10) % 10))

print(A *(B // 100))

print(A * B)
#d = B // 100
#e = (B % 100) // 10
#f = B % 10 

# A * d = (3)
# A * e = (4)
# A * f = (5)
# A * B = (6)

