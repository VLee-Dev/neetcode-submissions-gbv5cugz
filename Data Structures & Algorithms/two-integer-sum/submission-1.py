class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict={}
        for i, val in enumerate(nums):
            need= target-val
            if need in my_dict:
                return [my_dict[need], i]
            my_dict[val]=i
            
                