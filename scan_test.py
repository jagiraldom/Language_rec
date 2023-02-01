import os.path
from alphabets import alphabets
from scan_model import en_model, es_model # Trained models

from math import log

def scan_test(text_file:str, language="en")->str:

    """
    Reads 'text_file' in 'language' format, clears nonalphabetic symbols
    """

    with open(text_file, 'r', encoding='utf-8') as file:
        text = (file.readlines())
    all_words = "".join(text)
    all_words = all_words.lower()
    for code in alphabets[f"non_alphabetic_{language}"]:
        all_words = all_words.replace(chr(code), "")

    return all_words

def likelihood(string:str, probs:dict):
    result = 1.0
    for letter in string:
        result = result*probs[letter]

    return result

def log_likelihood(string:str, probs:dict):
    result = 0.0
    for letter in string:
        if probs[letter] != 0:
            result = result + log(probs[letter])
    return result

if __name__ == "__main__":
    t1 = scan_test(os.path.join("Test_data","en_test.txt"), "en")
    t2 = scan_test(os.path.join("Test_data","en_test.txt"), "es")
    print(log_likelihood(t1, en_model), likelihood(t1, en_model))
    print(log_likelihood(t1, es_model), likelihood(t1, es_model))
    print(log_likelihood(t2, es_model), likelihood(t2, es_model))
    print(log_likelihood(t2, en_model), likelihood(t2, en_model))