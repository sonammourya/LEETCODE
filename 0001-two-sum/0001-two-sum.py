class Solution(object):
    def twoSum(self, nums, target):
       self.nums=[]
       self.target=9
       for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                self.nums.append(i)
                self.nums.append(j)
                return self.nums
nums=[2,7,11,15]
target=9
obj=Solution()
obj.twoSum(nums,target)
                

        