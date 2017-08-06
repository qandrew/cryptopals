# Detect AES in ECB mode

from base64 import b64decode
from Crypto.Cipher import AES

def detectECB(txt):
  for line in txt:
    if checkrepeat(line):
      return line
  return False

def checkrepeat(line,block=16):
  for i in xrange(0,len(line),block):
    group = line[i:i+block]
    if line.count(group) > 1:
      print '\n'
      print repr(line)
      print repr(group)
      return True
  return False
  

if __name__ == "__main__":
  with open('8.txt', 'r') as f:
    data = f.read().decode('base64')
  print len(data)
  
  f = open('8.txt','r')
  txt = []
  for line in f:
    txt.append(line[:-1].decode('base64')) #in str format, ignore \n
  f.close()
  print len(txt), len(txt[0])
  # print type(txt[0])
  # print ord(txt[-1])

  detectECB(txt)