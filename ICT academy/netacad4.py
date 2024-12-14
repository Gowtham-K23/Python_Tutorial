class A:
    pass
class B(A):
    pass
class C(B):
    pass
print(issubclass(A,C))


def o(p):
    def q():
        return '*' * p
    return q

r = o(1)
s = o(2)
print(r()+s())

print(float("1.3"))

import calendar
calendar.setfirstweekday(calendar.SUNDAY)
print(calendar.weekheader(3))

print(__name__)

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

from datetime import timedelta

delta = timedelta(weeks = 1, days = 7, hours = 11)
print(delta * 2)


x = "\\\\"
print(len(x))




class A:
    A = 1
    def __init__(self):
        self.a = 0

print(hasattr(A,'a'))


def fun(n):
    s = '+'
    for i in range(n):
        s += s
        yield s

for x in fun(2):
    print(x,end='')

try:
    raise Exception
except BaseException:
    print("a")
except Exception:
    print("b")
except:
    print("c")

import math
print(dir(math))


