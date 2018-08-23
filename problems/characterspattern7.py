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
    l,c,s=map(int,input().split())
    i=i+1
    while j<=l*s*2:
        while k<=c*s*2:
            if (j+k+s-1)%(s*2)==0:
                line.append("/")
            elif (j-k -s)%(s*2)==0:
                line.append("\\")
            else:
                line.append(".")
            k=k+1
        arr1.append(line)
        line=[]
        j=j+1
        k=1
    arr2.append(arr1)
    j=1
    arr1=[]
while m<=t:
    while n<=len(arr2[m-1]):
        print("".join(arr2[m-1][n-1]))
        n=n+1
    m=m+1
    n=1