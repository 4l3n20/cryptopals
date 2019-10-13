
# Functionality: Convert hex to base64 + vice versa
# An answer to the challenge proposed on the below address
# https://cryptopals.com/sets/1/challenges/1
# The string:
# 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
#
# Should produce:
# SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
#


from codecs import encode, decode
import base64
import binascii

Message_hex = "Enter a Hex Value/String: "
Message_bs64 = "Enter a base64 data string to convert to hex: "
Message_bs64_2str = "Enter a base64 data string to convert to string: "
Message_str = "Enter a String: "
Err = "entered value must only contain Hex e.g.(0..9 - A..F)"


def read(i):                                                         # Read From User.
    i = i
    if i == '1':
        HEXag = input(Message_hex)
        return HEXag
    if i == '2':
        bs64 = input(Message_bs64)
        return bs64
    if i == '3':
        strg = input(Message_str)
        return strg
    if i == '4':
        b642str = input(Message_bs64_2str)
        return b642str


def is_hexa(inp):                                                    # Check if input is an actual HEX value.
    try:
        int(inp, 16)
        return True
    except ValueError:
        return False


def hex2b64(i):                                                      # make sure input is Hex then convert it to BASE64
    i = i
    hx = read(i)
    if is_hexa(hx):                                                  # make sure input is Hex
        bas64 = encode(decode(hx, 'hex'), 'base64').decode()         # Convert it to BASE64
        print("\n")
        return bas64
    else:
        return Err


def bas62hex(i):                                                     # Convert base64 to hex
    i = i
    bs = read(i)
    h3x = base64.b64decode(bs).hex()
    return h3x


def str2bs64(i):
    i = i
    str = read(i).encode('utf-8')
    bas64 = base64.b64encode(str).decode('utf-8')
    return bas64


def bs642str(i):
    i = i
    bs64 = read(i).encode('UTF-8')
    str = base64.b64decode(bs64).decode('utf-8')

    return str


def menu():
    print("[1] Hex2base64")
    print("[2] base64-2-hex")
    print("[3] String2base64")
    print("[4] base64-2-String")
    print("[q] Exit.  *Acceptable options (q, e, E, quit, exit, Exit)")
    print("Select from menu: ")


def main():
    menu()
    opt = input()
    while opt != 'q' or 'exit' or 'E' or 'e' or 'Exit' or 'quit':
        if opt == '1':
            print("OUTPUT: " + hex2b64(opt) + '\n')
            main()
        elif opt == '2':
            print("OUTPUT: " + bas62hex(opt) + '\n')
            main()
        elif opt == '3':
            print("OUTPUT: " + str2bs64(opt) + '\n')
            main()
        elif opt == '4':
            print("OUTPUT: " + bs642str(opt) + '\n')
        print("Bye!")
        exit()


if __name__ == '__main__':
    main()



