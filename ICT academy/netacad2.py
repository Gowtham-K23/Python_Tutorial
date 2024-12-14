
my = [1,2]
for v in range(2):
    my.insert(-1,my[v])
print(my)

print(1//5+1/5)

tup = (1,2,4,8)
tup = tup[-2:-1]
tup = tup[-1]
print(tup)

print("a","b","c",sep="sep")

my = [x*x for x in range(5)]
def fun(lst):
    del lst[lst[2]]
    return lst
print(fun(my))

y = input()
x = input()
print(x + y)


def func(x,y):
    if x==y:
        return x
    else:
        return func(x,y-1)

print(func(0,3))

x = 3
y = 2
x = x % y
x = x % y
y = y % x
print(y)


x = 1
y = 0
x = x ^ y
y = x ^ y
x = x ^ y
print(x, y)

dct = {}
dct['1'] = (1,2)
dct['2'] = (2,1)


dict1 = {'one':'two', 'three':'one', 'two':'three'}
v = dict1['three']

for k in range(len(dict1)):
    v = dict1[v]
print(v)

nums = [1,2,3]
vals = nums
del vals[:]
print(vals)

ls = [i for i in range(-1,-2)]
print(ls)

x = float(input())
y = float(input())
print(y ** (1/x))

def fun(x):
    if x%2 == 0:
        return 1
    else:
        return 2
print(fun(fun(2)))


x = 1
y = 2
x,y,z = x,x,y
z,y,z = x,y,z
print(x,y,z)

i = 0
while i<i+2:
    i+=1
    print("*")
else:
    print("*")
