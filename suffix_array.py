# python3
import sys


def build_suffix_array(text):
  """
  Build suffix array of the string text and
  return a list result of the same length as the text
  such that the value result[i] is the index (0-based)
  in text where the i-th lexicographically smallest
  suffix of text starts.
  """
  l = len(text)-1
  result = []
  bwtmat = []
  answer = []
  for i in range(len(text)):
    a = text[-1]
    a += text[0:-1] 
    text = a
    bwtmat.append(a)
  bwtmat.sort()

  for i in bwtmat:
    index = i.find("$")
    result.append(l-index)
  # Implement this function yourself
  #print(bwtmat)
  return result


if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  print(" ".join(map(str, build_suffix_array(text))))
