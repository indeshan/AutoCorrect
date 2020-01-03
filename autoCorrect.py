#pip install pyspellchecker #Required package
from spellchecker import SpellChecker
 
spell = SpellChecker(language=None, case_sensitive=True)
a=spell.word_frequency.load_words(['Hello', 'HELLO', 'I','AM', 'Shan', 'Inde'])
 
# find those words that may be misspelled
misspelled = spell.unknown(['hllo', 'Shhan', 'Index'])
 
for word in misspelled:
    # Get the one `most likely` answer
    print(spell.correction(word))
 
    # Get a list of `likely` options
    print(spell.candidates(word))
