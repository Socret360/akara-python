from akara import SpellChecker

checker = SpellChecker()
word = 'ស្គស'
assert len(checker.suggest(word)) == 3
