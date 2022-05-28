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
   text = filename.read()
   return text




def count_words(filename):
    text = read_file_content(filename)
    dict = {}

    text_words = str.split(text, " ")

    for word in text_words:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    return dict



print(count_words("Python\Reading-Text-Files\story.txt"))