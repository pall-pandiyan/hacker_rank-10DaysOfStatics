# Enter your code here. Read input from STDIN. Print output to STDOUT
def mean(arr, N):
    avg = sum(arr)/len(arr)
    return round(avg,1)
    
def median(arr, N):
    cen = N//2
    if N%2 == 1:
        return arr[cen]
    else:
        avg = (arr[cen]+arr[cen-1])/2
        return round(avg,1)

def mode(arr,N):
    uniqueArr = list(set(arr))
    if N == len(uniqueArr):
        return min(arr)

    dupArr = [x for x in arr if arr.count(x)>1]    
    dupArr = list(set(dupArr))
    
    item = max(dupArr)
    count = 0
    
    for dup in dupArr:
        dupCount = arr.count(dup)
        if (dupCount > count) or (dupCount == count and dup < item):
            count = dupCount
            item = dup
    return item


def main():
    N = int(input().strip())
    arr = list(map(int,input().strip().split()))
    arr = arr[:N]
    arr.sort()
    
    print(mean(arr,N))
    print(median(arr,N))
    print(mode(arr,N))
    
if __name__=="__main__":
    main()