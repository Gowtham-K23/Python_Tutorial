num = [12,-25,36,-48,70,-88]
def mydata(n):
  if n>0:
    return True
  else:
    return False

  z = [x for x in filter(mydata,num)]
  print(z)
