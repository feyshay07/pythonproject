tnums = [2,7,11,15]
target = 9


def findTarget(nums = [2,7,11,15], target = 9):

    l = 0
    k = 1

    while l != len(nums) - 1:
        if target == nums[l] + nums[k]:
            return print([l, k])
        elif k == len(nums) - 1:

            l += 1
            k = l + 1
        elif target != nums[l] + nums[k]:
            k = k + 1

    return print(0)



findTarget(nums = [2,7,11,15], target= 29)
