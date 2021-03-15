import re
from tokens_types import persons, wishes, rooms, subject_process, act, subject_additional_option

class Lexer:
    def get_command(self, command):
        return command.split()

    def get_tokens(self, divided_command, tokens):
        for word in divided_command:
            if word in persons:
                tokens.append(['PERSON: ', word])
            elif word in wishes:
                tokens.append(['WISH: ', word])
            elif word in rooms:
                tokens.append(['ROOM TYPE: ', word])
            elif word in subject_process:
                tokens.append(['SUBJECT PROCESS: ', word])
            elif word in subject_additional_option:
                tokens.append(['SUBJECT ADDITIONAL OPTION: ', word])
            elif word in act:
                tokens.append(['ACT: ', word])
            elif word in '*-/+%=':
                tokens.append(['OPERATOR: ', word])
            elif re.match(".[0-9]", word):
                tokens.append(['VALUE: ', word])