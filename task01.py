def multiply(a, b, bound):
    mul = a*b
    if mul <= bound:
        print (mul)
    else:
        print ("multiplication of "+str(a)+" and "+str(b)+" with bound "+str(bound)+" is not possible")
    return

n = int(input())
for i in range (n):
    [a, b, bound]=list(map(int, input().split()))
    multiply (a, b, bound)