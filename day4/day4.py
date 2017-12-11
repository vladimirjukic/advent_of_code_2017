def isAnagram(word1, word2):
    word1 = ''.join(sorted(word1))
    word2 = ''.join(sorted(word2))
    return word1 == word2

def isMatch(word1, word2):
    return word1 == word2

def calculateValidPassphrases(data, validFunction, part):
    result = 0
    for row in data:
        words = row.split(" ")
        i = 0
        isValid = True
        while i < len(words):
            j = i + 1
            while j < len(words):
                if validFunction(words[i], words[j]):
                    isValid = False
                j += 1
            i += 1
            
        if isValid:
            result += 1
    
    print "Valid passphrases", part, ":", result

f = open('input.txt', 'r')
content = f.read().splitlines()
f.close()

calculateValidPassphrases(content, isMatch, "part one")
calculateValidPassphrases(content, isAnagram, "part two")