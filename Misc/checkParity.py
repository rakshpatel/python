def parity1(x):
    result = 0
    while x:
        result ^=  x & 1
        x >>=  1
    return result

def parity2(x):
    result = 0
    while x:
        result ^= 1
        x &= x-1
    return result

if __name__ == "__main__":
    print("Example 1")
    print("Parity status {}".format(parity1(1)))
    print("Parity status {}".format(parity1(2)))
    print("Parity status {}".format(parity1(3)))
    print("Parity status {}".format(parity1(4)))
    print("Parity status {}".format(parity1(4836235692057875857979)))

    print("Example 2")
    print("Parity status {}".format(parity2(1)))
    print("Parity status {}".format(parity2(2)))
    print("Parity status {}".format(parity2(3)))
    print("Parity status {}".format(parity2(4)))
    print("Parity status {}".format(parity1(4836235692057875857979)))