'''
@Descripttion: 
@version: 
@Author: Liang Anqing
@Date: 2020-07-03 17:59:00
@LastEditors: Liang Anqing
@LastEditTime: 2020-07-03 17:59:47
'''
'''
775. 全局倒置与局部倒置

数组 A 是 [0, 1, ..., N - 1] 的一种排列，N 是数组 A 的长度。全局倒置指的是 i,j 满足 0 <= i < j < N 并且 A[i] > A[j] ，局部倒置指的是 i 满足 0 <= i < N 并且 A[i] > A[i+1] 。

当数组 A 中全局倒置的数量等于局部倒置的数量时，返回 true 。

 

示例 1:

输入: A = [1,0,2]
输出: true
解释: 有 1 个全局倒置，和 1 个局部倒置。

示例 2:

输入: A = [1,2,0]
输出: false
解释: 有 2 个全局倒置，和 1 个局部倒置。
'''

def isIdealPermutation(self, A):
    """
    :type A: List[int]
    :rtype: bool
    """
    #局部倒置必定属于全局倒置，当且仅当所有的全局倒置都是局部倒置时返回true
    #1.对于每一位数字，要么只比下一位大1，要么比下一位小
    #2.每一位数字只和他相邻的数字交换位置，即i 只出现在a[i-1],a[i],a[i+1]里面
    #3.当a[i-1]=i时,a[i]=i-1,当a[i+1]=i时，a[i]=i+1
    #满足上述三条则返回true
    for i in range(len(A)):
        if i==A[i]:
            continue
        elif i+1<len(A) and i==A[i+1]:
            if A[i]!=i+1:
                return False
        elif i>0 and i==A[i-1]:
            if A[i]!=i-1:
                return False
        else:
            return False
    return True
