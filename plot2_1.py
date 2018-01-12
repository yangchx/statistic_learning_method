import matplotlib.pyplot as plt  
import numpy as np

x_1 = [3, 4, 1 ]
x_2 = [3, 3, 1 ]
y = [1, 1, -1 ] ##x_1,x_2正实例,x_3负实例
N = 3

def plot_init():	
	#设置坐标轴名称
	plt.xlabel('$x^{(1)}$')
	plt.ylabel('$x^{(2)}$')
	#设置坐标轴范围
	plt.xlim((-0.5, 7))
	plt.ylim((-0.5, 7))

	#挪动坐标位置  
	ax = plt.gca()  
	#去掉边框  
	ax.spines['top'].set_color('none')  
	ax.spines['right'].set_color('none')  

	#移位置 设为原点相交  
	ax.xaxis.set_ticks_position('bottom')  
	ax.spines['bottom'].set_position(('data',0)) 
	ax.yaxis.set_ticks_position('left')  
	ax.spines['left'].set_position(('data',0))  
	

def plot_x1_x2(a,b):
	w1 = a[0]
	w2 = a[1]

	# w1*x1 + w2*x2+b = 0

	x1 = np.linspace(-0.5,7,50)
	x2 = -(b + w1*x1)/w2
	plt.plot(x1,x2 , color = 'k')

def plot_show(w, b):
	plot_init()
	
	plt.subplot(111) #解决plot和scatter不能同窗的问题

	plt.scatter(x_1[:2], x_2[:2], s=20, color='b', marker = 'o') 
	plt.scatter(x_1[-1], x_2[-1], s=20, color='b', marker = '+')
	plot_x1_x2(w , b)

	plt.show()  


def method():
	w, b, t = [0 , 0], 0, 1 #t表示步长
	i, j = 0, 0
	x = np.vstack((x_1 , x_2)) 
	x = x.T 

	while i != N:
		f = y[i]*(np.dot(w , x[i].T) + b)	
		while (y[i]*(np.dot(w , x[i].T) + b)) <= 0:
			print("w,b,f:", w, b, f)
			w = w + t*y[i]*x[i]
			b = b + t*y[i]
			i = 0					
		i += 1
	print("w,b,f:", w, b, f)
	plot_show(w , b)


if __name__ == '__main__':
	method()

