t = [[3-i for i in range(3)] for j in range (3)]
s = 0
for i in range(3):
    s+= t[i][i]
print(s)

my = [3,1,-2]

print(my[my[-1]])

vals = [0,1,2]
vals[0],vals[2] = vals[2],vals[0]
print(vals)

my = [1,2,3]
for v in range(len(my)):
    my.insert(1,my[v])
print(my)

my = [1,2,3]
my2 = []
for v in my:
    my2.insert(0,v)
print(my2)

var = 1
while var < 10:
    print("#")
    var = var << 1

nums = [1,2,3]
vals = nums
del vals[1:2]
print(vals)



my = [i for i in range(-1,2)]
print(my)

a = 1
b = 0
c = a & b
d = a | b
e = a ^ b
print(c+d+e)

vals = [0,1,2]
vals.insert(0, 1)
del vals[1]
print(vals)

m = [1,2,3,4]
print(m[-3:-2])

print(0 + 2 * 3 + 3 * 1)

tup = (1,2,4,8)
tup = tup[1:-1]
tup = tup[0]
print(tup)

def fun(x):
    global y
    y = x * x
    return y
fun(2)
print(y)

m = [1,2,3,4,5]
def fun(m):
    del m[3]
    m[3] = 10

print(m)

dict1 = {'one':'two', 'three':'one', 'two':'three'}
v = dict1['one']

for k in range(len(dict1)):
    v = dict1[v]
print(v)


dict1 = {}
my = ['a','b','c','d']
for i in range(len(my) - 1):
    dict1[my[i]] = (my[i], )
for i in sorted(dict1.keys()):
    k = dict1[i]
    print(k[0])

def f1(a):
    return a**a
def f2(a):
    return f1(a) * f1(a)
print(f2(2))

def any():
    print(var + 1, end = '')
var = 1
any()
print(var)



my = ['Mary','had','a','little','lamb']

def func(my):
    del my[3]
    my[3] = 'ram'

print(my)


def fu(inp=2 ,out=3):
    return inp * out
print(fu(out=2))

def fun():
    a = 1
    print(a)
fun()
