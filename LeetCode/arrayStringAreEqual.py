def arrayStringsAreEqual(word1, word2):
        word1Pointer = word2Pointer = string1Pointer = string2Pointer = 0
        while word1Pointer < len(word1) and word2Pointer < len(word2):
            if word1[word1Pointer][string1Pointer] != word2[word2Pointer][string2Pointer]:
                return False
            
            string1Pointer += 1
            string2Pointer += 1 
            
            if string1Pointer == len(word1[word1Pointer]):
                word1Pointer += 1
                string1Pointer = 0
        
            
            if string2Pointer == len(word2[word2Pointer]):
                word2Pointer += 1
                string2Pointer = 0
            
            
            
        
        return word1Pointer == len(word1) - 1 and word2Pointer == len(word2) - 1


word1 = ["ab", "c"]; word2 = ["a", "bc"]

arrayStringsAreEqual(word1, word2)