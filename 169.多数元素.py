'''
@Descripttion: 
@version: 
@Author: Liang Anqing
@Date: 2020-07-15 11:44:00
@LastEditors: Liang Anqing
@LastEditTime: 2020-07-15 11:44:22
'''
'''
169. 多数元素

给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

 

示例 1:

输入: [3,2,3]
输出: 3

示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2

'''
def majorityElement(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    return sorted(nums)[int(len(nums)>>1)]