# Detect single-character XOR

englishLetterFreq = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}


def parseHex(instring):
  if instring[-1] == '\n':
    instring = instring[:-1]
  # print instring, len(instring)
  assert len(instring) %2 == 0

  vals = []
  # allprint = True
  for i in xrange(0,len(instring),2):
    vals.append(instring[i]+instring[i+1])
    # if int(instring[i],16) < 2 or int(instring[i],16) > 7:
      #ascii property
      # allprint = False

  return vals#, allprint

def printHex(vals):
  for elt in vals:
    print elt, chr(int(elt,16))
  print ".\n---"

def singleXOR(key,l):
  s = ""
  t = True
  for elt in l:
    e = chr(key ^ int(elt,16))
    s += e
    if ord(e) < 31 or ord(e) > 127:
      if ord(e) != 10 and ord(e) != 13:
        t = False

  # print ".\n-----"
  return t, s

def bruteForceSingleXOR(l):
  maxkey = 0
  maxscore = 0
  for k in xrange(256):
    t,res = singleXOR(k,l)
    if t:
      sc = score(res)
      if sc > maxscore:
        maxkey = k
        maxscore = sc
  return maxkey
  # def key(p):
  #       return score(p[1])
  # return max([(i, strxor_c(s, i)) for i in range(0, 256)], key=key)

def score(s):
  tot = 0
  # print s, len(s)
  for let in s:
    if let.upper() in englishLetterFreq:
      tot += englishLetterFreq[let.upper()]
  return tot

if __name__ == "__main__":
  f = open('4.txt','r')
  txt = []
  for line in f:
    txt.append(line) #in str format
  f.close()

  txt2 = []
  for t in txt:
    t1 = parseHex(t)
    txt2.append(t1)
  print len(txt2)

  bestSc = 0
  bestStr = ""

  for l in xrange(len(txt2)):
    for k in xrange(128):
      t, res = singleXOR(k,txt2[l])
      if t:
        sc = score(res)
        if sc > bestSc:
          bestSc = sc
          bestStr = res
  print bestStr

  for l in xrange(len(txt2)):
    print bruteForceSingleXOR(txt2[l]),



# import c3

# 0e3647e859
# 2d35514a08
# 1243582536
# ed3de67340
# 59001e3f53
# 5ce6271032