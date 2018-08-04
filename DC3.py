import sys
def Ranker(Sorted):
    Rank = {}
    currRank = 1
    Rank[Sorted[0][1]] = currRank
    Repeat = False
    for x in range(1,len(Sorted)):
        if Sorted[x-1][0] == Sorted[x][0]:
            Rank[Sorted[x][1]] = currRank
            Repeat = True
        else:
            currRank += 1
            Rank[Sorted[x][1]] = currRank

    #print(Rank)
    return Rank,Repeat
            
def BCompare(A,B):
    if A < B:
        return 0
    return 1

def Merge(B0,B12,RankRes,T,listToBeSorted,ret = False):
    Rank = [0]*(len(T))
    for x in B12:
        Rank[x] = RankRes[x]

    if ret:
        currRank = 0
        for x in B12:
            currRank += 1
            Rank[x] = currRank

    if not ret:
        B12Sort = []
        for x in listToBeSorted:
            B12Sort.append(x[1])
        B12 = B12Sort
    listToBeSorted = []
    for x in B0:
            #print (x)
            #print(T[x])
        listToBeSorted.append([[T[x],Rank[x+1]],x])

    listToBeSorted.sort()
    B0 = []
    for x in listToBeSorted:
        B0.append(x[1])

    #print(B0)
    #print(B12)
    sorted = []
    while B0 and B12:
        index = B12[0]%3
        if index == 1:
            answer = BCompare([T[B0[0]],Rank[B0[0]+1]],[T[B12[0]],Rank[B12[0]+1]])
        if index == 2:
            answer = BCompare([T[B0[0]],T[B0[0]+1],Rank[B0[0]+2]],[T[B12[0]],T[B12[0]+1],Rank[B12[0]+2]])
				
        if answer == 0:
            sorted.append(B0[0])
            B0 = B0[1:]
        else :
            sorted.append(B12[0])
            B12 = B12[1:]

            #print(B0)
            #print(B12)
        
    sorted += B0
    sorted += B12

    return sorted

def DC_3(StringToBeSorted):
    T = StringToBeSorted
    #T += [0,0,0]
    T += [0]#maybe error prone
    #T += [0]
    #print(T)
    #l = len(StringToBeSorted) + len(StringToBeSorted)%3
    B0 = [x for x in range(len(T)) if (x%3==0)]
    B12 = [x for x in range(len(T)) if (x%3==1)]
    B12 += [x for x in range(len(T)) if (x%3==2)]
    T += [0,0,0]
    #print(B12)
    #print(B0)
    #sys.exit()
    listToBeSorted = []
    for a in B12:
        listToBeSorted.append([T[a:a+3],a])

    listToBeSorted.sort()
    #print(listToBeSorted)
    RankRes,Repeat = Ranker(listToBeSorted)
    #print(RankRes)
    #sys.exit()
    #print(RankRes[1])
    if Repeat:
        StringToBeSorted = []
        for x in B12:
            #StringToBeSorted += list(RankRes[x])
            StringToBeSorted.append(RankRes[x])
            #print(StringToBeSorted)
        #print('--------------------------')
        #print("String To Be Sorted",StringToBeSorted)
        recReturn = (DC_3(StringToBeSorted))
        sortedB12 = []
        #print("RecReturn ",recReturn)
        #print ("B12",B12)
        for x in recReturn[1:]:
            sortedB12.append(B12[x])
        B12 = sortedB12
        #print("B12----",B12)
        return Merge(B0,B12,RankRes,T,listToBeSorted,ret= True)



#####################################################
    if not Repeat:
        return Merge(B0,B12,RankRes,T,listToBeSorted)

	

#a = [2,1,2,1,2,1,2,1]
#b = [5,1,2,2,1,3,1,2,2,1,3,4]
#c = [1,1,2,3,1,4,1,3,2,3,3,4,1,3,1]
#print(DC_3(c))
