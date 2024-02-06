def spy_game(a):
    s = ''
    for i in a: 
        if(i == 7 or i == 0): 
            s += str(i)  # if it is 0 or 7 will be added into the 's'

    if('007' in s):
        return True
    else:
        return False

nums = [1,7,2,0,4,5,0] 
print(spy_game(nums))