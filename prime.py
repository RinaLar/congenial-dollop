def Prostota(m):
    a=1
    A=0
    m = int(m)
    for i in range (1,m):
        a=a*i
    A=a+1
    if A%m==0:
        return ("True")
    else:
        return ("False")






x= input()
print(Prostota(x))

