# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        _index = None 
        status = False
        for ar in array:
            for no ,i in enumerate(ar):
                if target < i:
                    if target==i:
                        status=True
                    else:
                        _index=no
        a_len = len(array)-1
        print _index,a_len,range(1,a_len)
        _list = range(_index)
        if _index:
            for i in range(1,a_len):
                for j in _list:
                    print array[i][j],i,j
                    if target==array[i][j]:
                        status=True
        return status
if  __name__ == '__main__':
    print Solution().Find(7,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]])
