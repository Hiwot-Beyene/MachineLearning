import matplotlib
import matplotlib.pyplot as plt
# or alternatively we can say
# from matplotlib import pyplot as plt

# print(matplotlib.__version__)

xcoordinates =[0,1,2,3,4,5,6]
ycoordinates = [10,15,20,25,30,35,40]
zcoordinates = [34,43,25,21,56,65,34]
plt.title("Graph of Relationships") #you can loc right, left or center(default)
plt.plot(xcoordinates,ycoordinates, linestyle ="--",marker = 's',color ='green') #marker
plt.plot(xcoordinates,zcoordinates, linestyle =":",color ='red')
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,66,133,87,64,87,77,85,86]
color = [0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100]
plt.scatter(x, y, c=color,cmap='viridis')
# m = [35, 15, 25, 25, 75, 25]
# L = ['first','second','third','fourth','fifth','sixth']
# color = ['blue','red','black','hotpink','#4CAF50','grey']
# plt.title('First Pie Chart')
# plt.pie(m, labels = L, colors = color)
plt.show()

# to zoom use plt.axis([pass 4 arguments]) the first to for x range the second two for y range