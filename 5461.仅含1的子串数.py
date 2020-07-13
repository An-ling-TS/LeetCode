'''
@Descripttion: 
@version: 
@Author: Liang Anqing
@Date: 2020-07-12 12:51:11
@LastEditors: Liang Anqing
@LastEditTime: 2020-07-12 13:47:07
'''
def numSub(s):
    """
    :type s: str
    :rtype: int
    """
    #转化为求最长含1子字符串
    dp=[int(ch) for ch in s]
    size=len(s)
    res=0
    for i in range(size):
        #i为dp下标，代表dp所表示的字符位置
        for j in range(1,size-i):
            if i>0 and s[i-1]=='1':
                dp[i]=0
            if s[i+j]=='0' or dp[i]==0:
                break
            dp[i]+=1
    if s[size-2]=='1':
	    dp[size-1]=0
    print('dp:  '+str(dp))
    for val in dp:
        if val==0:
            continue
        #res+=((val+1))*(val)>>1
        res+=((val+1)%1000000007)*(val%1000000007)>>1
    print('res:  '+str(res))
    return res
s='0110111'
numSub(1)        
                