def ComputePrefixFunction(P):
    s = [0]*len(P)
    border = 0
    for i in range(1,len(P)):
        while (border > 0) and (P[i] != P[border]):
            border = s[border - 1]

        if P[i]==P[border]:
            border = border + 1
        else:
            border = 0

        s[i] = border

    #print (s)
    return s

def FindAllOccurences(P,T):
    S = P + "$" + T
    s = ComputePrefixFunction(S)
    l= len(P)
    result = []
    for i in range(l+1,len(S)):
        if s[i] == l:
            result.append(i-2*l)

    return result

print(FindAllOccurences("abrac","abracadabra"))
