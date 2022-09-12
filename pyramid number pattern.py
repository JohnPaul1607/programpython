n=int(input("Enter the number"))
for i in range(0,n+1):
    for j in range(n-i):
        print("  ",end=" ")
    for j in range(1,i+1):
        print(i+1-j,end=" ")
    for j in range(i+1):
        print(j,end=" ")
    print()    
for i in range(0,n+1,1):
    for j in range(i):
        print('  ', end=" ")
    for j in range(n-i):
        print(n-j-i, end=" ")
    for j in range(n-i+1):
        print(j,end=" ")
    print()
