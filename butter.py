import numpy as np
import matplotlib.pyplot as plt
p=float(input("enter the dp value="))
s=float(input("enter the ds value="))
wp=float(input("enter the wp value="))
ws=float(input("enter the ws value="))
x=float((1/(p**2))-1)
y=float((1/(s**2))-1)
print("value of(float(1/(p**2))-1) =", x)       
z=wp/ws
a=np.log(x/y)
n=(1/2)*(a/np.log(z))
print ("value of n =",n)
wc=wp/(x**(1/(2*n)))
print ("cutoff frequency value =",wc)
w=np.arange(0,1000,1)
M=(1/np.sqrt(1+((w/wc)**(2*n))))
plt.plot(w,M)
plt.show()


