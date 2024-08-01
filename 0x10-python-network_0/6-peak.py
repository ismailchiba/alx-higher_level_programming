#!/usr/bin/python3
def find_peak(integers_list):
    if not integers_list:
        return None

    return _find_peak_rec(integers_list, 0, len(integers_list) - 1)


def _find_peak_rec(nums, low, high):
    mid = (low + high) // 2

    # Check if mid is a peak
    if (mid == 0 or nums[mid] >= nums[mid - 1]) and (mid == len(nums) - 1 or nums[mid] >= nums[mid + 1]):
        return nums[mid]
    # If left neighbor is greater, then peak must be in left half
    elif mid > 0 and nums[mid - 1] > nums[mid]:
        return _find_peak_rec(nums, low, mid - 1)
    # If right neighbor is greater, then peak must be in right half
    else:
        return _find_peak_rec(nums, mid + 1, high)
