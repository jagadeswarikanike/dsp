import numpy as np
import matplotlib.pyplot as plt
p=float(input("enter the dp value="))
s=float(input("enter the ds value="))
wp=float(input("enter the wp value="))
ws=float(input("enter the ws value="))
t=input("enter the w value=")
x=float((1/(p**2))-1)
y=float((1/(s**2))-1)
print("value of(float(1/(p**2))-1) =", x)       
z=wp/ws
a=np.log(x/y)
n=round((1/2)*(a/np.log(z)))
print ("value of n =",n)
wc=wp/(x**(1/(2*n)))
print ("cutoff frequency value =",wc)
w=np.arange(-np.pi,np.pi,(np.pi/10))
o=complex(0,1)
s1=(o*w)/t
s2=(o*2*np.tan(w/2))/t
if (n/2==0):
	sum=0
	for k in range(1,(n/2))
		sum=sum+(2*np.sin((2*k)-1)*np.pi)/(2*n))
	b.append(sum)
y=b
print(y)
end
		

