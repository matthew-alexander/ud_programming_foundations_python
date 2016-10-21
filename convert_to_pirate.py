# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 13:20:26 2016

@author: mda45
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 12:24:45 2016

@author: mda45
"""
import urllib 

def translate_text_to_pirate():
    pirate_version = []
    normal_text = open("luckycat.txt")
    contents_of_file = normal_text.read()
    # split into word list 
    word_list = contents_of_file.split()
    
    for word in word_list:
        # then run pirate tranlate
        new_word = translate_to_pirate(word)
        pirate_version.append(new_word)
    
    normal_text.close()
    print(" ".join(pirate_version)) 
    
    
    
    
    
def translate_to_pirate(text_to_check):
        connection = urllib.urlopen("http://isithackday.com/arrpi.php?text=" + text_to_check)
        translated_word = connection.read()
        connection.close()
        return translated_word
    
    
translate_text_to_pirate()
