class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n=len(spells)
        m=len(potions)
        potions.sort()
        result=[]
        for spell in spells:
            min_potions=math.ceil(success/spell)
            #binary search
            left=0
            right=m-1
            first_valid_index=m
            while left<=right:
                mid=left+(right-left)//2
                if potions[mid]>=min_potions:
                    first_valid_index=mid
                    right=mid-1
                else:
                    left=mid+1
            
            successful_count=m-first_valid_index
            result.append(successful_count)

        return result


        