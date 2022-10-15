#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: shwethakrishnan
"""

def clean_text(txt):
        """  takes a string of text txt as a parameter and returns a list
        containing the words in txt after it has been “cleaned”. 
        """
        cleaned_text = txt.lower()
        for character in txt:
            if character in '.,!?@#$%^&*()_-+={}[]':
                cleaned_text = cleaned_text.replace(character,'')
        return cleaned_text.split()
    
def stem(s):
    """accepts a string as a parameter. The function should then return the 
    stem of s. The stem of a word is the root part of the word, which excludes
    any prefixes and suffixes.
    """
    if s[-1:] == 'y':
        s = s[:-1] + 'i'
    elif s[-1:] == 'e':
        if len(s) >3:
         s = s[:-1]
    elif s[-3:] == 'ing':
        if len(s) > 6:
            if s[-4] == s[-5]:
                s = s[:-4]
            else:
                s = s[:-3]
    elif s[-2:] == 'er':
        if len(s) > 5:
            if s[-3] == s[-4]:
                s = s[:-3]
            else:
                s = s[:-2]
    elif s[-3:] == 'ers':
        if len(s) > 6:
            if s[-4] == s[-5]:
                s = s[:-4]
            else:
                s = s[:-3]
    elif s[-1:] == 's':
        if len(s) > 4:
            if s[-3:] == 'ies':
                s = s[:-2]
            else:
                s = s[:-1]
    elif s[-3:] == 'ful':
        if len(s) > 6:
            if s[-4] == s[-5]:
                s = s[:-4]
            else:
                s = s[:-3]
    elif s[-3:] == 'ish':
        if len(s) > 6:
            if s[-4] == s[-5]:
                s = s[:-4]
            else:
                s = s[:-3]
                
    elif s[-3:] == 'ant':
        if len(s) > 6:
            if s[-4] == s[-5]:
                s = s[:-4]
            else:
                s = s[:-3]
                
    elif s[-3:] == 'est':
        if len(s) > 6:
            if s[-4] == s[-5]:
                s = s[:-4]
            else:
                s = s[:-3]
    
    elif s[-2:] == 'ed':
        if len(s) > 5:
            if s[-3] == s[-4]:
                s = s[:-3]
            else:
                s = s[:-2]
    elif s[-2:] == 'ly':
        if len(s) > 5:
            if s[-3] == s[-4]:
                s = s[:-3]
            else:
                s = s[:-2]
    elif s[-2:] == 'al':
        if len(s) > 5:
            if s[-3] == s[-4]:
                s = s[:-3]
            else:
                s = s[:-2]
                
    elif s[-4:] == 'tion':
        if len(s) > 5:
            s = s[:-4]
    elif s[-4:] == 'able':
        if len(s) > 5:
            s = s[:-4]
    elif s[-4:] == 'ment':
        if len(s) > 5:
            s = s[:-4]
    elif s[-4:] == 'ious':
        if len(s) > 5:
            s = s[:-4]
    elif s[-2:] == 'ous':
        if len(s) > 5:
            if s[-3] == s[-4]:
                s = s[:-3]
            else:
                s = s[:-2]
    return s

import math 

def compare_dictionaries(d1, d2):
    """take two feature dictionaries d1 and d2 as inputs, and it should compute 
    and return their log similarity score."""
    score = 0
    total = 0
    for item in d1:
        total += d1[item]
    for item in d2:
        if item in d1:
            score +=  math.log(d1[item] / total) * d2[item]
        else:
            score += math.log(0.5 / total) * d2[item] 
    return score

  
        
class TextModel:
    
    def __init__(self, model_name):
        """constructs a new TextModel object by accepting a string model_name as a parameter 
        """
        self.name = model_name
        self.words = {}
        self.word_lengths = {}
        self.stems = {}
        self.sentence_lengths = {}
        self.max_probability_common_words = {}
        
        
    def __repr__(self):
        """returns a string that includes the name of the model as well 
        as the sizes of the dictionaries for each feature of the text.
        """
        s = 'text model name: ' + self.name + '\n'
        s += '  number of words: ' + str(len(self.words)) + '\n'
        s += '  number of word lengths: ' + str(len(self.word_lengths)) + '\n'
        s += '  number of stems: ' + str(len(self.stems)) + '\n'
        s += '  number of sentence lengths: ' + str(len(self.sentence_lengths)) + '\n'
        s += '  number of most common words: ' + str(len(self.max_probability_common_words)) + '\n' 
        return s
    
    
    def add_string(self, s):
            """ adds a string of text s to the model by augmenting the feature 
            dictionaries defined in the constructor.
            """
            sentence = s.split()
            empty_list = []
            count = 0
            for character in sentence:
                if character[-1] not in '?.!':
                    count += 1
                else:
                    count += 1
                    empty_list += [count]
                    count = 0
            
            for i in empty_list:
                if i in self.sentence_lengths:
                    self.sentence_lengths[i] += 1
                else:
                    self.sentence_lengths[i] = 1
                    
            # Add code to clean the text and split it into a list of words.
            # *Hint:* Call one of the functions you have already written!
            word_list = clean_text(s)
            # Template for updating the words dictionary.
            # Update self.words to reflect w
            # either add a new key-value pair for w
            # or update the existing key-value pair.
            for w in word_list:
                if w in self.words:
                    self.words[w] += 1 
                else:
                    self.words[w] = 1   
                # Add code to update other feature dictionaries.
                word_len = len(w)
                if word_len in self.word_lengths:
                    self.word_lengths[word_len] += 1
                else:
                    self.word_lengths[word_len] = 1
                #for w in s:
                if stem(w) not in self.stems:
                    self.stems[stem(w)] = 1
                else:
                    self.stems[stem(w)] += 1
                    
                common_words = []
                 
            # to find the most common word
                
            num_words = 0
            for words in self.words:
                num_words += self.words[words]
            black_listed_words = ['and','the','of','and','but','for','to','at','a', 'too','also','is','in','that','from','its','as','not','with']  
            for words in self.words:
                if (self.words[words]/num_words) >= 0.01 and words not in black_listed_words :
                    common_words += [words]
                    
            for word in common_words:
                self.max_probability_common_words[word] = self.words[word]
                
            
    def add_file(self, filename):
        """ adds all of the text in the file identified by filename
        to the model. It should not explicitly return a value.
        """
        f = open(filename, 'r', encoding='utf8', errors='ignore')
        #  use the read() method to read in the entire file into a single string
        file_read = f.read()
        # Take advantage of add_string()
        self.add_string(file_read)
        
    
    def save_model(self):
        """  saves the TextModel object self by writing its various feature 
        dictionaries to files. 
        """
        filename_one = self.name + '_' + 'words'
        f_one = open(filename_one, 'w') 
        f_one.write(str(self.words))
        f_one.close()
        
        filename_two = self.name + '_' + 'word_lengths'
        f_two = open(filename_two, 'w')
        f_two.write(str(self.word_lengths))
        f_two.close()
        
        filename_three = self.name + '_' + 'stems'
        f_three = open(filename_three, 'w')
        f_three.write(str(self.stems))
        f_three.close()
        
        filename_four = self.name + '_' + 'sentence_lengths'
        f_four = open(filename_four, 'w')
        f_four.write(str(self.sentence_lengths))
        f_four.close()
        
        filename_five = self.name + '_' + 'most_common_word'
        f_five = open(filename_five, 'w')
        f_five.write(str(self.max_probability_common_words))
        f_five.close()
    def read_model(self):
        """ reads the stored dictionaries for the called TextModel 
        object from their files and assigns them to the attributes of 
        the called TextModel.
        """
        filename_one = self.name + '_' + 'words'
        f_one  = open(filename_one, 'r')
        self.words_read = f_one .read()
        f_one .close
        
        
        filename_two = self.name + '_' + 'word_lengths'
        f_two= open(filename_two, 'r')
        self.word_lengths_read = f_two.read()
        f_two.close()
        
        filename_three = self.name + '_' + 'stems'
        f_three = open(filename_three, 'r')
        self.stems_read = f_three.read()
        f_three.close()
        
        filename_four = self.name + '_' + 'sentence_lengths'
        f_four = open(filename_four, 'r')
        self.sentence_lengths_read = f_four.read()
        f_four.close()
        
        filename_five = self.name + '_' + 'most_common_word'
        f_five = open(filename_five, 'r')
        self.max_probability_common_words_read = f_five.read()
        f_five.close()
        
        self.words = dict(eval(self.words_read))
        self.word_lengths = dict(eval(self.word_lengths_read))
        self.stems = dict(eval(self.stems_read))
        self.sentence_lengths = dict(eval(self.sentence_lengths_read))
        self.max_probability_common_words = dict(eval(self.max_probability_common_words_read))
        
    def similarity_scores(self, other):
        """computes and returns a list of log similarity scores measuring the 
        similarity of self and other – one score for each type of feature (words,
        word lengths, stems, sentence lengths, and your additional feature).  """
        word_score = compare_dictionaries(other.words, self.words)
        word_lengths_score = compare_dictionaries(other.word_lengths, self.word_lengths)
        stems_score = compare_dictionaries(other.stems, self.stems)
        sentence_lengths_score = compare_dictionaries(other.sentence_lengths, self.sentence_lengths)
        max_probability_common_words_score = compare_dictionaries(other.max_probability_common_words, self.max_probability_common_words)
        score_lst = [word_score, word_lengths_score, stems_score, sentence_lengths_score,max_probability_common_words_score]
        return score_lst
        
    
    def classify(self, source1, source2):
        """ that compares the called TextModel object (self) to two other 
        “source” TextModel objects (source1 and source2) and determines which
        of these other TextModels is the more likely source of the called 
        TextModel."""
        scores1 = self.similarity_scores(source1)
        scores2 = self.similarity_scores(source2)
        print('scores for source1: ' , scores1)
        print('scores for source2: ' , scores2)
        count1 = 0
        count2 = 0
        if scores1[0] > scores2[0]:
            count1 += 1
        else:
            count2 += 1
        if scores1[1] > scores2[1]:
            count1 += 1
        else:
            count2 += 1
        if scores1[2] > scores2[2]:
            count1 += 1
        else:
            count2 += 1
        if scores1[3] > scores2[3]:
            count1 += 1
        else:
            count2 += 1
        if scores1[4] > scores2[4]:
            count1 += 1
        else:
            count2 += 1
        
        if count1 > count2:
            print(self.name, 'is more likely to have come from', source1.name)
        else:
            print(self.name, 'is more likely to have come from', source2.name)
            
# testing           
# Copy and paste the following function into finalproject.py
# at the bottom of the file, *outside* of the TextModel class.
def run_tests():
    """ your docstring goes here """
    source1 = TextModel('Female Poets of India')
    source1.add_file('female_poets_of_india.txt')

    source2 = TextModel('Male poets of India')
    source2.add_file('male_poets_of_india.txt')

    new1 = TextModel('Female Poets of Britain ')
    new1.add_file('female_poets_of_britain.txt')
    new1.classify(source1, source2)
    
    # Add code for three other new models below.
    new2 = TextModel('Male Poets of Britain ')
    new2.add_file('male_poets_of_britain.txt')
    new2.classify(source1, source2)
    
    new3 = TextModel('Female Poets of America ')
    new3.add_file('female_poets_of_america.txt')
    new3.classify(source1, source2)
    
    new4 = TextModel('Male Poets of America ')
    new4.add_file('male_poets_of_america.txt')
    new4.classify(source1, source2)
    
    print(source1.max_probability_common_words)
    print(source2.max_probability_common_words)
    print(new1.max_probability_common_words)
    print(new2.max_probability_common_words)
    print(new3.max_probability_common_words)
    print(new4.max_probability_common_words)


        