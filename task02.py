def evenlist(start, n):
    if start%2 != 0:
        start += 1
    for i in range (n):
        print (start+2*i, end=" ")
    return

[start, n]=list(map(int, input().split()))
evenlist (start, n)