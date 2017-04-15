#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import pandas as pd
import numpy as np
import re

from pandas import Series, DataFrame

def main():

	s = pd.Series([12,-4,2,9],index=['red','blue','puple','hi'])
	
	print(s)
	
	# pandas 库是以 Numpy 为基础的，所以 Numpy数组的很多操作在 pandas 中同样适用
	# 然而对于 Numpy 的数学函数，pandas 中必须指定出处 np
	#s = np.log(s)
	
	# DataFrame
	frame = pd.DataFrame(np.arange(16).reshape(4,4),index=['red','blue','yellow','white'],columns=['ball','pen','paper','pencil'])
	
	# frame.index frame.values frame.columns
	print(frame)
	
	# frame['pen']  frame.pen  选取行 frame.ix[2]
	
	# delete columns
	del frame['pen']

	print(frame)
	
	print(frame[(frame < 12)])
 	
	# dataFrame 转置
	frame = frame.T
	print(frame)
	
	# delete frame.drop([,],axis=1)
	
	# 按行或列执行函数操作
	newFrame = frame.apply(f, axis=1)

	print(newFrame)
	
	# 协方差 和 相关性
	
	# NaN 数据
	# 对于series 直接使用 s.dropna() 或者 s[s.notnull()] 过滤所有 Nan
	# 对于Frame 使用 dropna的话，只要行或者列存在一个 NaN元素，该行、列就都会被删除
	# 为了避免，frame.dropna(how='all')
	
	# 为 NaN 填充其他值 frame.fillna(0)
	# frame.fillna({'ball':1,'bag':0})
		
	# pandas 数据处理：数据准备、数据转换、数据聚合
	
	# 合并：pd.merge(frame1,frame2,on='id')  on指定合并操作所依据的基准列
	
	# 转换：
	
	# 聚合：GroupBy - 分组、函数处理、合并
	# 可以使用 agg(def) 的方式自定义聚合函数
	# 高级聚合：transfom 、 apply
	
	
	
	
	
		
def f(x):
	
	return x.max() - x.min()
	
# entry
if __name__ == "__main__":
	sys.exit(main())