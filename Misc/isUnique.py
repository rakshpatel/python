def isUnique1(string):
    # TC: O(N^2)
    # SC: O(1)
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            if string[i] == string[j]:
                return True
        return False


def isUnique2(string):
    # TC: O(nlogn)
    # SC: O(1)
    prev=string[0]
    for val in sorted(string)[1:]:
        if val == prev:
            return True
        prev = val
    return False


def isUnique3(string):
    # TC: O(n)
    # SC: O(n)
    wordSet=set()
    for val in string:
        if val in wordSet:
            return True
        wordSet.add(val)
    return False

if __name__ == "__main__":
    string='abcdef'
    print(isUnique1(string))

    string='abcdefa'
    print(isUnique1(string))

    string='abcdef'
    print(isUnique2(string))

    string='abcdefa'
    print(isUnique2(string))

    string='abcdef'
    print(isUnique3(string))

    string='abcdefa'
    print(isUnique3(string))