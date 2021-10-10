def spy_game(nums):
    i = 0
    c = 0
    while c < len(nums) - 1:
        if nums[i] == 0:
            if nums[i + 1] == 0:
                if nums[i + 2] == 7:
                    return True
                else:
                    pass
            else:
                pass
        else:
            pass
        c += 1
        i += 1
    return False


print(spy_game([0,7,0,7]))
print(spy_game([0,1,2,3,7,8,3,0]))
print(spy_game([7,1,2,0,7,8,0,7,2]))
print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))

    #[0,7,0,7] ---> True
    #[0,1,2,3,7,8,3,0]  ---> False
    #[7,1,2,0,7,8,0,7,2] ---> True