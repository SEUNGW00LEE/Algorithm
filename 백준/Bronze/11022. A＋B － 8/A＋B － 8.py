# 각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력한다. 테스트 케이스 번호는 1부터 시작한다.

t = int(input())

for i in range(1,t+1):
  a, b = map(int, input().split())
  print("Case #"+str(i)+":",str(a),"+",str(b),"=",a+b)
  
# Case #1: 1 + 1 = 2
# Case #2: 2 + 3 = 5
# Case #3: 3 + 4 = 7
# Case #4: 9 + 8 = 17
# Case #5: 5 + 2 = 7