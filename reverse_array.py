import random

# [1] Swap with two pointers - while
def reverse(nums):

    start_index = 0
    end_index = len(nums) - 1

    while start_index < end_index:
        nums[start_index], nums[end_index] = nums[end_index], nums[start_index]
        start_index = start_index + 1
        end_index = end_index - 1

if __name__ == '__main__':

    nums = random.sample(range(0, 10), 10)
    print(nums)
    reverse(nums)
    print(nums)
