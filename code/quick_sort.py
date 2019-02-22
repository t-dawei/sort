#!/usr/bin/env python
#-*- coding:utf-8 -*-
# @auther: T


'''
思路：
通过一趟排序将要排序的数据分割成独立的两部分，
其中一部分的所有数据都比另外一部分的所有数据都要小，
然后再按此方法对这两部分数据分别进行快速排序，
整个排序过程可以递归进行，以此达到整个数据变成有序序列。
'''

'''
冒泡排序
时间复杂度：
	O(nlogn)
空间：O(1)
类别：交换类排序法：借助数据元素之间的互相交换进行排序的一种方法。
	方法一是交换排序
	方法二 是 分而治之 + 递归 
特点：
	1.方法一是原地排序算法， 方法2不是
'''

# 方法一
def quickSort(data, low, high):

	temp = data[low]
	while low != high:
		while low < high and data[high] >= temp:
			high -= 1
		data[low] = data[high]
		while low < high and data[low] <= temp:
			low += 1
		data[high] = data[low]

	data[low] =  temp

	return low

def partSort(data, low, high):
	if low < high:
		pos = quickSort(data, low, high)
		partSort(data, low, pos-1)
		partSort(data, pos+1, high)
	return data

# 方法二
def quickSort2(data):
	if len(data) < 2:
		return data
	# 选择基准线
	baseVal = data[0]
	less = [m for m in data if m < baseVal]
	equil = [m for m in data if m == baseVal]
	greater = [m for m in data if m > baseVal]
	return quickSort2(less) + equil + quickSort2(greater)


if __name__ == '__main__':
	list_data = [1, 0, 9, 7, 4, 5, 6, 3]
	print(partSort(list_data, 0, len(list_data)-1))
	print(quickSort2(list_data))