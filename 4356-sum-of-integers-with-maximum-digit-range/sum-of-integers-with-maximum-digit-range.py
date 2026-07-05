class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        n=len(nums)
        def digitrange(i):
            n1=str(nums[i])
            list1=list(n1)
            list2=[]
            for j in range(0,len(list1)):
                list2.append(int(list1[j]))
            if len(list2)==1:
                return 0
            else:
                list4=sorted(list2)
                n2=list4[-1]
                n3=list4[0]
                return n2-n3
        list3=[]
        for i in range(0,n):
            list3.append(digitrange(i))
        list5=sorted(list3)
        n4=list5[n-1]
        sum1=0
        for i in range(0,n):
            if list3[i]==n4:
                sum1+=nums[i]
        return sum1

        
        