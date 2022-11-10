import numpy as np

#get Levenshtein Distance 
def distance(word, c):
    dp = np.zeros((len(word)+1, len(c)+1))
    for i in range(1, len(word) + 1):
        dp[i][0] = dp[i-1][0] + 1
    for j in range(1, len(c) + 1):
        dp[0][j] = dp[0][j-1] + 1
    for i in range(1, len(word)+1):
        for j in range(1, len(c)+1):
            var1 = dp[i][j-1] + 1
            var2 = dp[i-1][j] + 1
            if (word[i-1] == c[j-1]):
                var3 = dp[i-1][j-1]
            else:
                var3 = dp[i-1][j-1] + 1
            dp[i][j] = min(var1, var2, var3)  
    return dp[len(word)][len(c)]

# collect candidates with distance 1,2, or 3 to the word
def find_candidates(word): 
    candidates1 = {} 
    candidates2 = {}
    candidates3 = {}
    for c in word_prob_dict.keys():
        if (len(c) <= len(word) + 3 and len(c) >= len(word) - 3):
            dist = distance(word, c)
            if (dist == 1):
                candidates1[c] = word_prob_dict[c]
            if (dist == 2):
                candidates2[c] = word_prob_dict[c]
            if (dist == 3):
                candidates3[c] = word_prob_dict[c]
    return (candidates1, candidates2, candidates3)

#word correcter
def word_correction(word):
    if word not in dictionary:
        candidates1, candidates2, candidates3 = find_candidates(word)
        if candidates1:
            return max(candidates1, key=candidates1.get)
        if candidates2:
            return max(candidates2, key=candidates2.get)
        if candidates3:
            return max(candidates3, key=candidates3.get)
        else:
            return word
    else:
        return word

if __name__ == "__main__":
    dictionary = {}
    with open("count_1w.txt") as file:
        for line in file:
            (key, value) = line.split()
            dictionary[key] = int(value)

    total_words = sum(dictionary.values())
    word_prob_dict = {}
    for key, value in dictionary.items():
        word_prob_dict[key] = value/total_words
    word = input("Enter the word you wanna test: ")
    correct = word_correction(word)
    print("The corrected word is: ", correct)