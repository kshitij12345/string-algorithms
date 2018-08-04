# python3
import sys

def BWT(text):
    bwtmat = []
    answer = []
    for i in range(len(text)):
        a = text[-1]
        a += text[0:-1] 
        text = a
        bwtmat.append(a)
        bwtmat.sort()

    for string in bwtmat:
        answer.append(string[-1])
    
    return answer


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))
