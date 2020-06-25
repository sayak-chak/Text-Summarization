import re

stopWords = {'',' ','\n','mr','mrs','a','to','the','s','t','ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than',',',';','|'} 

def findFreq(paragraph):
    freq = dict()
    paragraph = re.sub('\W+',' ', paragraph).split(" ")
    for word in paragraph:
        if word not in stopWords:
            if word not in freq.keys(): freq[word] = 0
            freq[word] += 1
    return freq

def findLineScore(line, freq):
    words = re.sub('\W+',' ', line).strip().split(" ")
    count = 0
    #print("asfs",words)
    for word in words:
        if word in freq.keys(): count += freq[word]
    return count

def summaryOfParagraph(paragraph, freq):
    seperateLinesParagraph = paragraph.split(".")
    lineScore = []
    for line in seperateLinesParagraph:
        lineScore.append((line, findLineScore(line, freq)))
    lineScore.sort(key = lambda var: var[1])
    #for some reason the first index has special characters, hacky fix
    return lineScore[1:]