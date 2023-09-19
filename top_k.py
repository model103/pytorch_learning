# 查找数组中第k大的数
import random

#快速排序方式，不考虑重复的数字
def top_k(nums, begin, end, k):
    l = begin
    r = end
    key = nums[l]
    while (l < r):
        while (l < r and nums[r] <= key): #从大到小排序
            r -= 1
        nums[l] = nums[r]
        while (l < r and nums[l] >= key):
            l += 1
        nums[r] = nums[l]
    nums[l] = key
    if l == (k - 1):
        return nums[l]
    elif l > (k - 1):
        return top_k(nums, begin, l - 1, k)
    else:
        return top_k(nums, l + 1, end, k)
#nums = [7, 9, 5, 9, 2, 0, 7, 3, 3, 1]
#print(nums)
#print(top_k(nums,0,len(nums)-1, 3))

for i in range(100000): #循环多次测试
    nums = [random.randint(0, 10) for _ in range(10)]
    copy = nums.copy()
    copy.sort()
    if copy[-3] == top_k(nums,0,len(nums)-1, 3):
        #print('bingo')
        pass
    else:
        print(nums)
        print(top_k(nums,0,len(nums)-1, 3))



def top_3(nums):
    if len(nums)<3:
        return -1
    k = [-pow(2,15) for _ in range(3)] #chush初始化

    for num in nums:
        if num > k[0]: #先把k往后滚动一格,再把最大的k[0]重新赋值为当前num
            k[1:3] = k[0:2]
            k[0] = num
        elif num < k[0] and num > k[1]:
            k[2] = k[1]
            k[1] = num
        elif num < k[1] and num > k[2]:
            k[2] = num
    return k[2]
#nums = [6, 6, 8, 2, 1, 6, 5, 3, 4, 1]
#print(top_3(nums))

for i in range(100000): #多次测试
    nums = [random.randint(0, 10) for _ in range(10)]
    copy = list(set(nums.copy()))#set去重并乱序
    copy.sort()
    if copy[-3] == top_3(nums):
        #print('bingo')
        pass
    else:
        print('nums',nums)
        print('copy',copy)
        print(top_3(nums))