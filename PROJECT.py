#Wisam Ali
#11/19/2018
"""
Sentiment Analysis - Python

We want to analyze the sentiment of the text on the sentence level. That is, we want to classify each sentence in this text as having either positive, neutral, or negative sentiment. The following three sentences illustrate each sentiment type. For example, 

I am so excited about my new car. (Positive sentiment)

I feel tired and moody today. (Negative sentiment)

There is parked car on the street. (Neutral sentiment)

If more words in a sentence carry the positive sentiment than negative, we will classify that sentence as having a positive sentiment. If the number of positive and
negative words in a sentence is equal, we will classify that sentence as neutral. Otherwise, the sentence is classified as having a negative sentiment. 


I'm going to be using and importing data from 3 files.

thehoundofthebaskervilles.txt
positivesentimentwords.txt
negativesentimentwords.txt'
"""

def main():
    file = open('thehoundofthebaskervilles.txt', 'r') # Opening the book txt file and reading it
        
    file1 = open('positivesentimentwords.txt', 'r') # Opening the positive words txt file and reading it 
        
    file2 = open('negativesentimentwords.txt', 'r') # Openin the negative words txt file and reading it
        
    A1 = [] # First array to store positive words 
    A2 = [] # Second array to store negative words
    for word in file1:
        A1.append(word.replace('\n', ''))
    for word in file2:
        A2.append(word.replace('\n', ''))
    poslines1 = 0
    negativelines2 = 0
    neutlines3 = 0
    for line in file:
        sentenceScore= 0 #if the outcome is positive, it's a positive sentence.
        splitLine = line.split(' ')

        for word in splitLine:
            if word.__contains__('.'):
                word = word.replace('.','') #Removing dots from the book and splitting the words.
            if word in A1:
                sentenceScore += 1
            elif word in A2:
                sentenceScore -= 1
            else:
                sentenceScore += 0
        if sentenceScore > 0:
            poslines1 += 1
        elif sentenceScore < 0:
            negativelines2 += 1
        else:
            neutlines3 +=1

    print("Positive:", poslines1)
    print("Negative:", negativelines2)
    print("Neutral:", neutlines3)

main()
