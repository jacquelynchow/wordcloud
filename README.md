# Wordcloud Project
*Description:* Displays and saves an image that's made up of different sized words (sizes of the words are determined by the frequency of each word in a specific text)

## Features:
- Wordcloud library (WordCloud generator and Stop Words)
- Instead of using Wordcloud's built in word cloud generator, I coded my own frequency dictionary for the word cloud
- Masked image feature (example done for Scarlet Letter wordcloud)

## Texts Done So Far:
*Text files from Project Gutenberg*
- The Scarlet Letter (by Nathaniel Hawthorne)
- The Wonderful Wizard of Oz (by L. Frank Baum)
- The Iliad (by Homer)
- Moby Dick; Or, The Whale (by Herman Melville)

## How To Use With Your Own Text Files
1) Add your own text file into the textfiles folder (remove any extra unwanted text in the file)
In the .py file, 
2) Add the name of the .txt file to the textName variable 
3) Add your own stop words into the extraWords list
4) Run the program by doing python3 word-cloud.py
### Optional:
Play around in the calculate_frequencies() with the parameters for WordCloud() -- the max_font_size, min_font_size, max_words -- or add more words to the extraWords list for a better word cloud display