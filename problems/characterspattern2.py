t=int(input())
i=1
j=1
k=1
line=[]
arr1=[]
arr2=[]
m=1
n=1
while i<=t:
    l,c=map(int,input().split())
    i=i+1
    while j<=l:
        while k<=c:
            if j==1 or j==l or k==1 or k==c:
                line.append("*")
            else:
                line.append(".")
            k=k+1
        arr1.append(line)
        line=[]
        j=j+1
        k=1
    arr2.append(arr1)
    arr1=[]
    j=1
while m<=t:
    while n<=len(arr2[m-1]):
        print("".join(arr2[m-1][n-1]))
        n=n+1
    print("")
    m=m+1
    n=1
