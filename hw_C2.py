n = input()
mult = 1
summa = 0
for i in n:
  summa += int(i)
  if int(i) != 0:
    mult *= int(i)
 
print("Сумма цифр:", summa)
print("Произведение значащих цифр:", mult)
