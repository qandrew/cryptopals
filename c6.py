# Break repeating-key XOR

import base64
import c5

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

s1 = "this is a test"
s2 = "wokka wokka!!!"
# print hamdist(s1,s2)

if __name__ == "__main__":
  f = open('6.txt','r')
  txt = []
  t64 = []
  for line in f:
    txt.append(line) #in str format
    t64.append(base64.b64decode(line))
  f.close()

  # b = 'HUIfTQsPAh9PE048GmllH0kcDk4TAQsHThsBFkU2AB4BSWQgVB0dQzNTTmVS'  
  # g = 'BgBHVBwNRU0HBAxTEjwMHghJGgkRTxRMIRpHKwAFHUdZEQQJAGQmB1MANxYG'
  # bD = base64.b64decode(b)
  # gD = base64.b64decode(g)
  # print hamdist(bD, gD)


  q1 = [66, 117, 114, 110, 105, 110, 103, 32, 39, 101, 109, 44, 32, 105, 102, 32, 121, 111, 117, 32, 97, 105, 110, 39, 116, 32, 113, 117, 105, 99, 107, 32, 97, 110, 100, 32, 110, 105, 109, 98, 108, 101, 10, 73, 32, 103, 111, 32, 99, 114, 97, 122, 121, 32, 119, 104, 101, 110, 32, 73, 32, 104, 101, 97, 114, 32, 97, 32, 99, 121, 109, 98, 97, 108]
  q2 = [11, 54, 55, 39, 42, 43, 46, 99, 98, 44, 46, 105, 105, 42, 35, 105, 58, 42, 60, 99, 36, 32, 45, 98, 61, 99, 52, 60, 42, 38, 34, 99, 36, 39, 39, 101, 39, 42, 40, 43, 47, 32, 67, 10, 101, 46, 44, 101, 42, 49, 36, 51, 58, 101, 62, 43, 32, 39, 99, 12, 105, 43, 32, 40, 49, 101, 40, 99, 38, 48, 46, 39, 40, 47]
  print hamdistArr(q1,q2)

  # part 2
  bestsize = 1000000000000
  bestkey = 0
  
  for KEYSIZE in xrange(2,40):
    for line in t64:
      sc = float(hamdist(line[:KEYSIZE],line[KEYSIZE:2*KEYSIZE]))/KEYSIZE
      if sc < bestsize:
        bestsize = sc
        bestkey = KEYSIZE
  print bestkey, bestsize


"""
KEYSIZE is length of key


"""