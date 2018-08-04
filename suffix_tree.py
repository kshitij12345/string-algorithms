# python3
import sys

'''def Compress(trie,current,key):
  if current == {}:
    return []
  elif len(current.keys())==1:
    for x in current:
      return Compress(trie,trie[current[x]],current[x])+list(x)
  else:
    for x in current:
      #print (Compress(trie,trie[current[x]]))      
      current[x] = Compress(trie,trie[current[x]],current[x])
      #print (trie)
    return key'''

def Compress(trie,current,key):
  if current == {}:
    return []
  elif len(current.keys())==1:
    for x in current:
      try:
        y = Compress(trie,trie[current[x]],current[x])
        return y+list(x)
      except:
        current[x] = y
        return key
  else:
    for x in current:
      #print (Compress(trie,trie[current[x]]))      
      y = Compress(trie,trie[current[x]],current[x])
      if type(y)==type([]):
        current[x] = y+[x]
      else:
        current[x] = y
      #print (trie)
    return key


      
  
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

    print (tree)                
    return tree

global visited

def visit(currentNode,trie):
  for x in currentNode:
    #print(currentNode[x])
    if type(currentNode[x]) == type(2):
      visited[currentNode[x]] = True
      visit(trie[currentNode[x]],trie)

def ShortenTrie(trie):
  global visited
  visited = [False]*len(trie.keys())

  visited[0]= True
  visit(trie[0],trie)

  for i in range(len(trie.keys())):
    if not visited[i]:
      del trie[i]
  


def build_suffix_tree(text):
  """
  Build a suffix tree of the string text and return a list
  with all of the labels of its edges (the corresponding 
  substrings of the text) in any order.
  """
  result = []
  pattern = []
  for x in range(len(text)):
    pattern.append(text)
    text = text[1:]

  trie = build_trie(pattern)
  #print(len(trie[0].keys()))
  Compress(trie,trie[0],0)
  #print (trie)
  ShortenTrie(trie)
  print(trie)
  
  return result


if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  result = build_suffix_tree(text)
  print("\n".join(result))
