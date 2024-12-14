import math
res = math.e != math.pow(2,4)
print(int(res))


print(ord('c') - ord('a'))

x = '\''
print(len(x))

try:
    print("5"/0)
except ArithmeticError:
    print("A")
except ZeroDivisionError:
    print("B")
except:
    print("C")
    
print('Mike' > 'Mikey')

print(3 * 'abc' + 'xyz')

print(chr(ord('z') - 2))

class A:
    def __str__(self):
        return 'a'

class B(A):
    def __str__(self):
        return 'b'

class C(B):
    pass

o =C()
print(o)



class A:
    X = 0
    def __init__(self,v=0):
        self.Y = v
        A.X += v

a = A()
b = A(1)
c = A(2)

print(c.X)

def f(x):
    try:
        x = x/x
    except:
        print("a",end = '')
    else:
        print("b",end = '')
    finally:
        print("c",end = '')

f(1)
f(0)


class A:
    pass
class B(A):
    pass
class C(B):
    pass
print(issubclass(C,A))

class A:
    def a(self):
        print('a')

class B:
    def a(self):
        print('b')

class C(B,A):
    def c(self):
        self.a()

o = C()
o.c()


class A:
    def __str__(self):
        return 'a'

class B:
    def __str__(self):
        return 'b'

class C(A, B):
    pass
o = C()
print(o)


class I:
    def __init__(self):
        self.s = 'abc'
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == len(self.s):
            raise StopIteration
        V = self.s[self.i]
        self.i += 1
        return V

for x in I():
    print(x,end='')

print("\n")
try:
    raise Exception(1,2,3)
except Exception as e:
    print(len(e.args))



class Ex(Exception):
    def __init__(self,msg):
        Exception.__init__(self,msg + msg)
        self.args = (msg,)

try:
    raise Ex('ex')
except Ex as e:
    print(e)
except Exception as e:
    print(e)

class A:
    A = 1
print(hasattr(A,'A'))


class A:
    def __init__(self,v=1):
        self.v = v

    def set(self,v):
        self.v = v
        return v

a = A()
print(a.set(a.v + 1))

import calendar
print(calendar.weekheader(2))

def func(n):
    s = '+'
    for i in range(n):
        s += s
        yield s
for x in func(2):
    print(x, end = '')


import calendar
c = calendar.Calendar()
for weekday in c.iterweekdays():
    print(weekday,end = "")

def o(p):
    def q():
        return '*' * p
    return q

r = o(1)
s = o(2)
print(r() + s())

b = bytearray(3)
print(b)

from datetime import date

date_1 = date(1992,1,16)
date_2 = date(1991,2,5)
print(date_1 - date_2)

from datetime import datetime

datetime = datetime(2019,11,27,11,27,22)
print(datetime.strftime('%y/%B/%d %H:%M:%S'))

def f():
    s = 'abcdef'
    for c in s[::2]:
        yield c

for x in I():
    print(x, end='')

import os
os.mkdir('thumbnails')
os.chdir('thumbnails')

sizes = ['small', 'medium', 'large']

for size in sizes:
    os.mkdir(size)
print(os.listdir())
