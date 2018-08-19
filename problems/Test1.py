t=int(input())
i=1
j=1
k=1
k=int(k)
arr2=[]
test=[]
arr3=[]
while i<=t:
    text=input()
    arr1=list(text)
    i=i+1
    lenght=int(len(arr1))
    while j<=lenght/2:
        arr2.append(arr1[j-1])
        j=j+1
        l=len(arr2)
    while k<=l:
        if (int(k)-1)%2==0:
            test.append(arr2[k-1])
        k=k+1
    print("".join(test))
    arr1=[]
    arr2=[]
    test=[]
    j=1
    k=1