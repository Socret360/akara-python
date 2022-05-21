from akara import SpellChecker

checker = SpellChecker()

word = 'ស្គស'
assert checker.is_correct(word) == False
assert len(checker.suggest(word)) == 3
