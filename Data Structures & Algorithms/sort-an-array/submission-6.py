class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
       
     def merge(nums1,nums2):
         i=0
         j=0
         result=[]
         while i < len(nums1) and  j< len(nums2):
            if nums1[i]<=nums2[j]:
                result.append(nums1[i])
                i=i+1
            else: 
                result.append(nums2[j])
                j=j+1
            if i==len(nums1):
                result.extend(nums2[j:])
            if j==len(nums2):
                result.extend(nums1[i:])

         return result

     def mergesort(nums):
           if len(nums)<=1:
              return nums
           mid=(len(nums))//2
           left=mergesort(nums[:mid])
           right=mergesort(nums[mid:])
           return merge(left,right)


     return mergesort(nums)
    
              

       




        
        