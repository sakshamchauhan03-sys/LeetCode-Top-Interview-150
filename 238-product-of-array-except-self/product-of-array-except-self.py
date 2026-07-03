class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        product=1
        mul=[]
        if 0 not in nums:
            for i in range(0,n):
                product*=nums[i]
            for i in range(0,n):
                mul.append(int(product/nums[i]))
            return mul
        else:
            count=0
            i=0
            while i<n:
                if nums[i]==0:
                    count+=1
                i+=1
            if count==1:
                a=nums.index(0)
                nums.remove(0)
                for i in range(0,n-1):
                    product*=nums[i]
                    list1=[]
                for i in range(0,n):
                    list1.append(0)
                list1[a]=product
                return list1
            else:
                list2=[]
                for i in range(0,n):
                    list2.append(0)
                return list2



