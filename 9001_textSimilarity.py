"""
9. String Similarity Search

**Problem**: Find the most similar words from a dictionary for a given string.

**Similarity Metrics**:
- Edit distance (Levenshtein)
- Jaccard similarity
- N-gram matching
- Phonetic similarity

**Optimization**:
- Trie data structure
- BK-tree for metric spaces
- Locality-sensitive hashing

First, you must decide if you are interested in ortographic similarity or semantic similarity.

Ortographic similarity
In this case, you score the distance between two strings. There are various metrics for computing edit distance. 
Levenshtein distance is the most common: you can find various python implementations, like this.

"gold" is similar to "good", but not similar to "metal".

Semantic similarity
In this case, you measure how much two strings have a similar meaning.

fastText and other word embeddings fall into this case, even if they also take into account ortographic aspects.

"gold" is more similar to "metal" than to "good".

If you have a limited number of words in your list, you can use an existing word embedding, 
pretrained on your language. Based on this word embedding, you can compute the word vector for 
each word/sentence in your list, then compare the vector for your new word with the vectors 
from the list, using cosine similarity.
"""

import fasttext
import numpy as np

# download English pretrained model
fasttext.util.download_model('en', if_exists='ignore')
ft = fasttext.load_model('cc.en.300.bin')

def cos_sim(a, b):
    """Takes 2 vectors a, b and returns the cosine similarity according 
    to the definition of the dot product
    (https://masongallo.github.io/machine/learning,/python/2016/07/29/cosine-similarity.html)
    """
    dot_product = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    return dot_product / (norm_a * norm_b)

def compare_word(w, words_vectors):
    """
    Compares new word with those in the words vectors dictionary
    """
    vec=ft.get_sentence_vector(w)
    return {w1:cos_sim(vec,vec1) for w1,vec1 in words_vectors.items()}

# define your word list
words_list=[ "metal", "st. patrick", "health"]

# compute words vectors and save them into a dictionary.
# since there are multiwords expressions, we use get_sentence_vector method
# instead, you can use  get_word_vector method
words_vectors={w:ft.get_sentence_vector(w) for  w in words_list}

# try compare_word function!

compare_word('saint patrick', words_vectors)
# output: {'metal': 0.13774191, 'st. patrick': 0.78390956, 'health': 0.10316559}

compare_word('copper', words_vectors)
# output: {'metal': 0.6028242, 'st. patrick': 0.16589196, 'health': 0.10199054}

compare_word('ireland', words_vectors)
# output: {'metal': 0.092361264, 'st. patrick': 0.3721483, 'health': 0.118174866}

compare_word('disease', words_vectors)
# output: {'metal': 0.10678574, 'st. patrick': 0.07039305, 'health': 0.4192972}