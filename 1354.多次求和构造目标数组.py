'''
@Descripttion: 
@version: 
@Author: Liang Anqing
@Date: 2020-07-10 20:29:55
@LastEditors: Liang Anqing
@LastEditTime: 2020-07-11 10:18:23
'''
def isPossible(target):
    """
    :type target: List[int]
    :rtype: bool
    """
    if len(target)==1 and target[0]!=1:
            return False
    while max(target)>1:
        #当前最大值
        max_=max(target)
        #将存放当前最大值的位置重置为此前被替换掉的数 num=max_ - k*(sum-max_) -> num=(k+1)*max_-k*sum
        if 2*max_-sum(target)<1:
            return False
        tem=list(target)
        del tem[tem.index(max_)]
        #print(target)
        k=int((max_-max(tem))/(sum(target)-max_))
        if k<1:
            k=1
        print('k=   '+str(k))
        print('count=   '+str((k+1)*max_-k*sum(target)))
        target[target.index(max_)]=(k+1)*max_-k*sum(target)
    return True
te=[1,10000]
print('rs:  '+str(isPossible(te)))
                
    