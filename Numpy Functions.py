#To check array is empty or not we use this empty function 

import numpy as np
arr=np.empty((2,2))
print(arr)

#Will returns an array full of specified values
#Syntax: numpy.full(shape,fill,dtype=float,order='c') c is used to represent on rowwise

arr=np.full((3,3),2)
print(arr)

#Will returns evenly spaced nymbers over a specified interval
#Syntax:-numpy.linespace(start,stop,num=50,endpoint=True,retstep=False,dtype=None)

arr=np.linspace(2,10,5,dtype=int,retstep=True)
print(arr)

#WIll returns a contagious flatted array
#Syntax:- numpy.ravel(a,order='c')

lst=[[2,3],[5,8],[4,6]]
arr=np.array(lst)
print(arr)
print(np.ravel(arr))

#will returns members spaced evenly on a logscale

arr=np.logspace(0,1,num=10,base=10)
print(arr)

#Stack arrange in sequence vertically(row wise)

lst1=[2,3,4]
lst2=[5,6,7]
arr1=np.array(lst1)
arr2=np.array(lst2)
print(arr1)
print(arr2)
print(np.vstack((arr1,arr2)))

#Stack arrange in sequence horizontally(colomn wise)

lst1=[2,3,4]
lst2=[5,6,7]
arr1=np.array(lst1)
arr2=np.array(lst2)
print(arr1)
print(arr2)
print(np.hstack((arr1,arr2)))

#Join a sequence of array along a new axis

lst1=[2,3,4]
lst2=[5,6,7]
arr1=np.array(lst1)
arr2=np.array(lst2)
print(arr1)
print(arr2)
print(np.stack((arr1,arr2),0))
print(np.stack((arr1.arr2),1))



