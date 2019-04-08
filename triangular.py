import numpy as np
import matplotlib.pyplot as plt
m=int(input("enter value="))
h=[]
for n in range(0,m-1):
	a=np.abs(n-(m-1)/2)
	x=(1-(2*a)/(m-1))
	h=np.append(h,x)

plt.plot(h)
plt.xlabel("frequency(w/pi)")
plt.ylabel("magnitude")
plt.title("triangular")
plt.show()