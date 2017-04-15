#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import pandas as pd
import numpy as np

from pandas import Series, DataFrame

def main():
	array = np.array([[1,2,5],[3,4,8]]);
	
	print(array.dtype)
	
	print(array.ndim)
	
	for item in array.flat:
		print(item)
		
	item = np.apply_along_axis(np.mean, axis=0, arr=array)
	print(item)
	
	narr = array.reshape(3,2)
	print(narr)
	
	# narr.shape = (6)
	print(narr.ravel())    
	
	# 矩阵转置
	print(narr.transpose())
	
	# 连接数组
	A = np.ones((3,3))
	B = np.zeros((3,3))
	np.vstack((A,B))
	np.hstack((A,B))
	
	C = np.ones((3,3))
	D = np.column_stack((A,B,C))	
	print(D)
	
	# split array
	[E,F,G] = np.hsplit(D,3)
	print(F)
	
	[E,F,G] = np.split(D,[1,3],axis=1)
	print(E)
	print(F)
	print(G)
	
	# 向量化
	A * B
	
	
	
# entry
if __name__ == "__main__":
	sys.exit(main())