'''
@Descripttion: 
@version: 
@Author: Liang Anqing
@Date: 2020-07-12 14:51:57
@LastEditors: Liang Anqing
@LastEditTime: 2020-07-12 15:11:35
'''
def largestRectangleArea(heights):
    """
    :type heights: List[int]
    :rtype: int
    """
    #动态规划
    #dp[i]=area 表示从i开始，向右勾画所能画出的最大矩形的面积
    dp=[i for i in heights]
    size=len(heights)
    for i in range(size):
        for j in range(size-i):
            print('min='+str(min(heights[i:j+1+i])*(j+1)))
            print('dp['+str(i)+']='+str(max(dp[i],min(heights[i:j+1+i])*(j+1))))
            dp[i]=max(dp[i],min(heights[i:j+1+i])*(j+1))
    print(max(dp))
    return max(dp)
s=[2,1,5,6,2,3]
largestRectangleArea(s)