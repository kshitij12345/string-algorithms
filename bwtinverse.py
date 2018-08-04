# python3
import sys

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start


def InverseBWT(bwt):
    sort = list(bwt)
    sort.sort()
    bwt = (bwt)
    answer = []
    s = ""
    #print (sort)
    
    for char in sort:
        s += char
        #print (s)

    #print(s,bwt)
    first = sort[0]
    second = bwt[0]
    index = 0
    while bwt:
        #print(first,second)
        #print(s,bwt)
        answer.append(second)
        #print ("CNT",bwt,second,index)
        cnt = bwt[:index+1].count(second)
        #print("CNTTT",cnt)
        s = s[:index]+s[index+1:]
        bwt = bwt[:index]+bwt[index+1:]
        cnts = s
        #print(s,bwt,cnt)
        #index = 0
        index = find_nth(cnts,second,cnt)
        if index == -1:
            break
        #print (index,s)
        first = s[index]
        second = bwt[index]
        #print(first,second)
        #second = bwt[second]

    #print ("-----")
    #print(s,bwt)
    #print (answer)
    answer.remove('$')
    #print (answer)
    answer.reverse()
    #print (answer)
    s = ""
    for char in answer:
        s +=char
    s+="$"
    return s


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))
