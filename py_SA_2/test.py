s = 'hi hello, world.'

b = list(s)
print('b=',b)

# to remove , and . 
a = s.split(' ')
print('a=',a)
for i in a:
    if (i.endswith(',')) or (i.endswith('.')):
        a[a.index(i)] = i[:len(i)-1]
print('a=',a)