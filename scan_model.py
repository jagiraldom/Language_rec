import os.path # To handle paths
from alphabets import alphabets # Base alphabets

def scan_model(text_file:str, language="en")->dict:

    """
    Reads 'text_file' in 'language' format, clears nonalphabetic symbols and counts frequencies
    """
    
    with open(text_file, 'r', encoding='utf-8') as file:
        text = (file.readlines())
    all_words = "".join(text)
            
    hist = dict()

    if len(all_words) != 0:
        all_words = all_words.lower()
        for code in alphabets[f"non_alphabetic_{language}"]:
            all_words = all_words.replace(chr(code), "")

        for code in alphabets[f"{language}_alphabet"]:
            hist[chr(code)] = all_words.count(chr(code))/len(all_words)
    
    return hist

en_model = scan_model(os.path.join("Train_data","en_train.txt"), "en") # Trained frecuencies English
es_model = scan_model(os.path.join("Train_data","es_train.txt"), "es") # Trained frecuencias Spanish

if __name__ == "__main__":
    print("Collected probabilities for Spanish model",es_model, sep="\n\n", end="\n\n")
    print("Collected probabilities for English model",en_model, sep="\n\n", end="\n\n")
