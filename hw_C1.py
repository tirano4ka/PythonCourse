a = [int(i) for i in input('Введите числа через пробел ').split()]
b=[]
for i in range(len(a)):
  if a[i] > a[i-1]:
    b.append(a[i])
print(b)
