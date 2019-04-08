import numpy as np
import matplotlib.pyplot as plt
m=int(input("enter value="))
h=[]
for n in range(0,m-1):
	x=1
	h=np.append(h,x)

plt.plot(h)
plt.xlabel("frequency(w/pi)")
plt.ylabel("magnitude")
plt.title("rectangular")
plt.show()