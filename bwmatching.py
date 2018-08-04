# python3
import sys
from collections import OrderedDict


def PreprocessBWT(bwt):
  """
  Preprocess the Burrows-Wheeler Transform bwt of some text
  and compute as a result:
    * starts - for each character C in bwt, starts[C] is the first position 
        of this character in the sorted array of 
        all characters of the text.
    * occ_count_before - for each character C in bwt and each position P in bwt,
        occ_count_before[C][P] is the number of occurrences of character C in bwt
        from position 0 to position P inclusive.
  """
  # Implement this function yourself
  sort = list(bwt)
  sort.sort()
  s = ""
  for char in sort:
    s += char

  starts = {}
  occ_count_before =[(0)*len(''.join(OrderedDict.fromkeys(bwt).keys()))]*len(bwt)
  #print(occ_count_before)
  #sys.exit()
  #for char in bwt:
  #  t.append(0)
  for i in range(len(bwt)):
    index = bwt[i]
    starts[index]=s.find(index)
    t = ''.join(OrderedDict.fromkeys(bwt).keys())
    if i==0:
      occ_count_before[i][t.find(index)]+=1
    else:
      occ_count_before[i][t.find(index)] = (1 + occ_count_before[i-1][t.find(index)])
    
      
  
  print (starts,occ_count_before)
  sys.exit()
  return starts,occ_count_before



def CountOccurrences(pattern, bwt, starts, occ_counts_before):
  """
  Compute the number of occurrences of string pattern in the text
  given only Burrows-Wheeler Transform bwt of the text and additional
  information we get from the preprocessing stage - starts and occ_counts_before.
  """
  top = 0
  bottom = len(bwt)-1
  #print(top,bottom)
  while top <= bottom:
    if pattern != "":
      #print(pattern)
      symbol = pattern[-1]
      pattern = pattern[:-1]
      #print (symbol)
      if symbol in bwt[top:bottom]:
        top = starts[symbol]+bwt[:top].count(symbol)
        bottom = starts[symbol]+bwt[:bottom+1].count(symbol)-1
        #print (top,bottom)
      else:
        return 0
    else:
      return bottom - top + 1

  #print(pattern)
  #print(top,bottom)
  
  # Implement this function yourself
  
     


if __name__ == '__main__':
  bwt = sys.stdin.readline().strip()
  pattern_count = int(sys.stdin.readline().strip())
  patterns = sys.stdin.readline().strip().split()
  # Preprocess the BWT once to get starts and occ_count_before.
  # For each pattern, we will then use these precomputed values and
  # spend only O(|pattern|) to find all occurrences of the pattern
  # in the text instead of O(|pattern| + |text|).  
  starts, occ_counts_before = PreprocessBWT(bwt)
  occurrence_counts = []
  for pattern in patterns:
    occurrence_counts.append(CountOccurrences(pattern, bwt, starts, occ_counts_before))
  print(' '.join(map(str, occurrence_counts)))
