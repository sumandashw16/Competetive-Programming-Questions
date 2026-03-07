nums = [2,7,11,15]
target = 9

p1 = 0
p2 = 0
emptyList = []
while(p1<len(nums)-1):
    p2 = p1 + 1
    # print("here also")
    # print(p1, p2)
    p1 = p1+1
    for i in range(p2, len(nums)):
        # print("here")
        if(nums[p1-1] + nums[i] == target):
            # print("inside the loop")
            emptyList.append(p1-1)
            emptyList.append(i)
            p1 = len(nums)
            break
    # p1 = p1 + 1
print(emptyList)