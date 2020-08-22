# pip install wordcloud

import numpy as np
import io
import sys
from matplotlib import pyplot as plt
from IPython.display import display
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image

def calculate_frequencies(f):
    # Here is a list of punctuations and stop words you can use to process the text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    stopwords = set(STOPWORDS)
    # extra words that don't have relavance to the text file but appear alot
    stopwords.add('illustration')

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
                if (saveWord not in freqDict) and (saveWord not in stopwords):
                    freqDict[saveWord] = 1
                # word already in dictionary
                elif (saveWord in freqDict):
                    freqDict[saveWord] += 1
                # word not in dictionary and is a stop word word, don't do anything
                # restart saved word var
                saveWord = ""
    
    scarlet_letter_coloring = np.array(Image.open("scarletBW.jpg"))

    # wordcloud
    cloud = WordCloud(background_color="white", max_words=1000, mask=scarlet_letter_coloring,
               stopwords=stopwords, max_font_size=40, random_state=42)
    cloud.generate_from_frequencies(freqDict)
    # save wordcloud jpg
    cloud.to_file("scarlet_wordcloud.jpg")
    return cloud.to_array()


filename = "scarlet.txt"
# open text file
f = open(filename, "r")
myimage = calculate_frequencies(f.read())
# close file
f.close()

# display wordcloud image
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()