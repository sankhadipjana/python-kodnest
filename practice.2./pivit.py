def pivot_index(nums):
    total_sum = sum(nums)
    left_sum = 0
    
    for i in range(len(nums)):
        # The right sum is the total sum minus what's on the left and the current element
        right_sum = total_sum - left_sum - nums[i]
        
        if left_sum == right_sum:
            return i
            
        left_sum += nums[i]
        
    return -1

n =  [1,2,3,2,1]

print(pivot_index(n))    