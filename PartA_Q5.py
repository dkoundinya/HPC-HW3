# Part A, Question 5 
import numpy as np
# 1-D arrays
a1= np.array([1,2,3,4])
a2= np.array([5,6,7,8])
add1=np.add(a1,a2)
sub1=np.subtract(a1,a2)
mul1=np.multiply(a1,a2)
div1=np.divide(a1,a2)
print(f"sum = {add1}\n\n difference= \n{sub1}\n\n product= \n{mul1}\n\n division=\n{div1}\n\n")
# 2-D arrays
a3= np.random.rand(4,4)
a4= np.random.rand(4,4)
print(a3 ,'\n\n', a4,'\n\n')
add2=np.add(a3,a4)
sub2=np.subtract(a3,a4)
mul2=np.multiply(a3,a4)
div2=np.divide(a3,a4)
print(f"sum = {add2} \n\n difference= {sub2} \n\n product= {mul2} \n\n division= {div2}")