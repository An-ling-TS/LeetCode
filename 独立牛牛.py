'''
@Descripttion: 
@version: 
@Author: Liang Anqing
@Date: 2020-07-17 19:50:41
@LastEditors: Liang Anqing
@LastEditTime: 2020-07-17 19:53:16
'''
def solu(arr):
    x,f,d,p=arr
    if int(d/x)<=f:
        return int(d/x)
    return f+int((d-f*x)/(p+x))
    
if __name__=='__main__':
    arr=list(map(int,input().strip().split()))
    print(solu(arr))