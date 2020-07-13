'''
@Descripttion: 
@version: 
@Author: Liang Anqing
@Date: 2020-07-12 14:44:08
@LastEditors: Liang Anqing
@LastEditTime: 2020-07-12 14:44:41
'''
'''
429. N叉树的层序遍历

给定一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。

例如，给定一个 3叉树 :

 

 

返回其层序遍历:

[
     [1],
     [3,2,4],
     [5,6]
]

 

说明:

    树的深度不会超过 1000。
    树的节点总数不会超过 5000。
'''
def levelOrder(self, root):
    """
    :type root: Node
    :rtype: List[List[int]]
    """
    if root==None:
        return []
    res=[]
    queue=[]
    queue.append(root)
    while len(queue)>0:
        temp=[]
        size=len(queue)
        for i in range(size):
            cur=queue[0]
            del queue[0]
            temp.append(cur.val)
            for child in cur.children:
                queue.append(child)
        res.append(temp)
    return res