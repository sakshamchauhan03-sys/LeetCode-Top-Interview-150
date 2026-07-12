class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        n = len(arr)
        list2 = []
        set1 = set(arr)
        list1 = list(set1)
        list3 = sorted(list1)
        rank_map = {val: idx + 1 for idx, val in enumerate(list3)}

        for i in range(0, n):
            list2.append(rank_map[arr[i]])  

        return list2



        