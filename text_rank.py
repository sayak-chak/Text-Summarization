from copy import deepcopy
from word_score_matrix import *
from wordAnalyzer import stopWords

def get_sentence_list_after_reduction(original_input):
    # print(original_input)
    temp_list = []
    if '.' in original_input: temp_list = original_input.split(".")
    else: temp_list = original_input.split('।')
    final_list = []
    for sentence in temp_list:
        temp_line = ""
        line = sentence.split(" ")
        for word in line:
            if word not in stopWords: temp_line += word+" "
        final_list.append(temp_line)
    return final_list

def get_max_score_line(sentence_score_dict):
    # print(sentence_score_dict)
    index = -1
    max_score = -float('inf')
    for line_index in sentence_score_dict:
        if sentence_score_dict[line_index][1] > max_score:
            max_score = sentence_score_dict[line_index][1]
            index = line_index
    return index

def insert(ele,heap):
        if len(heap) == 0: 
            heap.append(ele)
            return 
        max_heapify(ele, heap)

def parentfind(index):
        return index//2

def bubbleUp(parent, child, heap):
        if heap[child][1] > heap[parent][1]:
            temp = deepcopy(heap[parent])
            heap[parent] = deepcopy(heap[child])
            heap[child] = deepcopy(temp)
            bubbleUp(parentfind(parent), parent, heap)

def max_heapify(ele,heap):
        heap.append(ele)
        index = len(heap) - 1
        bubbleUp(parentfind(index), index, heap)

def pop(heap):
    ret = heap.pop(0)
    return ret[2]

def best_first_search_from(index, sentence_score_dict, limit):
    path = []
    adj_heap = []
    covered = set()
    insert([sentence_score_dict[index][0], sentence_score_dict[index][1], index], adj_heap)
    path.append(index)
    while len(adj_heap) != 0 and len(path) < limit:
        current = pop(adj_heap)
        covered.add(current)
        for adj in sentence_score_dict[current][0]:
            if adj not in covered:
                covered.add(adj)
                insert([sentence_score_dict[adj][0],sentence_score_dict[adj][1], adj], adj_heap)
                path.append(adj)
                if len(path) >= limit: break
        if len(path) >= limit: break
    return path

def print_the_path(path, sentence_list):
    ans = ""
    for index in path:
        if index >=0 and index < len(sentence_list):
            temp = sentence_list[index].strip()
            if len(temp) > 1:
                temp = temp[0].upper()+temp[1:]
            ans += temp+". "
    return ans
# def text_rank_summarization(input):
#     threshold = 0.1
#     no_summary = -1
#     sentence_list = get_sentence_list_after_reduction(input)
#     cosine_matrix = get_cosine_matrix(sentence_list)
#     sentence_score_dict = get_sentence_score_dict(cosine_matrix, threshold)
#     max_score_sentence = get_max_score_line(sentence_score_dict)
#     # print(sentence_list)
#     # print(cosine_matrix)
#     # print(sentence_score_dict)
#     # print(max_score_sentence)
#     if max_score_sentence > no_summary:
#         path = best_first_search_from(max_score_sentence, sentence_score_dict)
#         return print_the_path(path, sentence_list)

if __name__ == "__main__":
    print(text_rank_summarization(input()))