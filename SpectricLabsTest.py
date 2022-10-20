def take_skip(arr, take, skip):
    ans = []
    for i in range(0, len(arr), (take+skip)):
        # append "take" number of numbers
        for j in range(take):
            # make sure it is not out of bound
            if i + j < len(arr):
                ans.append(arr[i+j])
    return ans

def length_calculator(arr, take, skip):
    step = len(arr)//(take+skip)
    remainder = len(arr) % (take+skip)
    return step*take + min(take,remainder)
