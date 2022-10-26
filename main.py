#z1
for i in range(31):
  print(i, end=" ")
#z2
for i in range(1, 10, 2):
  print(i*i, end=" ")
#z3
for i in range(1137, 10000, 379):
  print(i, end=" ")
#z4
for i in range(100, 1000):
  if i%5==0 or i % 6==0 or i % 11==0:
    print(i, end=" ")
#z5
n = int(input())
suma = 0
for i in range(0, n):
  suma += int(input())
print(suma)
#z6
k = int(input())
suma = 0
for i in range(0, 2*k, 2):
  suma+=i
print(suma)
#z7
m = int(input())
suma = 0
for i in range(11, 2*m+11, 2):
  suma+=i
print(suma)
#z8
W0 = int(input("W0: "))
L = float(input("L: "))
wartosc = W0
for i in range(0, int(2 * L), 1):
  for j in range(6):
    wartosc = wartosc * 1.06
print(wartosc)
#z9
n = int(input())
suma = 0
for i in range(21, n*100+21, 100):
  suma+=i
print(suma)
#z10
for i in range(1, 32):
  a = i*i
  if i<10:
    while a>=10:
      a -= 10
  else:
    while a>=100:
      a -= 100
  if i==a:
    print(i*i)