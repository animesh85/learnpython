## LSU - IE7428 Semantic Analysis
## Ricardo A. Calix
## Multimedia Semantic Analysis Lab
## Python interface to Stanford parser

import re
import pprint
import os
import shutil
import commands
import random
import time
import sys
import copy
import datetime
import glob
import math
import subprocess
import sets
from subprocess import call, Popen, PIPE, STDOUT
import nltk

############################################################################################################

def run_cmd(cmd):
    arglist = cmd.split()
    p = Popen(arglist, stdout=PIPE, stderr=STDOUT)
    output = p.communicate()[0]
    return (p.returncode, output)


############################################################################################################

def mycommandsfunction():
 
    path = 'C:\\Users\\Ricardo\\Desktop\\javascripts\\parser\\'
    os.chdir(path)
    
    stanfordcommandPOS = 'java -cp stanford-parser.jar -mx1024m edu.stanford.nlp.parser.lexparser.LexicalizedParser -outputFormat "wordsAndTags" englishPCFG.ser.gz "C:\Users\Ricardo\Desktop\javascripts\data\sentences.txt" > "C:\Users\Ricardo\Desktop\javascripts\data\sentences.POS.parsed.txt"'
    stanfordcommandPENN = 'java -cp stanford-parser.jar -mx1024m edu.stanford.nlp.parser.lexparser.LexicalizedParser -outputFormat "penn" englishPCFG.ser.gz "C:\Users\Ricardo\Desktop\javascripts\data\sentences.txt" > "C:\Users\Ricardo\Desktop\javascripts\data\sentences.PENN.parsed.txt"'
    stanfordcommandDEPEN = 'java -cp stanford-parser.jar -mx1024m edu.stanford.nlp.parser.lexparser.LexicalizedParser -outputFormat "typedDependencies" englishPCFG.ser.gz "C:\Users\Ricardo\Desktop\javascripts\data\sentences.txt" > "C:\Users\Ricardo\Desktop\javascripts\data\sentences.DEPEN.parsed.txt"'
    os.system(stanfordcommandPOS)
    os.system(stanfordcommandPENN)
    os.system(stanfordcommandDEPEN)


##########################################################################################################

def GetSyntacticParseStanfordParser(sentence):
    g_add_sentence = 'C:\\Users\\Ricardo\\Desktop\\javascripts\\data\\sentences.txt'
    f_add_sentence = open(g_add_sentence,'w')
    f_add_sentence.write(sentence)
    f_add_sentence.write('\n')
    f_add_sentence.close()

    path = 'C:\\Users\\Ricardo\\Desktop\\javascripts\\parser\\'
    os.chdir(path)
    
    stanfordcommandPENN = 'java -cp stanford-parser.jar -mx1024m edu.stanford.nlp.parser.lexparser.LexicalizedParser -outputFormat "penn" englishPCFG.ser.gz "C:\Users\Ricardo\Desktop\javascripts\data\sentences.txt" > "C:\Users\Ricardo\Desktop\javascripts\data\sentences.PENN.parsed.txt"'
    os.system(stanfordcommandPENN)
  

    g_stanford_parse_PENN = 'C:\\Users\\Ricardo\\Desktop\\javascripts\\data\\sentences.PENN.parsed.txt'
    f_stanford_parse_PENN = open(g_stanford_parse_PENN,'r')

    s_penn = ''
    for line in f_stanford_parse_PENN.readlines():
        s_penn = s_penn + line

    f_stanford_parse_PENN.close()

    temp = re.sub('\n','',s_penn)
    temp = re.sub('\t','',temp)

    return temp

##########################################################################################################

def GetDependencyParseStanfordParser(sentence):
    g_add_sentence = 'C:\\Users\\Ricardo\\Desktop\\javascripts\\data\\sentences.txt'
    f_add_sentence = open(g_add_sentence,'w')
    f_add_sentence.write(sentence)
    f_add_sentence.write('\n')
    f_add_sentence.close()

    path = 'C:\\Users\\Ricardo\\Desktop\\javascripts\\parser\\'
    os.chdir(path)
    
    stanfordcommandDEPEN = 'java -cp stanford-parser.jar -mx1024m edu.stanford.nlp.parser.lexparser.LexicalizedParser -outputFormat "typedDependencies" englishPCFG.ser.gz "C:\Users\Ricardo\Desktop\javascripts\data\sentences.txt" > "C:\Users\Ricardo\Desktop\javascripts\data\sentences.DEPEN.parsed.txt"'
    os.system(stanfordcommandDEPEN)
  
    g_stanford_parse_DEPEN = 'C:\\Users\\Ricardo\\Desktop\\javascripts\\data\\sentences.DEPEN.parsed.txt'
    f_stanford_parse_DEPEN = open(g_stanford_parse_DEPEN,'r')

    s_penn_DEPEN = []
    for line in f_stanford_parse_DEPEN.readlines():
        temp3 = re.sub('\n','',line)
        s_penn_DEPEN.append(temp3)

    f_stanford_parse_DEPEN.close()

    #temp = re.sub('\n','',s_penn)
    #temp = re.sub('\t','',temp)

    return s_penn_DEPEN

###########################################################################################################



## Main()

sent = 'Today Joe went to visit Dr. Gerald M. Knapp at the hospital, where his sister, was very sick not two months ago.'
the_parse = GetSyntacticParseStanfordParser(sent)
my_dependencies_list = GetDependencyParseStanfordParser(sent)

#print the_parse

############################################################################


def traverse(t):
 
    try:
        #t.label()
        t.node
        #print t.node
        #print t.label()
    except AttributeError:
        df =0
    else:
        #print t
        if t.height() == 2:   #change 2 or 3
            #print t
            #print t.node
            #print t.parent()
            ii=8
        if t.node == 'VBD' and t.height() == 2:
            print t
            print t.node
        if t.node == 'NP' and t.height() == 3:
            print t
            print t.node
            

        for child in t:
            traverse(child)


############################################################################


treeRC = nltk.Tree(the_parse)

traverse(treeRC)

############################################################################


#print treeRC
#print myleaves
treeRC.draw()
############################################################################

print ''
print my_dependencies_list
    
print '<<<<<<<<<<<<DONE>>>>>>>>>>>>'


####END
############################################################################################################

