def subarray_sum(nums, target):
    num_map = {}
    sum_ = 0
    
    for i, num in enumerate(nums):
        sum_ += num
        
        while sum_ > target:
            sum_ -= nums[num_map[i - 1]]
            num_map.pop(i - 1)
            i -= 1

        if sum_ == target:
            return [num_map[i] + 1, i]

        num_map[i] = i

    return None



print(subarray_sum([1, 2, 3, 4, 5], 9))




