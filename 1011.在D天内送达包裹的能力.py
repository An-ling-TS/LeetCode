'''
1011. 在 D 天内送达包裹的能力

传送带上的包裹必须在 D 天内从一个港口运送到另一个港口。

传送带上的第 i 个包裹的重量为 weights[i]。每一天，我们都会按给出重量的顺序往传送带上装载包裹。我们装载的重量不会超过船的最大运载重量。

返回能在 D 天内将传送带上的所有包裹送达的船的最低运载能力。

 

示例 1：

输入：weights = [1,2,3,4,5,6,7,8,9,10], D = 5
输出：15
解释：
船舶最低载重 15 就能够在 5 天内送达所有包裹，如下所示：
第 1 天：1, 2, 3, 4, 5
第 2 天：6, 7
第 3 天：8
第 4 天：9
第 5 天：10

请注意，货物必须按照给定的顺序装运，因此使用载重能力为 14 的船舶并将包装分成 (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) 是不允许的。 

示例 2：

输入：weights = [3,2,2,4,1,4], D = 3
输出：6
解释：
船舶最低载重 6 就能够在 3 天内送达所有包裹，如下所示：
第 1 天：3, 2
第 2 天：2, 4
第 3 天：1, 4

示例 3：

输入：weights = [1,2,3,1,1], D = 4
输出：3
解释：
第 1 天：1
第 2 天：2
第 3 天：3
第 4 天：1, 1

'''
import math
class Solution(object):
    '''
    最低载重为每天的平均运载量，即average=总重W/天数D
    p_max=最重包裹
    载重>=average && 载重>=p_max
    每天尽力装满，从最小载重开始枚举，计算天数
    当计算结果=D 时，其最小载重为所求结果
    '''
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        p_max=max(weights)
        p_sum=sum(weights)
        p_average=math.ceil(p_sum/D)
        boat=max(p_max,p_average)
        D_count=0
        while D_count>D or D_count==0:
            D_count=0
            i=0
            #依次装入
            while i<len(weights):
                temp=boat
                #剩余容量无法再装时跳出
                while i<len(weights) and temp>=weights[i]:
                    temp-=weights[i]
                    i+=1
                D_count+=1
            boat+=1
        return int(boat-1)
if __name__=='__main__':
    so=Solution()
    D=5
    weights=[1,2,3,4,5,6,7,8,9,10]
    print(so.shipWithinDays(weights,5))
