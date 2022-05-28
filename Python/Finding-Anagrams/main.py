# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True



def find_anagram(word, anagram):
    if len(word) == len(anagram):
        if sorted(word) == sorted(anagram):
            return True
        else:
            return False
    else:
       return False

print(find_anagram("ade","eda"))