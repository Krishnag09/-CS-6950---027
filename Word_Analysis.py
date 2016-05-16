from collections import Counter
import re
import csv

 
def openfile(filename):
    fh = open(filename, "r+")
    str = fh.read()
    fh.close()
    return str
 
def removegarbage(str):
    # Replace one or more non-word (non-alphanumeric) chars with a space
    str = re.sub(r'\W+', ' ', str)
    str = str.lower()
    return str
 
def getwordbins(words):
    cnt = Counter()
    for word in words:
        cnt[word] += 1
    return cnt
 
def main(filename, topwords):
    txt = openfile(filename)
    txt = removegarbage(txt)
    words = txt.split(' ')
    bins = getwordbins(words)
    for key, value in bins.most_common(topwords):
        with open('text_data1.csv','a') as csvfile:
             fieldnames= ['word','frequency']
             writer= csv.DictWriter(csvfile,fieldnames=fieldnames)
             writer.writerow({'word':key,'frequency': value})
        print key,value
 
main('founder_bio.txt', 100)
