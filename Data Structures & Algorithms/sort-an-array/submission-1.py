class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
       import random

       def quicksort(nums,low,high):
           if low >= high:
            return
           random_index=random.randint(low,high)
           nums[random_index],nums[high]=nums[high],nums[random_index]
           partition=high
           i=low-1
           j=0
           for j in range(low,partition):
            if nums[j]<= nums[partition]:
                i=i+1
                nums[i],nums[j]=nums[j],nums[i]

           nums[i+1],nums[partition]=nums[partition],nums[i+1]
           quicksort(nums,low,i)
           quicksort(nums,i+2,high)

       quicksort(nums,0,len(nums)-1)
       return nums






        
        