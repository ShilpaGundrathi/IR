from collections import Counter
from glob import iglob
import re
import os
import pandas as pd
import math
import urllib.request
import csv
from pprint import pprint
from urllib.request import urlopen
import json


def remove_garbage(text):
    """Replace non-word (non-alphanumeric) chars in text with spaces,
       then convert and return a lowercase version of the result.
    """
    text = re.sub(r'\W+', ' ', text)
    text = text.lower()
    return text
# data = pd.read_csv("https://raw.githubusercontent.com/BuzzFeedNews/2016-10-facebook-fact-check/master/data/facebook-fact-check.csv",index_col=0,parse_dates=[0])
# data.to_csv("data.csv")
url = "https://raw.githubusercontent.com/BuzzFeedNews/2016-10-facebook-fact-check/master/data/facebook-fact-check.csv"
url  = urllib.request.urlopen("https://raw.githubusercontent.com/BuzzFeedNews/2016-10-facebook-fact-check/master/data/facebook-fact-check.csv")
cr = csv.reader(url)


with urlopen(url) as u:
    content = u.read()
    obj = json.loads(content[3:])



pprint(url.read())
# topwords = 1000
folderpath = '/Users/shilpagundrathi/Desktop/IR/transcripts'
total_files = (len(os.listdir(folderpath)))
print("tot",total_files)
list_total_files = ((os.listdir(folderpath)))
counter = Counter()

def file_operations(path):
    for filepath in iglob(os.path.join(path, '*.txt')):
        with open(filepath,'r') as file:
            counter.update(remove_garbage(file.read()).split())

    # The number of word tokens in the database;
    sum_words = sum(counter.values())
    print("The number of word tokens in the database",sum_words)

    # The number of unique words in the database;
    unique_words = len(counter)
    print("The number of unique words in the database",unique_words)

    # The number of words that occur only once in the database;
    one_freq = Counter(el for el in counter.elements() if counter[el] == 1)
    print("The number of words that occur only once in the database",sum(one_freq.values()))

    # The average number of word tokens per document.
    avg = sum_words/total_files
    print("The average number of word tokens per document",avg)

    # for most common 30 values and tf
    list = []
    word_list = []
    for word, count in counter.most_common(30):
        mf = (word, count)
        list.append(mf)
        word_list.append(word)

# cal idf
    idf_list = []
    total_count = []
    new_count = []
    for file_words in (word_list):
        for filename in iglob(os.path.join(folderpath, '*.txt')):
            with open(filename) as f:
                filecount = ((f.read().count(file_words)))
                idf_list.append(filecount)
        mycount=(sum(x is not 0 for x in idf_list))
        print("countt",mycount)
        total_count.append(mycount)
        new_count.append((math.log(total_files/mycount)))
        idf_list.clear()
    df = pd.DataFrame(list ,columns=['frq_word', 'tf'])
    df1 = pd.DataFrame(new_count,word_list ,columns=['idf'])
    print(df1)
    new_df = df.assign(idf=df1.values)
    new_df["tfidf"] = new_df['tf']*new_df['idf']
    new_df['probability'] =( new_df['tf'] / sum_words)
    new_df.to_csv("tfidf.csv")
    return new_df


print(file_operations(folderpath))