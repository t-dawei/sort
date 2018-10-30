#!/usr/bin/env python
#-*- coding:utf-8 -*-
# @auther: T

'''
冒泡排序
时间复杂度：
	最差：O(n*n)
	最好：O(n)
空间：O(1)
类别：交换排序
特点：
	1.原地排序算法
'''
def bubbleSort(list_data):
	# i 表示需要循环的次数
	for i in range(len(list_data)-1):
		state_change = False
		# j 表示需要比较的次数
		for j in range(len(list_data)-i-1):
			if list_data[j] > list_data[j+1]:
				list_data[j], list_data[j+1] = list_data[j+1], list_data[j]
				state_change = True
		if not state_change:
			break
	return list_data

if __name__ == '__main__':
	list_data = [1, 0, 9, 7, 4, 5, 6, 3]
	print(bubbleSort(list_data))
