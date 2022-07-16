#example
print('a', 'b', 'c')
print('d', 'e', 'f')
      
#example1
print('a', 'b', 'c', sep='*')
print('d', 'e', 'f', sep='**')

#example2
print('a', 'b', 'c', end='@')
print('d', 'e', 'f', end='@@')

#example3
print('a', 'b', 'c', end='@')
print('d', 'e', 'f', end='@@')

#example4
print('a', 'b', 'c', sep='*', end='finish')
print('d', 'e', 'f', sep='**', end='^__^')
print('g', 'h', 'i', sep='+', end='%')
print('j', 'k', 'l', sep='-', end='#')
print('m', 'n', 'o', sep='/', end='!')

sep=' '   # пробел
end='\n'  # перевод строки

print('31', '12', '2019', sep='-')
31-12-2019

#example5
print('Mercury', 'Venus', sep='*', end='!')
print('Mars', 'Jupiter', sep='**', end='?')
Mercurt*Venus!Mars**Jupiter?

#example6
print('a', 'b', 'c', sep='*')
print('d', 'e', 'f', sep='**', end='')
print('g', 'h', 'i', sep='+', end='%')
print('j', 'k', 'l', sep='-', end='\n')
print('m', 'n', 'o', sep='/', end='!')
print('p', 'q', 'r', sep='1', end='%')
print('s', 't', 'u', sep='&', end='\n')
print('v', 'w', 'x', sep='%')
print('y', 'z', sep='/', end='!')

print('I', 'Like', 'Python', sep='***')

#example7
star = input()
one = input()
two = input()
three = input()
print(one,two,three, sep='*')

#example8
star,one,two,three = input()
print(one,two,three, sep='*')

#example9
s = input()
one = input()
two = input()
three = input()
print(one,two,three, sep=s)

#example10
name = input()
print ('Привет,' , name, end='!')