'''
@Descripttion: 
@version: 
@Author: Liang Anqing
@Date: 2020-07-04 14:15:07
@LastEditors: Liang Anqing
@LastEditTime: 2020-07-04 14:15:57
'''
'''
面试题 01.05. 一次编辑

字符串有三种编辑操作:插入一个字符、删除一个字符或者替换一个字符。 给定两个字符串，编写一个函数判定它们是否只需要一次(或者零次)编辑。

 

示例 1:

输入: 
first = "pale"
second = "ple"
输出: True

 

示例 2:

输入: 
first = "pales"
second = "pal"
输出: False

'''
def oneEditAway(self, first, second):
    """
    :type first: str
    :type second: str
    :rtype: bool
    """
    #如果一样,或者一个空，一个长度为一，直接返回true
    if first==second or (len(first)==0 and len(second)==1) or (len(second)==0 and len(first)==1):
        return True
    #如果长度相差大于1，则返回False
    if abs(len(first)-len(second))>1:
        return False
    max_=max(len(first),len(second))
    for i in range(max_):
        if len(first)==i or len(second)==i:
            return True
        if first[i]==second[i]:
            continue
        #替换
        if len(first)==len(second):
            if first[0:i]+second[i]+first[i+1:len(first)]==second:
                return True
            return False
        #插入
        if len(first)<len(second):
            if first[0:i]+second[i]+first[i:len(first)] ==second:
                return True
            return False
        #first删除->second 插入
        if second[0:i]+first[i]+second[i:len(second)]==first:
            return True
        return False