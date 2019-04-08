import numpy as np
import matplotlib.pyplot as plt
m=int(input("enter value="))
j=[]
for n in range(0,m-1):
	b=np.cos(2*np.pi*n/(m-1))
	z=np.abs(0.5-0.5*b)
	j=np.append(j,z)

plt.stem(j)
plt.xlabel("frequency(w/pi)")
plt.ylabel("magnitude")
plt.title("hanning")
plt.show()
