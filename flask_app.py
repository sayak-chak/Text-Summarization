from flask import Flask, render_template, request
from wordAnalyzer import *
from text_rank import *

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/summary',methods = ['POST'])
def freq_based():
   choice = request.form['options']
   input = request.form['input']
   if str(choice) == "freq-based": 
       return freq_based(input)
   elif str(choice) == "text-rank": 
       return text_rank_summarization(input)

def text_rank_summarization(input):
    threshold = 0.1
    no_summary = -1
    factor = 0.5
    sentence_list = get_sentence_list_after_reduction(input)
    cosine_matrix = get_cosine_matrix(sentence_list)
    sentence_score_dict = get_sentence_score_dict(cosine_matrix, threshold)
    max_score_sentence = get_max_score_line(sentence_score_dict)
    if max_score_sentence > no_summary:
        limit = int(len(sentence_list)*factor)
        path = best_first_search_from(max_score_sentence, sentence_score_dict, limit)
        return print_the_path(path, sentence_list)

def printOut(strArr):
    ans = ""
    for line in strArr: 
        temp = (line[0]+". ").strip()
        if len(temp) > 1:
            temp = temp[0].upper() + temp[1:]
        ans += temp+" "
    return ans

def freq_based(input):
    # filepath = 'sample.txt'
    # file = open(filepath, 'r')
    paragraph = input.lower() #file.read().lower()

    freqOfWords = findFreq(paragraph)
    #print(freqOfWords)
    
    orderedImportanceOfLines = summaryOfParagraph(paragraph, freqOfWords)

    return printOut(orderedImportanceOfLines)