for i in range(9,200,9):
    if i==9:
           print(i)
    else:
        i=str(i)
        if len(i)==2:
            if i[0]< i[1]:
                print(i)
        if len(i)==3:
            if i[1]<=i[2]:
                print(i)
                if i[1]==i[2]:
                    break
 

