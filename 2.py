# https://cryptopals.com/sets/1/challenges/2
# fixed xor

feed = 0x1c0111001f010100061a024b53535009181c
xor  = 0x686974207468652062756c6c277320657965
goal = 0x746865206b696420646f6e277420706c6179

x1 = feed ^ xor

print hex(x1)