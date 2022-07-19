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
age = int(input())
if age <= 13:
    print('childhood')
if 14 <= age <= 24:
    print('youth')
if 25 <= age <= 59:
    print('maturity')
if age >= 60:
    print('age')

# example 9
a = int(input())
b = int(input())
c = int(input())
sum = 0
if a > sum < b and c > sum:
    print(a+b+c)
elif a < sum < b and c > sum:
    print(b+c)
elif a > sum > b and c > sum:
    print(a+c)
elif a > sum < b and c < sum:
    print(a+b)
elif a > sum > b and c < sum:
    print(a)
elif a < sum < b and c < sum:
    print(b)
elif a < sum > b and c > sum:
    print(c)
elif a < sum > b and c < sum:
    print(sum)
    
# example 10
x = int(input())
if -1 < x < 17:
    print('True')
else:
    print('False')

# example 11
x = int(input())
if x <= -3 or x >= 7:
    print("True")
else:
    print("False")
    
# example 12
x = int(input())
if -2 >= x > -30 or 7 < x <= 25:
    print('True')
else:
    print('False')

# example 13
a = int(input())
if a >= 1000 and a <= 9999 and (a % 7 == 0 or a % 17 == 0):
    print('YES')
else:
    print("NO")

# example14
a = int(input())
b = int(input())
c = int(input())
if a + b > c and a + c > b and b + c > a:
    print('YES')
else:
    print('NO')
    
# example15
a = int(input())
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('YES')
else:
    print('NO')