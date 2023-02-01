import os

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
    file_list = os.listdir("Test_data")
    results = {"Correct":0, "Incorrect":0, "Total":len(file_list)}
    for file in file_list:
        file_path = os.path.join("Test_data", file)
        data = scan_test(file_path)
        test = log_likelihood(data, en_model), log_likelihood(data, es_model)
        guess = "es" if test[0]<test[1] else "en"
        if guess == file[:2]:
            results["Correct"] += 1
        else:
            results["Incorrect"] += 1
        print(file, guess, sep="---->",end="\n")
    print(results)
