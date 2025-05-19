class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict[nums[0]] = 0
        for idx in range(1, len(nums)):
            curr_num = nums[idx]
            if target - curr_num in num_dict:
                return [num_dict[target - curr_num], idx]
            num_dict[curr_num] = idx
        return False
