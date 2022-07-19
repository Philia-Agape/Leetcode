class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        nums.sort()
        num_map = {}
        for n in nums:
            if num_map.get(n) == None:
                num_map.update({n:1})
            else:
                num_map[n] += 1 
        delete, flag = 0, 1
        for n,v in num_map.items():
            #flag = 1
            if flag and delete != len(nums):
                flag = 0
                for d in numsDivide:
                    if d % n != 0:
                        flag = 1
                        delete += v
                        break
        return delete if delete != len(nums) else -1                
