import numpy as np
import matplotlib.pyplot as plt
m=int(input("enter value="))
h=[]
for n in range(0,m-1):
	x=1
	h=np.append(h,x)
i=[]
for n in range(0,m-1):
	a=np.abs(n-(m-1)/2)
	y=(1-(2*a)/(m-1))
	i=np.append(i,y)
j=[]
for n in range(0,m-1):
	b=np.cos(2*np.pi*n/(m-1))
	z=np.abs(0.5-0.5*b)
	j=np.append(j,z)
k=[]
for n in range(0,m-1):
	c=np.cos(2*np.pi*n/(m-1))
	r=np.abs(0.54-0.46*c)
	k=np.append(k,r)
l=[]
for n in range(0,m-1):
	d=np.cos(2*np.pi*n/(m-1))
	e=np.cos(4*np.pi*n/(m-1))
	t=np.abs(0.4-0.5*d-0.08*e)
	l=np.append(l,t)
plt.subplot(5,1,1)
plt.plot(h)
plt.xlabel("frequency(w/pi)")
plt.ylabel("magnitude")
plt.title("rectangular")
plt.subplot(5,1,2)
plt.stem(i)
plt.xlabel("frequency(w/pi)")
plt.ylabel("magnitude")
plt.title("triangular")
plt.subplot(5,1,3)
plt.stem(j)
plt.xlabel("frequency(w/pi)")
plt.ylabel("magnitude")
plt.title("hanning")
plt.subplot(5,1,4)
plt.stem(k)
plt.xlabel("frequency(w/pi)")
plt.ylabel("magnitude")
plt.title("hamming")
plt.subplot(5,1,5)
plt.stem(l)
plt.xlabel("frequency(w/pi)")
plt.ylabel("magnitude")
plt.title("blateman")
plt.show()
