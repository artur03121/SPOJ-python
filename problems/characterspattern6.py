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
    l,c,h,w=map(int,input().split())
    while j<=l*(h+1)+h:
        while k<=c*(w+1)+w:
            if k%(w+1)==0 and j%(h+1)==0:
                line.append("+")
            elif k%(w+1)==0:
                line.append("|")
            elif j%(h+1)==0:
                line.append("-")
            else:
                line.append(".")
            k=k+1
        j=j+1
        k=1
        arr1.append(line)
        line=[]
    j=1
    arr2.append(arr1)
    arr1=[]
while m<=t:
    while n<=len(arr2[m-1]):
        print("".join(arr2[m-1][n-1]))
        n=n+1
    m=m+1
    n=1
    print("")
        