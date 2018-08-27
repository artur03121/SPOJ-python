t=int(input())
i=1
arr=[]
x_left=0
x_right=0
y_bot=0
y_top=0
j=1
x_max=-1000
x_min=1000
y_max=-1000
y_min=1000
arr=[]
while i<=t:
    n=int(input())
    i=i+1
    while j<=n:
        a=input()
        a=a.split()
        if a[0]=="p":
            y_bot=int(a[2])
            x_left=int(a[1])
            x_right=int(a[1])
            y_top=int(a[2])
        elif a[0]=="c":
            y_bot=int(a[2])-int(a[3])
            y_top=int(a[2])+int(a[3])
            x_left=int(a[1])-int(a[3])
            x_right=int(a[1])+int(a[3])
        else:
            if int(a[2])>=int(a[4]):
                y_bot=int(a[4])
                y_top=int(a[2])
            else:
                y_bot=int(a[2])
                y_top=int(a[4])
            if int(a[1])>=int(a[3]):
                x_right=int(a[1])
                x_left=int(a[3])
            else:
                x_right=int(a[3])
                x_left=int(a[1])
        j=j+1
        if x_right>x_max:
            x_max=x_right
        if y_top>y_max:
            y_max=y_top
        if x_left<x_min:
            x_min=x_left
        if y_bot<y_min:
            y_min=y_bot
    arr.append(str(x_min)+" ")
    arr.append(str(y_min)+" ")
    arr.append(str(x_max)+" ")
    arr.append(str(y_max))
    print("".join(arr))
    arr=[]
    j=1
    x_min=1000
    x_max=-1000
    y_max=-1000
    y_min=1000
    print("")
    
    