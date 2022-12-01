#The author's name is Julia Bub

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import string
# open the text file:
#EXPLANATION: this imports a built-in module called string that allows for string manipulation like splitting strings

f = open('relativity.txt')
# read the file and create a list of words (google split function in python):
#EXPLANATION: This line assignes and opens the text file named 'relativity.txt' to the variable f
#After googling a split function in python, it splits a string into a list.

words = f.read().split()
#EXPLANATION: This line reads what is inside the text file in the variable f, then splits the string(s) into a list
f.close()
#EXPLANATION: This line closes the open text file in the variable f

# calculate how many time each word is repeated (using dictionary):
word_counts = {}
#EXPLANATION: This line creates an open dictionary
for word in words:
#EXPLANATION: This line loops over every word in the relativity text file, which we split into a list above
    word_counts[word] = word_counts.get(word, 0) + 1
    #EXPLANATION: This line assigns each key, which is each word in words, a value if it is not already in our new dictionary
    #EXPLANATION: The .get method takes a key and a default value of 0. If this key we created is already in our dictionary, it will return its corresponding value + 1. If the key is not in the dictionary, it will return the default (0).


# create a list of all words:
word_list = list(word_counts.keys())
#EXPLANATION: This line creates a list of all of the keys in our dictionary word_counts

# sort the list of all words based on how many times they are repeated:
def dict_val(x):
#EXPLANATION: This line creates a function called dict_val and takes a parameter (x)
    return word_counts[x]
    #EXPLANATION: This line returns the values of the keys for the dictionary word_counts
word_list.sort(key = dict_val, reverse = True)
#EXPLANATION: This line takes our list of keys and sorts them in descending order based on their values because of the key=dict_val and reverse=True

# print the top 10 most frequently used words:
print("List of top 10 most frequently used words: ")
#EXPLANATION: This line prints the string in the ()
print(word_list[ : 10])
#EXPLANATION: This line prints the first 10 words starting from 0-9

###this doesn't provide much information about the text because all of these are stop words


###second attempt###
#contents = open('relativity.txt').read()
#translation_table = {ord(ch) : None  for ch in string.punctuation}
#contents = contents.translate(translation_table)
#words = contents.split()

# create a list of all words in lower case:
lowercase_words = [word.lower() for word in words]
#EXPLANATION: .lower returns a string in all lowercase, so the for loop will make every word in the list called words lowercase

# open the file containing all of the stop words in English language:
f = open('stopWords.txt')
#EXPLANATION: This line opens and assignes the text file 'stopWords.txt' to the variable f

# read the file create the list of all stop words in English language:
stop_words = f.read().split()
#EXPLANATION: This line reads what is inside the text file in the variable f, then splits the string(s) into a list


###remove stop words###
# create the list of non stop words by filtering out the stop words:
non_stop_words = [word for word in lowercase_words if word not in stop_words]
#EXPLANATION: This line creates a list of words from lowercase_words that are not in the list stop_words

# now calculate the frequency of the non stop words:
word_counts = {}
#EXPLANATION: This line creates an empty dictonary

for word in non_stop_words:
#EXPLANATION: This line loops through each word in the list non_stop_words
    word_counts[word] = word_counts.get(word, 0) + 1
    #EXPLANATION: This line assigns each key, which is each word in non_stop_words, a value if it is not already in our new dictionary
    #EXPLANATION: The .get method takes a key and a default value of 0. If this key we created is already in our dictionary, it will return its corresponding value + 1. If the key is not in the dictionary, it will return the default (0).


word_list = list(word_counts.keys())
#EXPLANATION: This line creates a list of all of the keys in our dictionary word_counts


# sort the words again:
word_list.sort(key = dict_val, reverse = True)
#EXPLANATION: This line takes our list of keys and sorts them in descending order based on their values because of the key=dict_val and reverse=True

# prin the top 10 most frequently used words:
print("\nList of top 10 most frequently used non stop words: ")
#EXPLANATION: This line prints the string in the ()
print(word_list[ : 10])
#EXPLANATION: This line prints the first 10 words starting from 0-9
