# Single-byte XOR cipher


instring = 0x1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736

vals = []
s = str(hex(instring))[2:]
if s[-1] == "L":
    s = s[:-1]
assert len(s)%2 == 0

for i in xrange(0,len(s),2):
  vals.append(s[i]+s[i+1])

# print str(hex(instring))

def singleXOR(key,l):
  for elt in l:
    print chr(key ^ int(elt,16)),
  print ".\n-----"

"""
answer is 
C o o k i n g   M C ' s   l i k e   a   p o u n d   o f   b a c o n .
key X
"""

if __name__ == "__main__":

  for i in xrange(128):
    print i, chr(i)
    singleXOR(i,vals)
