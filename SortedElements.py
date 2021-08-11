print("Enter the input")
n=input()
c=[]
z=set(n)
z=list(z)
print("Sorted elments are as follow:")
for i in range(len(z)):
  co=0
  for m in range(len(n)):
    if n[m]==z[i]:
      co = co+1
  print(str(z[i])+"="+str(co))
