en_alphabet = list(range(97, 123))
es_alphabet = en_alphabet.copy()
es_alphabet.append(241)

all_ascii = list(range(256))
non_alphabetic_en = [simbol for simbol in all_ascii if simbol not in en_alphabet] 
non_alphabetic_es = [simbol for simbol in all_ascii if simbol not in es_alphabet]

alphabets = {
    "en_alphabet": en_alphabet,
    "es_alphabet": es_alphabet,
    "non_alphabetic_en": non_alphabetic_en,
    "non_alphabetic_es": non_alphabetic_es
}