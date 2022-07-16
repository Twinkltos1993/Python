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