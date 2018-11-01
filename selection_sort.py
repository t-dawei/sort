#!/usr/bin/env python
#-*- coding:utf-8 -*-
# @auther: T

'''
思想：

1.找到数组中最小的那个元素

2.将最小的这个元素和数组中第一个元素交换位置

3.在剩下的元素中找到最小的的元素，与数组第二个元素交换位置

重复以上步骤，即可以得到有序数组。
'''
'''
冒泡排序
时间复杂度：
	O(n*n)
空间：O(1)
类别：
	选择排序
特点：
	1.原地排序算法
'''

def selectionSort(data):

	for i in range(len(data)-1):
		min_ = i
		for j in range(i+1, len(data)):
			if data[j] < data[min_]:
				min_ = j
		data[i], data[min_] = data[min_], data[i]
	return data


if __name__ == '__main__':
	list_data = [1, 0, 9, 7, 4, 5, 6, 3]
	print(selectionSort(list_data))
