#!/usr/bin/env python
# -*- coding: utf-8 -*-
s = 'hi hello, world.'

b = list(s)
# print('b=',b)

# to remove , and . (nutzlich mit Worter, die mit /def/ anfangen, damit g nicht , oder . sein)
a = s.split(' ')
# print('a=',a)

c = ' '.join(a)
# print(c)

# for i in a:
#     if (i.endswith(',')) or (i.endswith('.')):
#         a[a.index(i)] = i[:len(i)-1]
# print('a=',a)


# Analyse:
s = 'Noch wird \abc nicht veraendert. Aber jetzt kommt eine Makrodefinition \def\abc?abcA\?B\?Cabc?, die dann hier \abc zu einer Textersetzung f�hrt.'
# ss = s.encode(encoding='UTF-8', errors='strict')
# ss = s.decode('utf8')

print(s)

# a = s.split(' ')
# for i in a:
# #     if(i.startswith('\def\\')):
# #     if(i[1:4]=='def'):
#     print(i)
print('\def\\') 
        