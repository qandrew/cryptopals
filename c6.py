# Break repeating-key XOR

import base64
import c5, c4
import itertools

def hamdist(str1, str2):
  """Count the # of differences between equal length strings str1 and str2"""
  s1 = ""
  for let in str1:
    s1 += format(ord(let),'#010b')[2:]
  s2 = ""
  for let in str2:
    s2 += format(ord(let),'#010b')[2:]
  diffs = 0
  for ch1, ch2 in zip(s1, s2):
    if ch1 != ch2:
      diffs += 1
  return diffs

assert hamdist("this is a test","wokka wokka!!!") == 37

def hamdistArr(a1, a2):
  """Count the # of differences between equal length strings str1 and str2"""
  s1 = ""
  for let in a1:
    s1 += format(let,'#010b')[2:]
  s2 = ""
  for let in a2:
    s2 += format(let,'#010b')[2:]
  diffs = 0
  for ch1, ch2 in zip(s1, s2):
    if ch1 != ch2:
      diffs += 1
  return diffs

def findKeySize(file,k):
  shortblock = [file[i:i+k] for i in xrange(0,k*4,k)]
  pairs = list(itertools.combinations(shortblock, 2))
  scores = [hamdist(p[0], p[1])/float(k) for p in pairs][0:6]
  return sum(scores)/len(scores)

def breakStringFindXor(file,k):
  """
    given file, the ciphertext
    k, the key length
    transpose block to be of size k, and solve single character xor
  """
  newBlock = [file[i:i+k] for i in xrange(0,len(file),k)]
  print repr(newBlock[0]), len(newBlock[0])
  transposedBlocks = list(itertools.izip_longest(*newBlock, fillvalue=0))
  print len(transposedBlocks)
  print transposedBlocks[0]
  for x in transposedBlocks:
    print c4.bruteForceSingleXOR(bytes(x))
  # key = [c4.bruteForceSingleXOR(bytes(x))[0] for x in transposedBlocks]

if __name__ == "__main__":
  file = base64.b64decode(open('6.txt', 'r').read())  

  k = min(range(2, 41), key=lambda k: findKeySize(file, k)) #find keysize
  breakStringFindXor(file,k)
  