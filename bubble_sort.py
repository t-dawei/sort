#!/usr/bin/env python
#-*- coding:utf-8 -*-
# @auther: T

'''
冒泡排序算法的原理如下：
比较相邻的元素。如果第一个比第二个大，就交换他们两个。
对每一对相邻元素做同样的工作，从开始第一对到结尾的最后一对。在这一点，最后的元素应该会是最大的数。
针对所有的元素重复以上的步骤，除了最后一个。
持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较
'''

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
