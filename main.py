from lexer import Lexer
from syntacticalAnalyzer.analyzer import syntacticalAnalyzer
from semanticAnalyzer.analyzer import semanticAnalyzer

lexer = Lexer()
tokens = []

print('enter your command: ')

#input_command = input()
#input_command = 'i want to turn on tv latte in the bedroom'
input_command = 'i want to turn on coffee-machine tea in the kitchen'
#input_command = 'i want to turn in plate degree = 200 in the kitchen'
print(input_command)
divided_command = lexer.get_command(input_command.lower())
lexer.get_tokens(divided_command, tokens)

tokens_types = []

if len(tokens) == 0:
    print('wrong command')
else:
    synAnalyzer = syntacticalAnalyzer()
    words = synAnalyzer.get_sentence(input_command)
    syntax_error = synAnalyzer.createSentenceTree(words)

    if syntax_error == True:
        print('you have a syntax error, please recheck your commnad')
    else:
        semAnalyzer = semanticAnalyzer()
        result = semAnalyzer.room_to_object(tokens)
        if type(result) == dict:
            final = semAnalyzer.option_to_subject(tokens)
            print(final)
        else:
            print(result)
