a,b,c = 10,20,30
print(max(a,b,c),"is the greatest number")

def fun(a):

    b = a / (a-3)
    print(b)

a = int(input())

try:
    fun(a)
    print("Executed successfully")
except:
    print("Exception occurs")

for i in range(5):
    print(i,end=" ");

name='kerala'
for i in range(len(name)+1):
    print(name[:i])

from colorama import Fore, Back, Style
print(Fore.YELLOW + "SOme Red text")
print(Back.GREEN + "And Green background")
