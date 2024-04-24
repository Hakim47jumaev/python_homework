a=input().split()
for i in range(0,len(a)+1):
    if int(a[i])*int(a[i+1])>0:
        print(a[i],a[i+1])
        break