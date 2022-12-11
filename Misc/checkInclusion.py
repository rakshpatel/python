"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false

Constraints:

    1 <= s1.length, s2.length <= 104
    s1 and s2 consist of lowercase English letters.

"""
def checkInclusion(s1: str, s2: str) -> bool:
        s1Dict = {}
        tempDict = {}
        found = 0
        for val in s1:
            s1Dict[val] = s1Dict.get(val, 0) + 1
        
        start = 0
        end = 0
        lnS2 = len(s2)
        lnS1 = len(s1)
        
        while end < lnS2:
            tempDict[s2[end]] = tempDict.get(s2[end], 0) + 1
            if s2[end] in s1Dict:
                s1Dict[s2[end]] = s1Dict.get(s2[end], 0) - 1
                if s1Dict[s2[end]] >= 0:
                    found += 1
                if found == lnS1:
                    return True
            if end - start + 1 < lnS1:
                end += 1
            elif end - start + 1 == lnS1:
                tempDict[s2[start]] = tempDict.get(s2[start]) - 1
                if s2[start] in s1Dict:
                    s1Dict[s2[start]] = s1Dict.get(s2[start], 0) + 1
                    if s1Dict[s2[start]] > 0:
                        found -= 1
                start += 1
                end += 1
            
        return False
            
            

if __name__ == "__main__":
    s1 = "ab"
    s2 = "eidbaooo"
    print(checkInclusion(s1, s2))
    
    s1 = "ab"
    s2 = "eidboaoo"
    print(checkInclusion(s1, s2))
    
    s1 = "adc"
    s2 = "dcda"
    print(checkInclusion(s1, s2))
    
    
    s1 = "abcdxabcde"
    s2 = "abcdeabcdx"
    print(checkInclusion(s1, s2))
    
    s1 = "trinitrophenylmethylnitramine"
    s2 = "dinitrophenylhydrazinetrinitrophenylmethylnitramine" 
    print(checkInclusion(s1, s2))