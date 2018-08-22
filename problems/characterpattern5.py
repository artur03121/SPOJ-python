t=int(input())
i=1
j=1
k=1
m=1
n=1
line=[]
arr1=[]
arr2=[]
while i<=t:
    l,c,s=map(int,input().split())
    i=i+1
    while j<= l*(s+1)+1:
        while k<= c*(s+1) +1:
            if (j-1) %(s+1)==0 or (k-1)%(s+1)==0:
                line.append("*")
            elif (j-k)%(2*s+2)==0:
                line.append("\\")
            elif(j+k-2)%(2*s+2)==0:
                line.append("/")
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
    m=m+1
    n=1
    print("")