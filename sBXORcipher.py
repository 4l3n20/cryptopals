from binascii import hexlify, unhexlify

# 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736

O = unhexlify('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')

ascii_txt_char = list(range(97, 122))
print(ascii_txt_char)

def doXor(a, b):
    a = bytes([x ^ y for (x, y) in zip(a, b)])
    return a


def build_list():
    return ([ii in ascii_txt_char for ii in bytes(O)])

    # Similar Loop
    # for ii in ascii_txt_char:
    # print(ii, chr(ii))


def decode(inpt_byt):
    for i in range(70, 89):  # check the 88th
        key = bytes([i])
        KS = key * len(O)
        return doXor(inpt_byt, KS)


def letter_ratio(input_bytes):
    #nb_letters = sum([x in ascii_txt_char for x in decode(unhexlify(input_bytes))])
    cnt = 0
    dec = decode(unhexlify(input_bytes))
    k = str(dec)
    for x in k[2:]:
        for i in ascii_txt_char:
            if x == chr(i):
                cnt += 1
    print(cnt)
    print(len(k[2:]))
    return cnt / len(k[2:])


def is_probably_text(input_bytes):
    r = letter_ratio(input_bytes)
    return True if r > 0.6 else False


def main():
    abs = unhexlify(input("enter a hex encoded: "))
    print(decode(abs))
    #print(letter_ratio(hexlify(abs)))
    print(is_probably_text(hexlify(abs)))


if __name__ == '__main__':
    main()