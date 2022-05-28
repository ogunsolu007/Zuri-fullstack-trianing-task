# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

# f = open("Python\Reading-Text-Files\story.txt","r") 
# cont = f.readlines()
# con = f.read()
 # co = f.readline()
import json


def read_file_content(filename):
    # [assignment] Add your code here 
   filename = open(filename,"r")
   text = filename.readlines()
   return text




def count_words():
    text = read_file_content("Python\Reading-Text-Files\story.txt")
   
    text_word = text[0].split()
    result = json.loads(text_word)
    
    print(text)
    
    return {"as": 10, "would": 20}

count_words()