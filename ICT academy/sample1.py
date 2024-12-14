s = "##$$%^%go890-k23%$3#"
l = list(s)

for i in l:
    
    i1 = ord(i)
    if (i1>=65 and i1<=90 or i1>=97 and i1<=122):
        print(str(i),end="")

print("\n")
dno = '23A'
street = 'gandhi st'
nagar = 'nehru nagar'
city = 'dindigul'
addr = ','.join([dno,street,nagar,city])
print(addr)


today = '12-03-2024'
print(today.split('-',1))
