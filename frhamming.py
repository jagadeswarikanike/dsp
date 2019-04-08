import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
m=int(input("enter value="))
k=int(input("enter number of samples for x[n]:"))
a=[]
for n in range(0,m-1):
	c=np.cos(2*np.pi*n/(m-1))
	r=np.abs(0.54-0.5*c)
	a=np.append(a,r)
N=1000
j=cm.sqrt(-1)
X=[]
w=np.linspace(-np.pi,np.pi,N)
for i in range(0,N):
	s=0
	for n in range(0,len(a)):
		s=s+(a[n]*np.exp(-n*w[i]*j))
	X.append(s)
print("X[n]=",np.abs(X))
plt.plot(w,np.abs(X))
plt.xlabel("freq(w/pi)")
plt.ylabel("magnitude")
plt.title("magnitude spectrum")
plt.show()
