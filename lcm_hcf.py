x=int(input('Enter 1st number: '))
y=int(input('Enter 1st number: '))
cont=1
if x>y:
    bg=x
    sm=y
else:
    bg=y
    sm=x
k=bg
t=1


while t==1:
  if (k%bg==0)and(k%sm==0):
      t=0
  k+=1
    

hcf=(x*y)/(k-1)
print('lcm: ',k-1)
print('hcf: ',hcf)
