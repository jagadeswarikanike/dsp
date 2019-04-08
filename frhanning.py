import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
m=int(input("enter value="))
k=int(input("enter number of samples for x[n]:"))
r=[]
for n in range(0,m-1):
	b=np.cos(2*np.pi*n/(m-1))
	z=np.abs(0.5-0.5*b)
	r=np.append(r,z)
N=1000
j=cm.sqrt(-1)
X=[]
w=np.linspace(-np.pi,np.pi,N)
for i in range(0,N):
	s=0
	for n in range(0,len(r)):
		s=s+(r[n]*np.exp(-n*w[i]*j))
	X.append(s)
print("X[n]=",np.abs(X))
plt.plot(w,np.abs(X))
plt.xlabel("freq(w/pi)")
plt.ylabel("magnitude")
plt.title("magnitude spectrum")
plt.show()
