import numpy as np
import matplotlib.pyplot as plt
m=int(input("enter value="))
k=[]
for n in range(0,m-1):
	c=np.cos(2*np.pi*n/(m-1))
	r=np.abs(0.54-0.5*c)
	k=np.append(k,r)

plt.stem(k)
plt.xlabel("frequency(w/pi)")
plt.ylabel("magnitude")
plt.title("hamming")
plt.show()
