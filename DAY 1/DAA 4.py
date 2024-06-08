def findlargestelement(arr):
    if len(arr)==1:
        return arr[0]
    else:
        return max(arr[0],findlargestelement(arr[1:]))
arr=[3,5,7,2,8,1]
print(findlargestelement(arr))
