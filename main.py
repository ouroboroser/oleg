from lexer import Lexer
from syntacticalAnalyzer.analyzer import syntacticalAnalyzer

lexer = Lexer()
tokens = []

print('enter your command: ')

#input_command = input()
input_command = 'i want to turn on tv show in the bedro9om'
divided_command = lexer.get_command(input_command.lower())
lexer.get_tokens(divided_command, tokens)

tokens_types = []

if len(tokens) == 0:
    print('wrong command')
else:
    print('OK')
    synAnalyzer = syntacticalAnalyzer()
    words = synAnalyzer.get_sentence(input_command)
    synAnalyzer.createSentenceTree(words)