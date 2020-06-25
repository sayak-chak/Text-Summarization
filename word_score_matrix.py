from cosine_similarity import find

def get_cosine_matrix(seperate_lines_in_paragraph):
    # seperate_lines_in_paragraph = paragraph.split(".")
    no_of_sentences = len(seperate_lines_in_paragraph)
    matrix = []
    for _ in range(no_of_sentences):
        temp = [0]*no_of_sentences
        matrix.append(temp)
    
    for index1 in range(no_of_sentences):
        for index2 in range(index1+1, no_of_sentences):
            matrix[index1][index2] = matrix[index2][index1] = find(seperate_lines_in_paragraph[index1], seperate_lines_in_paragraph[index2])

    return matrix

def get_sentence_score_dict(cosine_matrix, threshold):
    if len(cosine_matrix) > 0:
        no_of_sentences = len(cosine_matrix)
        score_dict = {} #line - score
        for index1 in range(no_of_sentences):
            for index2 in range(no_of_sentences):
                if index1!=index2 and cosine_matrix[index1][index2] > threshold: #omit repetations
                    if index1 not in score_dict: score_dict[index1] = [set(), 0]
                    if index2 not in score_dict: score_dict[index2] = [set(), 0] #adjacent nodes, score
                    score_dict[index1][0].add(index2)
                    score_dict[index2][0].add(index1)
                    score_dict[index1][1] += cosine_matrix[index1][index2]
                    score_dict[index2][1] += cosine_matrix[index1][index2]
        return score_dict
    return {}
    
# input = input().split(".")
# threshold = 0.2
# cosine_matrix = get_cosine_matrix(input)
# print(get_sentence_score_dict(cosine_matrix, threshold))