t= int(input())



def maximaze(t):

    for i in range(t):
        m, n, k = map(int, input().split(" "))
        maximum=0       # maximum number of rooms that may recieve power
        ls1 = []        # how many rooms per floor have correct wiring
        for i in range(m):
            ls1.append(int(input()))
        for x in ls1:
            if x<n:
                maximum+=n-x
            else:
                maximum+=x
        print(maximum)
    return ""
print(maximaze(t))