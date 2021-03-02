from lexer import Lexer

lexer = Lexer()
tokens = []

print('enter your command: ')

input_command = input()
divided_command = lexer.get_command(input_command.lower())
lexer.find_room(divided_command, tokens)

tokens_types = []

if len(tokens) == 0:
    print('wrong command')
else:
    print('result:', tokens)