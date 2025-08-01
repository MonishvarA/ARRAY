def movneg(arr):
    neg=[]
    i=0
    while i<len(arr):
        if arr[i]<0:
            neg.append(arr[i])
            arr.pop(i)
        else:
            i+=1
    arr.extend(neg)
    return arr
arr=list(map(int,input("enter the number: ").split()))
print(movneg(arr))