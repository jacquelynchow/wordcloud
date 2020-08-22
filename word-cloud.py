# pip install wordcloud

import numpy as np
import io
import sys
from matplotlib import pyplot as plt
from IPython.display import display
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image

def calculate_frequencies(f, textName, extraWords):
    # Here is a list of punctuations and stop words you can use to process the text
    punctuations = '''!()-[]“{};:"\,<>./?@#$%^&*_~'''
    stopwords = set(STOPWORDS)
    # extra words that don't have relavance to the text file but appear alot
    for word in extraWords:
        stopwords.add(word)
    # init the dictionary that will show frequency of words
    freqDict = {}

    # Before processing any text, remove all the punctuation marks. To do this, go through each line of text, 
    # character-by-character, using the isalpha() method
    # Before storing words in the frequency dictionary, check if they’re part of 
    # the "uninteresting" set of words
    
    # split up file into a large list of words, then go through each word
    for word in f.split():
        saveWord = ""
        for letter in word:
            # make sure all letters are lower case
            letter = letter.lower()
            # not a punct. or space, must be a letter, so save to save word var
            if not ((letter in punctuations) or (letter == " ")):
                saveWord += letter
            # end of the word, got either a punct. or space
            else:
                # new word, need to save in dictionary
                if (saveWord not in freqDict) and (saveWord not in stopwords) and (len(saveWord) > 1):
                    freqDict[saveWord] = 1
                # word already in dictionary
                elif (saveWord in freqDict):
                    freqDict[saveWord] += 1
                # word not in dictionary and is a stop word word, don't do anything
                # restart saved word var
                saveWord = ""
    
    # for masking images
    # image = "mask-images/" + textName + "BW.jpg"
    # letter_coloring = np.array(Image.open(image))
    # add "mask=letter_coloring," to WordCloud() parameters

    # wordcloud
    cloud = WordCloud(background_color="white", width=600, height= 400, max_words=800, 
               stopwords=stopwords, max_font_size=130, min_font_size=3, random_state=42, scale=3)
    cloud.generate_from_frequencies(freqDict)
   
    # save wordcloud jpg
    saveImage = textName + "_wordcloud.jpg"
    cloud.to_file(saveImage)
    return cloud.to_array()

# textName = "scarlet"
# extraWords = ["illustration", "say", "thus", "might", "moreover", "days", "thought", "ago", "part", "one", "come", "mr", "said", "likewise", \
#     "meanwhile", "yet", "perhaps", "stood", "-and", "rather", "nevertheless"]

# textName = "iliad"
# extraWords = ["pg", "said", "spoke", "thus", "thee", "threw", "know"]

# textName = "oz"
# extraWords = ["said", "asked", "know", "replied", "answered", "em", "knew"]

# textName = "mobydick"
# extraWords = ["say", "one", "said", "though", "oh", "come", "see", "mister", "meanwhile", "days" \
#     "will", "besides", "mr", "side", "yet", "thing", "way", "look", "day", "indeed"]
# filename = "textfiles/" + textName + ".txt"

# INPUT DATA HERE
textName = "input"
extraWords = ["word"]

# open text file
f = open(filename, "r")
myimage = calculate_frequencies(f.read(), textName, extraWords)
# close file
f.close()

# display wordcloud image
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()