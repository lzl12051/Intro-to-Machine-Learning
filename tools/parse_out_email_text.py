#!/usr/bin/python

from nltk.stem.snowball import SnowballStemmer
import string

def parseOutText(f):
    """ given an opened email file f, parse out all text below the
        metadata block at the top
        (in Part 2, you will also add stemming capabilities)
        and return a string that contains all the words
        in the email (space-separated) 
        
        example use case:
        f = open("email_file_name.txt", "r")
        text = parseOutText(f)
        
        """


    f.seek(0)  ### go back to beginning of file (annoying)
    all_text = f.read()

    ### split off metadata
    content = all_text.split("X-FileName:")
    words = ""
    if len(content) > 1:
        ### remove punctuation
        text_string = content[1].translate(str.maketrans("", "", string.punctuation))

        ### project part 2: comment out the line below
        #words = text_string

        ### split the text string into individual words, stem each word,
        ### and append the stemmed word to words (make sure there's a single
        ### space between each stemmed word)
    str_list = text_string.split(" ")
    #print(str_list)
    #不知道为什么会有空的元素夹杂在里边，所以写个循环删掉空的元素
    for txt in str_list:
        if txt == "":
            str_list.remove("")
    
    stemmer = SnowballStemmer("english")
    for x in range(0,len(str_list)):
        str_list[x] = stemmer.stem(str_list[x])
        
    # 将一个列表转换为字符串并且用空格隔开
    words = " ".join(str_list)
    #words = str_list
    
    #print("The type is", type(str_list))
    return words

    

def main():
    ff = open("../text_learning/test_email.txt", "r")
    text = parseOutText(ff)
    print(text)



if __name__ == '__main__':
    main()

