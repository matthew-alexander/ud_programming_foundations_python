# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 12:24:45 2016

@author: mda45
"""
import urllib 

def read_text():
    quotes = open("movie_quotes.txt")
    contents_of_file = quotes.read()
    #print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)
    
    
    
def check_profanity(text_to_check):
        connection = urllib.urlopen(" http://www.wdylike.appspot.com/?q=" + text_to_check)
        output = connection.read()
        if output == "true":
            print("PROFANITY DETECTED!")
        elif output == "false":
            print("This document looks ok")
        else:
            print("Document not properly scanned...")    
        
        connection.close()
    
    
read_text()
