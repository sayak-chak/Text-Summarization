from wordAnalyzer import *

def printOut(strArr):
    print(strArr)
    ans = ""
    for line in strArr: 
        if len(line) > 1:
            ans += (line[0][1].upper())+ line[0][2:]+". "
    return ans

def freq_based(input):
    # filepath = 'sample.txt'
    # file = open(filepath, 'r')
    paragraph = input.lower() #file.read().lower()

    freqOfWords = findFreq(paragraph)
    #print(freqOfWords)
    
    orderedImportanceOfLines = summaryOfParagraph(paragraph, freqOfWords)

    return printOut(orderedImportanceOfLines)
    

if __name__ == "__main__":
    print(freq_based(input()))