from binascii import hexlify, unhexlify

# 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736

O = unhexlify('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')

print(len(O))


def doXor(a, b):
    return bytes([x ^ y for (x, y) in zip(a, b)])


for i in range(1, 255):  # check the 88th
    key = bytes([i])
    KS = key * len(O)
    print(i, " __ ", doXor(O,KS))
