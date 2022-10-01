# ALthough short, this is not a fundamental solution since I'm using derivative methods in python such as sort(). Should focus on a fundamental appraoch using binary search.

def findMedianSortedArrays(nums1:list[int], nums2:list[int]) -> float:
    nums = (nums1+nums2)
    nums.sort()
    return nums[int((len(nums)+1)/2)-1] if len(nums) % 2 != 0 else (nums[int(len(nums)/2)-1] + nums[int(len(nums)/2+1)-1])/2.0

print(findMedianSortedArrays([1,3],[2,4]))