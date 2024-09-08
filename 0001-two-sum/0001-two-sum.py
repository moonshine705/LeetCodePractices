""" better runtime solution:
class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {}
        for i in range(len(nums)):
            remain = target - nums[i]
            if remain in hashmap:
                return [i, hashmap[remain]]
            hashmap[nums[i]] = i

"""
class Solution(object):
    def twoSum(self, nums, target):
        '''
        :type nums: List[int]
        :type target: int
        :rtype: List[int]'''
    
        for i in range(len(nums)):
            for j in range(i+1, len(nums)): #i+1 is to not use the previous index before i
                if nums[i] + nums[j] == target:
                    return [i,j]

            