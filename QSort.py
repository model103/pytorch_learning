import random
def QSort(nums:list):
    if len(nums) <= 1:
        return nums
    l = 0
    r = len(nums) - 1
    key = nums[0]
    while l < r:
        while nums[r] >= key and l < r:
            r-=1
        nums[l] = nums[r]
        while nums[l] <= key and l <r:
            l+=1
        nums[r] = nums[l]
    nums[l] = key
    return QSort(nums[0:l]) + [key] + QSort(nums[r+1:])

nums = [random.randint(0,9) for _ in range(10)]
print(QSort(nums))