# -*- coding: UTF-8 -*-


class Solution(object):

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return 0
        elif length == 1:
            return 0 if target <= nums[0] else 1
        begin, end = 0, length - 1
        while end != begin:
            mid = (end + begin) / 2
            comp = nums[mid]
            if target == comp:
                return mid
            elif target < comp:
                end = mid
                continue
            elif target > comp:
                begin = mid + 1
                continue
        if target <= nums[begin]:
            return begin
        return begin + 1
