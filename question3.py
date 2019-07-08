def equilibrium(arr): 
    total_sum = sum(arr) 
    leftsum = 0
    for i, num in enumerate(arr): 
        total_sum -= num 
        if leftsum == total_sum: 
            return i 
        leftsum += num 
arr = [2,4,4,1,5,4,1] 
print ('First equilibrium index is ', 
       equilibrium(arr))
