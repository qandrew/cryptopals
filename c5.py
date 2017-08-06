# Implement repeating-key XOR

def toArray(text):
  ar = []
  for let in text:
    ar.append(ord(let))
  return ar

def repeatKeyEnc(key,intArr):
  enc = []
  i = 0
  for num in intArr:
    # print repr(let)
    # enc.append("%02x" %(ord(let) ^ ord(key[i])))
    enc.append((num ^ ord(key[i])))
    i = (i + 1)%len(key)
  return enc

def repeatKey(key,s):
  enc = ""
  i = 0
  for let in s:
    # print repr(let)
    # enc.append("%02x" %(ord(let) ^ ord(key[i])))
    enc += "%02x" %(ord(let) ^ ord(key[i]))
    i = (i + 1)%len(key)
  return enc

if __name__ == "__main__":
  plain = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
  t = toArray(plain)
  print repeatKey("ICE",plain)
  # print t
  # a = repeatKeyEnc("ICE",t)
  # print a
  # print repeatKeyEnc("ICE",a)
