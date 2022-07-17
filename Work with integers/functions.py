#function
a,b = int(input()), int(input())
c = 3*(a+b)**3+275*b**2-127*a-41
print(c)

#example
a = int(input())
b = a+1
c = a-1
print('Next in number' , a , 'is:' , b)
print('For a number', a , 'previous number:' , c )

#example1
monitor,computer,keyboard,mouse = int(input()), int(input()), int(input()), int(input())
coast = (monitor+computer+keyboard+mouse)*3
print(coast)

#example2
a = int(input())
b = int(input())
f = a + b
g = a - b
h = a * b
print(a ,'+', b ,'=', f)
print(a ,'-', b ,'=', g)
print(a ,'*', b ,'=', h)

#example3
a1,d,n = int(input()), int(input()), int(input())
g = a1+d*(n-1)
print(g)

#example4
x = int(input())
print(x, x*2, x*3, x*4, x*5, sep ='---')

#example5
b1 = int(input())
q = int(input())
n = int(input())
f = b1*q**(n-1)
print(f)

#example6
a = int(input())
b = (a // 100)
print(b)

#example7
n = int(input())
k = int(input())
d = (k // n)
f = (k % n)
print(d)
print(f)

#exmaple8
n = int(input())
print(n // 2 + n % 2)

#example9
n = int(input())
k = -n // 4
print(-k)


#example10
h = int(input())
d = (h // 60)
a = (h % 60)
print(h, 'min - it', d, 'hours', a, 'minutes.')

#example11
num = int(input())
a = num % 10
b = (num % 100) // 10
c = num // 100
print('Сумма цифр =', a+b+c)
print('Произведение цифр =', a*b*c)

#example12
num = int(input())
a = num % 10
b = (num % 100) // 10
c = num // 100
print(c,b,a, sep ="")
print(c,a,b, sep ="")
print(b,c,a, sep ="")
print(b,a,c, sep ="")
print(a,c,b, sep ="")
print(a,b,c, sep ="")

#example13
num = int(input())
a = (num % 10**1) // 10**0
b = (num % 10**2) // 10**1
c = (num % 10**3) // 10**2
d = (num % 10**4) // 10**3
print('The digit in the thousands is equal', d)
print('The number in the hundreds position is equal', c)
print('The digit in the tens position is equal', b)
print('The digit in the units position is equal to', a)