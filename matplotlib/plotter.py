import matplotlib.pyplot as plt
from math import *
y=input("y=")
lower_limit=int(input("Enter lower limit of x-values"))
upper_limit=int(input("Enter upper limit of x-values"))
x1=[]
y1=[]
for i in range(lower_limit,upper_limit+1):
    x1.append(i)
    exec(f"""x={i}
y_out={y}
y1.append(y_out)""")
plt.plot(x1, y1)
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
# giving a title to my graph
plt.title("Plotter")
# function to show the plot
plt.show()
