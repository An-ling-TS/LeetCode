'''
@Descripttion: 
@version: 
@Author: Liang Anqing
@Date: 2020-07-06 15:51:01
@LastEditors: Liang Anqing
@LastEditTime: 2020-07-06 16:07:09
'''
'''
面试题 17.10. 主要元素

数组中占比超过一半的元素称之为主要元素。给定一个整数数组，找到它的主要元素。若没有，返回-1。

示例 1：

输入：[1,2,5,9,5,9,5,5,5]
输出：5

 

示例 2：

输入：[3,2]
输出：-1

 

示例 3：

输入：[2,2,1,1,1,2,2]
输出：2
'''
def majorityElement(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    a=sorted(nums)
    size=len(a)
    if size<2:
        return -1 if size==0 else nums[0]
    if size==3:
        return a[1] if a[1]==a[2] or a[1]==a[0] else -1
    return a[size>>1] if a[size>>1]==a[size>>2] or a[size>>1]==a[(size>>2)*3] else -1
'''
执行结果：
通过
显示详情
执行用时：20 ms, 在所有 Python 提交中击败了99.50% 的用户
内存消耗：13.8 MB, 在所有 Python 提交中击败了100.00% 的用户
'''