#!/usr/bin/env python
#-*- coding:utf-8 -*-
# @auther: T

'''
思路：
插入排序的基本操作就是将一个数据插入到已经排好序的有序数据中，
从而得到一个新的、个数加一的有序数据，算法适用于少量数据的排序
'''
'''
冒泡排序
时间复杂度：
	O(n*n)
空间：O(1)
类别：
	插入排序
特点：
	1.原地排序算法
'''

# 方式1 边比较边插入
def insertSort(data):
	for i in range(1, len(data)):
		for j in range(i, 0, -1):
			if data[j] < data[j-1]:
				data[j], data[j-1] = data[j-1], data[j]
	return data

# 方式2 先查找位置 最后插入
def insertSort2(data):
	for i in range(1, len(data)):
		for j in range(i-1, -1, -1):
			if data[i] < data[j]:
				data[j+1] = data[j]
			else:
				data[j+1] = data[i]
				break
		else:
			data[0] = data[i]
	return data

if __name__ == '__main__':
	list_data = [1, 0, 9, 7, 4, 5, 6, 3]
	print(insertSort(list_data))
	print(insertSort2(list_data))