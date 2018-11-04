"""
Bite 113. Filter words with non-ascii characters 

https://codechalleng.es/bites/113
"""
def extract_non_ascii_words(text):
    """Filter a text returning a list of non-ascii words"""
    non_ascii_lst = []
    words = text.split(" ")
    for word in words:
        for c in word:
            if ord(c) > 127:
                non_ascii_lst.append(word)
                break
    return non_ascii_lst
        
                
import pytest

@pytest.mark.parametrize("phrase, expected", [
    ('An preost wes on leoden, Laȝamon was ihoten', ['Laȝamon']),
    ('He wes Leovenaðes sone -- liðe him be Drihten', ['Leovenaðes', 'liðe']),
    ('He wonede at Ernleȝe at æðelen are chirechen', ['Ernleȝe', 'æðelen']),
    ('Uppen Sevarne staþe, sel þar him þuhte', ['staþe,', 'þar', 'þuhte']),
    ('Onfest Radestone, þer he bock radde', ['þer']),
    ('Fichier non trouvé', ['trouvé']),
    ('Over \u0e55\u0e57 57 flavours', ['๕๗']),
    ('Sí ... habrá que saber algo de Unicode, ¿no?', ['Sí', 'habrá', '¿no?']),
    ('This string only contains ascii words', []),
])
def test_extract_non_ascii_words(phrase, expected):
    assert extract_non_ascii_words(phrase) == expected
    
import sys
if __name__ == '__main__':
    pytest.main(sys.argv)          