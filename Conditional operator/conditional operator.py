# if-else
answer = input('What programming language are we learning?')
if answer == 'Python':
    print('Right! We use Python =)')
    print('Python - is a great language!')
else:
    print('Not certainly in that way!')

# example1
a = input()
b = input()
if a == b:
    print('Password match')
else:
    print('Password does not match')
    
# example2
numb = int(input())
if numb % 2 == 0:
    print('Even')
else:
    print('Uneven')
    
# example3
num = int(input())
d = (num % 10**4) // 10**3
c = (num % 10**3) // 10**2
b = (num % 10**2) // 10**1
a = (num % 10**1) // 10**0
if d + a == c - b:
    print('YES')
else:
    print('NO')
    
# example4
age = int(input())
if age >= 18:
    print('Access is allowed')
else:
    print('Access is denied')

# example 5
a = int(input())
b = int(input())
c = int(input())
if (b - a) + b == c:
    print('YES')
else:
    print('NO')

# example 6
a = int(input())
b = int(input())
if a < b > a:
    print(a)
else:
    print(b)

# example 7
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if b > a < c:
    if d > a:
        print(a)
if a >= b < c:
    if d > b:
        print(b)
if a > c <= b:
    if d > c:
        print(c)
if a > d < b:
    if c >= d:
        print(d)
        
#example 8
