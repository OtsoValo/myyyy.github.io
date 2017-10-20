# -*- coding:utf-8 -*-
# class Solution:
#     # array 二维列表
#     def Find(self, target, array):
#         # write code here
#         n=len(array)
#         flag='false'
#         for i in range(n):
#             if target in array[i]:
#                 flag='true';
#                 break
#         return flag
# while True:
#     try:
#         S=Solution()
#         # 字符串转为list
#         L=list(eval(raw_input()))
#         array=L[1]
#         target=L[0]
#         print(S.Find(target, array))
#     except:
#         break


# -*- coding:utf-8 -*-
# class Solution:
#     # array 二维列表
#     def Find(self, target, array):
#         # write code here
#         _index = -1 
#         status = False
#         for ar in array:
#             for no ,i in enumerate(ar):
#                 print no,i,target
#                 if target <= i:
#                     if target==i:
#                         status=True
#                         print status
#                         return status
#                     else:
#                         _index=no
                
#         a_len = len(array)-1
#         _list = range(_index)
#         if _index:
#             for i in range(1,a_len):
#                 for j in _list:
#                     if target==array[i][j]:
#                         status=True
#         return status
# -*- coding:utf-8 -*-
# class Solution:
#     # array 二维列表
#     def Find(self, target, array):
#         # write code here
#         _index = -1 
#         status = False
#         array = eval(str(array))

#         for ar in array:
#             if target in ar:
#                 return 'true'
#         return 'false'
# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        a = s.split(' ')
        return '%20'.join(a)
        # write code here
if  __name__ == '__main__':
    import time
    t1=time.time()
    # print Solution().Find('hello world')
    print Solution().replaceSpace('hello world')
    
    t2 = time.time()
    print t2-t1
