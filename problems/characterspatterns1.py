t=int(input())
i=1
k=1
j=1
arr=[]
arr2=[]
m=1
n=1
while i<=t: #inicia um caso
    l,c=map(int,input().split())
    line=[]
    while k<=l: #max de linhas
        while j<=c: #montando uma linha
            if (k-1)%2==0: #linha par
                if (j-1)%2==0: #coluna par
                    line.append("*")
                else:
                    line.append(".")
            else: #linha impar
                if (j-1)%2==0: #coluna par
                    line.append(".")
                else:
                    line.append("*")
            j=j+1
        k=k+1
        arr.append(line)
        line=[]
        j=1
    arr2.append(arr)
    arr=[]
    k=1
    i=i+1
    line=[]
while m<=t:
    while n<=len(arr2[m-1]):
        print("".join(arr2[m-1][n-1]))
        n=n+1
    m=m+1
    n=1
    print("")