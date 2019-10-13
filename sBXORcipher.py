from binascii import hexlify, unhexlify

# 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736

O = unhexlify('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')


a = b'1b 37 37 33 31 36 3f 78 15 1b 7f 2b 78 34 31 33 3d 78 39 78 28 37 2d 36 3c 78 37 3e 78 3a 39 3b 37 36'

e = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']

print (len(O))
def bxor(a, b):
    "bitwise XOR of bytestrings"
    return bytes([x ^ y for (x, y) in zip(a, b)])


for ii in range (1,255):
    key = bytes([ii])
    KS = key * len(O)
    print(ii, bxor(O,KS))
#
# j = 0
# for j in e:
#     s = int(j, 16)
#     print(str(j) + "= " + str(s))
# m = '10'
# print(int(m, 16))
# # alpha = b'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# # for i in alpha:
# #     print(chr(i) + " = " + str(i))
#
# x = b'0011'
# z = b'0110'
# #y = x ^ z
# print(bin(123))