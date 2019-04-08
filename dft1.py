import numpy as np
import matplotlib.pyplot as plt
x=[0,1,2,3,4,5]
def dft1(x):
N=1000
s=complex(0,-1)
a=[]
k=np.linspace(0,N,1000)
for i in range(0,n):
	sum=0
	for n in range(0,N):
		sum=sum+(x[n]*np.exp((-s*2*np.pi*k[i]*n/N))
	a.append(a,sum)
return x
x1=np.abs(a)
plt.subplot(1,3,2)
plt.plot(k,x1)
plt.xlabel('freq')
plt.ylabel('magnitude')
plt.title('magnitude spectrum')
x2=np.angle(a)
plt.subplot(1,3,3)
plt.plot(k,x2)
plt.xlabel('freq')