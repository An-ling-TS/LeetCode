'''
@Descripttion: 
@version: 
@Author: Liang Anqing
@Date: 2020-07-17 12:11:34
@LastEditors: Liang Anqing
@LastEditTime: 2020-07-17 14:20:33
'''
import random
def sort(nums,le,ri):
    if le>=ri:
        return nums
    base=nums[le]
    i,j=le,ri
    print('(i,j)=('+str(i)+','+str(j)+')')
    print('base='+str(base))
    while i<j:
        #print('(i,j)='+'('+str(i)+','+str(j)+')')
        while i<j and nums[j]>base:
            j-=1
        nums[i]=nums[j]
        while i<j and nums[i]<=base:
            i+=1
        nums[j]=nums[i]
    nums[i]=base
    print('nums='+str(nums))
    sort(nums,le,i-1)
    sort(nums,i+1,ri)
    return nums

if __name__=='__main__':
    n=int(input('n='))
    nums=[]
    for i in range(n):
        nums.append(random.randint(0,n))
    print('排序前：'+str(nums))
    print('排序后：'+str(sort(nums,0,n-1)))