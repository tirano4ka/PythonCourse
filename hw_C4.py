print('Введите коэффициенты для квадратного уравнения (ax^2 + bx + c = 0):')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
 
d = b*b - 4*a*c
 
if d > 0:
    x1 = (-b + math.sqrt(d))/(2*a)
    x2 = (-b - math.sqrt(d))/(2*a)
    print('Корни: х1={}, x2={}'.format(x1, x2))
elif d == 0:
    x = -b/(2*a)
    print('Корень равен {х}')
else:
    print('Нет действительных корней')
