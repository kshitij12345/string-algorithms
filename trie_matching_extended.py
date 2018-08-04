# python3
import sys

NA = -1

class Node:
	def __init__ (self):
		self.next = [NA] * 4
		self.patternEnd = False

def build_trie(patterns):
    tree = dict()
    tree[0] = {}
    cnt = 0
    for s in patterns:
        currentNode = tree[0]
        for char in s:
            currentSymbol = char
            if currentSymbol in currentNode:
                currentNode = tree[currentNode[currentSymbol]]
            else:
                cnt += 1
                currentNode[currentSymbol] = cnt
                tree[cnt] = {}
                currentNode = tree[cnt]
        currentNode['end']={}
    return tree

def PrefixTrieMatching(Text,trie):
        symbol = Text[0]
        v = trie[0]
        while True:
                if 'end' in v :
                        return True
                elif symbol in v:
                        Text = Text[1:]
                        if not Text:
                                break
                        v = trie[v[symbol]]
                        symbol = Text[0]
                        #print (v)
                        #v = trie[v[symbol]]

                else:
                        return False

        v = trie[v[symbol]]
        if 'end' in v:
                return True

        return False


def TrieMatching(Text,trie):
        result = []
        cnt = 0
        while Text:
                if PrefixTrieMatching(Text,trie):
                        result.append(cnt)
                cnt += 1
                Text = Text[1:]

        return result
                        


def solve (text, n, patterns):
	result = []

	trie = build_trie(patterns)
	#print(trie)
	result = TrieMatching(text,trie)
	

	return result


text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
	patterns += [sys.stdin.readline ().strip ()]

ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
