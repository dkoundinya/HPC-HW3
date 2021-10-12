#Part A, Question 1
def solution(list, num): #O(1)
    a=0 
    b=0 
    nums=[]
    '''type in your solution, find a and b in array that a+b=num'''
    for i in range(0,len(numbers)):
        nums.append(abs(numbers[i]-num))
    for i in range(0,len(nums)):
        if nums[i] in numbers :
            a=nums[i]
            b=numbers[i]
        
    return a, b  
  
numbers = [21, 78, 19, 90, 13,109] 
print(solution(numbers, 109)) 
print(solution(numbers, 25))