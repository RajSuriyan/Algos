
def sumfinder(a,k):
    for i in a:
        diff=k-i
        if (diff in a):
            return True
    return False
def dsa(a,b):
    count=0
    for i in range(len(a)):
        count+=1
        if(a[i]>b[i]):
            a[i]=a[i]-b[i]
        if(len(set(a))==1):
            break
    return count
        


print(dsa([]))