def strXor():
    a = '1c0111001f010100061a024b53535009181c'
    b = '686974207468652062756c6c277320657965'

    print("".join(["%x" % (int(x, 16) ^ int(y, 16)) for (x, y) in zip(a[:len(b)], b)]))

    print(" ".join(["%x" % (int(x, 16) ^ int(y, 16)) for (x, y) in zip(a[:len(b)], b)]))

    print("|".join(["%x" % (int(x, 16) ^ int(y, 16)) for (x, y) in zip(a[:len(b)], b)]))


def main():
    strXor()


if __name__ == '__main__':
    main()



