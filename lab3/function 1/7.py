def has_33(a):
    for i in range(1,len(a)):           #check if the current element and the previous element are both 3
        if(a[i - 1] == a[i] == '3'):
            return True
    return False

nums = input().split()
print(has_33(nums))