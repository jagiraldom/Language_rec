from alphabets import alphabets

def scan_model(text_file:str, language="en")->dict:

    with open(text_file, 'r', encoding='utf-8') as file:
        text = (file.readlines())
    all_words = "".join(text)
            
    hist = dict()

    if len(all_words) != 0:
        for code in alphabets[f"non_alphabetic_{language}"]:
            all_words = all_words.replace(chr(code), "")
        all_words = all_words.lower()

        for code in alphabets[f"{language}_alphabet"]:
            hist[chr(code)] = all_words.count(chr(code))/len(all_words)
    
    return hist

en_model = scan_model("en_text.txt", "en")
es_model = scan_model("es_text.txt", "es")

print(es_model, en_model, sep="\n\n") # agregar formato para imprimir
if __name__ == "__main__":
    pass
    #print(scan_model("sample.txt"))
    #print(scan_model("sample.txt", "es"))
