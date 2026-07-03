class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        set1=set(nums)
        list1=list(set1)
        for i in range(0,len(list1)):
            if nums.count(list1[i])>int(n/2):
                return list1[i]
        