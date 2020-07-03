
'''
@Descripttion: 
@version: 
@Author: Liang Anqing
@Date: 2020-07-03 20:15:38
@LastEditors: Liang Anqing
@LastEditTime: 2020-07-03 20:22:26
'''
'''
476. 数字的补数

给定一个正整数，输出它的补数。补数是对该数的二进制表示取反。

 

示例 1:

输入: 5
输出: 2
解释: 5 的二进制表示为 101（没有前导零位），其补数为 010。所以你需要输出 2 。

示例 2:

输入: 1
输出: 0
解释: 1 的二进制表示为 1（没有前导零位），其补数为 0。所以你需要输出 0 。
'''
def findComplement(num):
    """
    :type num: int
    :rtype: int
    """
    temp=bin(num)
    rs=''
    for i in range(len(temp)):
        if temp[i]=='0' and i!=0:
            rs+='1'
        elif temp[i]=='1':
            rs+='0'
        else:
            rs+=temp[i]
        print(rs)
    return int(rs,2)
rs=findComplement(5)
print(rs)