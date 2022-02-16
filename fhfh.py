def fyn (x,y):
    a=x+y
    return a
c= fyn(1,2)
print(c)

a=int(input())
def frac (a):
    if a>0:
        s=a*frac(a-1)
        return(s)
    else:
        return 1
print(frac(a))
