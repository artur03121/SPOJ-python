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
    i=i+1
    l, c, h, w=map(int, input().split())
    while j<=l*(h+1)+1:
        while k<=c*(w+1)+1:
            if (j-1)%(h+1)==0 or (k-1)%(w+1)==0:
                line.append("*")
            else:
                line.append(".")
            k=k+1
        arr1.append(line)
        k=1
        line=[]
        j=j+1
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