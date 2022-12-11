"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""
import string
tempDict = {str(key):val for key, val in enumerate(string.ascii_lowercase, 1)}
def transform(s, outString):
    if not s:
        print(outString)
        return
    
    if len(s) >= 2:
        transform(s[2:], outString + tempDict[s[:2]])

    transform(s[1:], outString + tempDict[s[0]])


if __name__ == "__main__":
    transform("111", "")
    print()
    transform("1111", "")
    print()
    transform("123", "")
    print()
    transform("", "")
    print()
