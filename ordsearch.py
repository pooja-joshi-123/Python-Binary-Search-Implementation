
#function to perform binary search
def binary(data,value):
    low=0
    high=len(data)-1
    while low<=high:
        mid=(low+high)//2
        if value>data[mid]:
            low=mid+1
        elif value<data[mid]:
            high=mid-1
        else:
            return mid
    if value>data[high]:
        return -1
    else:
        return low

#function to get the first elements of each of the input lists
def binary_pairs(data, value):
    i=0
    words=[]
    while i<len(data):
        words.append(data[i][0])
        i=i+1
    return binary(words, value)

        
    
