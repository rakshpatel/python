"""
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""


def lengthOfLongestSubstring(s: str) -> int:
        start = 0
        end = 0
        tempDict = {}
        longestStringLn = 0
        longestString = ""
        currentString = ""
        isDuplicate = 0
        lnString = len(s)
        
        while end < lnString:
            currentString = s[start:end+1]
            tempDict[s[end]] = tempDict.get(s[end],0) + 1
            if tempDict[s[end]] > 1:
                isDuplicate += 1
            
            if not isDuplicate:
                
                if len(currentString) > longestStringLn:
                    longestStringLn = len(currentString)
            elif isDuplicate:
                tempDict[s[start]] = tempDict.get(s[start]) - 1
                if tempDict[s[start]] > 0:
                    isDuplicate -= 1
                start += 1
            end += 1
        return longestStringLn

def isDuplicate(d):
    for key, val in d.items():
        if val > 1:
            return True
    else:
        return False

if __name__ == "__main__":
    s = "abcabcbb"
    print(lengthOfLongestSubstring(s))
    
    s = "bbbbb"
    print(lengthOfLongestSubstring(s))
    
    s = "pwwkew"
    print(lengthOfLongestSubstring(s))
    
    s = "arwvivbgvtybtnudd"
    print(lengthOfLongestSubstring(s))
