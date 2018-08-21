t=int(input())
i=1
j=int(1)
k=1
line=[]
arr1=[]
arr2=[]
m=1
n=1
while i<=t:
    i=i+1
    l,c=map(int,input().split())
    while j<=l*3+1:
        while k<=c*3+1:
            if (k-1)%3==0 or (j-1)%3==0:
                line.append("*")
            else:
                line.append(".")
            k=k+1
        j=j+1
        arr1.append(line)
        line=[]
        k=1
    arr2.append(arr1)
    arr1=[]
    j=1
while m<=t:
    while n<=len(arr2[m-1]):
        print("".join(arr2[m-1][n-1]))
        n=n+1
    m=m+1
    n=1
    print("")