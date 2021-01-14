
# -*- coding: utf-8 -*-
import math
import colors
from collections import defaultdict, Counter
import nltk
from nltk import sent_tokenize, word_tokenize, stem
from nltk.corpus import stopwords
from datetime import datetime
import numpy as np
import re
import networkx as nx
import sys
import os

"""
this is the implmentation of LexRank algorithm
http://arxiv.org/pdf/1109.2128.pdf
"""
stop_words = stopwords.words('english')

def idf_dict(sentence_sets):
     idf_dict = defaultdict(lambda:0.0)
     N = len(sentence_sets)
     all_words = []
     for sentence in sentence_sets:
          sent = list(set(sentence.split()))
          for word in sent:
               idf_dict[word] += 1
               all_words.append(word)

     all_words = list(set(all_words))
     for word in all_words:
          idf = (N/idf_dict[word])
          idf_dict[word] = math.log(idf, 10)

     return idf_dict


def idf_cosine_calc(sent_x, sent_y, idf_dict):
     x_dict, y_dict = defaultdict(lambda:0), defaultdict(lambda:0)
     # Create dict of tf each sentence
     for x_word in sent_x.split():
          x_dict[x_word] += 1
     for y_word in sent_y.split():
          y_dict[y_word] += 1
     both = sent_x.split()
     both.extend(sent_y.split())
     both = list(set(both))
     # calc numerator part of idf_cosine
     numerator = sum([((x_dict[word])*(y_dict[word])*(idf_dict[word]**2)) for word in both])
     x_denomerator = sum([(x_dict[word]*(idf_dict[word]))**2 for word in list(set(sent_x.strip().split()))])
     y_denomerator = sum([(y_dict[word]*(idf_dict[word]))**2 for word in list(set(sent_y.strip().split()))])

     if numerator == 0 or math.sqrt(x_denomerator) == 0 or math.sqrt(y_denomerator) == 0:
          return 0
     else:
          return round(numerator/(math.sqrt(x_denomerator)*math.sqrt(y_denomerator)),4)


def idfmodified_cosine_matrix(sentences, idf_dict):
    #Create Matrix
    cos_matrix = np.zeros([len(sentences),len(sentences)])
    row_num = [x for x in range(len(sentences))]
    col_num = [x for x in range(len(sentences))]
    N = len(sentences)
    for i in row_num:
        for j in col_num:
            cos_matrix[i][j] = idf_cosine_calc(sentences[i],sentences[j], idf_dict)
    return cos_matrix


def lexrank_graph(similarity_matrix, cos_th, alpha):
    rows_over_thr, cols_over_thr = np.where(similarity_matrix >= cos_th)
    graph_matrix = np.zeros(similarity_matrix.shape)
    #make degree vector 
    degree_matrix = np.zeros(similarity_matrix.shape[1])

    for i, j in zip(rows_over_thr, cols_over_thr):
        if i == j:
            continue
        else:
            graph_matrix[i][j] = 1
            degree_matrix[i]+= 1
    #CosineMatrix[i][j]/Degree[i]
    for i, j in zip(rows_over_thr, cols_over_thr):
        if i == j:
            continue
        else:
            similarity_matrix[i][j] = similarity_matrix[i][j]/degree_matrix[i]
    # using networkx
    graph = nx.Graph()
    for i, j in zip(rows_over_thr, cols_over_thr):
        if i == j:
            continue
        else:
            graph.add_edge(i, j , weight= similarity_matrix[i][j])
    lexrank = nx.pagerank(graph, alpha=0.9,  max_iter=5000)
    return lexrank


def lexrank(sentences, word_thr=100, sent_split=False, word_split=False, stemming=False, cos_th=0.05, alpha=0.9):
    # sentence_tokenize
    if sent_split:
        sentences = sent_tokenize(sentences)
    # retain original
    original_sentences = sentences
    #print("This is the original document")
    #print()
    #print(original_sentences)
    print()
    with colors.pretty_output(colors.BOLD, colors.FG_YELLOW) as out:
        out.write("THIS IS THE SUMMARY OF THE DETAILED TEXT GIVEN ABOVE")
        #out.write(stop_words)
    print()
    #print(stop_words)
    # word_tokenize
    if word_split:
        sentences = [" ".join(word_tokenize(sent)) for sent in sentences]
    # stemming
    if stemming:
        stemmer = stem.PorterStemmer()
        sentences = [stemmer.stem(sent) for sent in sentences]
    # make all words lowercase for calc tf-idf & lexrank
    sentences_lower = [sent.lower() for sent in sentences]
    # construct idf dictionary
    idf_set           = idf_dict(sentences_lower)
    similarity_matrix = idfmodified_cosine_matrix(sentences_lower, idf_set)
    lexrank           = lexrank_graph(similarity_matrix, cos_th, alpha)
    lexrank_sentences = []
    word_counter = 0
    for num, score in sorted(lexrank.items(), key=lambda x:x[1], reverse=True):
        length = len(original_sentences[num].strip().split())
        if word_counter+length <= word_thr:
            word_counter += length
            lexrank_sentences.append(original_sentences[num])
        else:
            # avoid to extract nothing if 1st sentence of lexrank score is longer than word_thr
            if word_counter == 0:
                continue
            else:
                break
    return " ".join(lexrank_sentences)


def test():
    # example sentence from LexRank paper
    
    tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
    with colors.pretty_output(colors.BOLD, colors.FG_RED) as out:
        print()
        out.write("THE AVAILABLE OPTIONS ARE ")
        print()
        out.write("VOTING  GULFWAR  PARLIAMENT  WORLD BANK")
        print()
    with colors.pretty_output(colors.BOLD, colors.FG_GREEN) as out:
        out.write("PRESS 1 FOR VOTING INFO")
        print()
        out.write("PRESS 2 FOR GULFWAR INFO")
        print()
        out.write("PRESS 3 FOR PARLIAMENT INFO")
        print()
        out.write("PRESS 4 FOR WORLD-BANK INFO")
        print()
        out.write("PRESS 5 FOR ANY OTHER INFORMATION")
        print()
        out.write("PRESS 6 FOR EXIT")
        print()
    domain = input("CHOOSE AN OPTION  ")
    print()
    if domain == "1":
        fp = open("voting.txt")
    if domain == "2":
        fp = open("gulfwar.txt")
    if domain == "3":
        fp = open("parliament.txt")
    if domain == "4":
        fp = open("Worldbank.txt")
    if domain == "5":
        fp=open("otherdomain.txt")
    if domain == "6":
        sys.exit()
    #fp=open(filename)
    data=fp.read()
    #sents=list(data)
    #print(sents)
    #print(type(data))
    print(list(tokenizer.tokenize(data)))
    #print('\n----\n'.join(tokenizer.tokenize(data)))
    print("Lexrank:\n{}".format(lexrank(tokenizer.tokenize(data), word_thr=100, word_split=True)))
    print("\n")
    print("The stop words used are",end="\n")
    print(stop_words,end="\n")
    print("\n")
    f = open("demofile2.txt", "a")
    fp = open("demofile2.pdf", "a")
    #fd = open('debug.txt',"a")
    f.write("Lexrank:\n{}".format(lexrank(tokenizer.tokenize(data), word_thr=100, word_split=True)))
    #os.system('python scriptone.py')
    #os.system('cupsfilter demofile2.txt > demofile2.pdf')
    #os.system('open demofile2.pdf')
    f.close()
    fp.close()
    os.system('python scriptone.py')
    #os.system('rm demofile2.txt')
    #os.system('rm demofile2.pdf')
    #fd.close()


if __name__ == '__main__':
    test()
