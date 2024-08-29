x = int(input ('Digite um número: '))
y = int(input ('Digite outro número: '))
if x<y:
     x = x + 1
     while x < y:
          print(x)
          x = x + 1
else:
     y = y + 1
     while y < x:
          print(y)
          y = y + 1
