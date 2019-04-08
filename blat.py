import numpy as np
import matplotlib.pyplot as plt
m=int(input("enter value="))
l=[]
for n in range(0,m-1):
	d=np.cos(2*np.pi*n/(m-1))
	e=np.cos(4*np.pi*n/(m-1))
	t=np.abs(0.4-0.5*d-0.08*e)
	l=np.append(l,t)

plt.stem(l)
plt.xlabel("frequency(w/pi)")
plt.ylabel("magnitude")
plt.title("blateman")
plt.show()
