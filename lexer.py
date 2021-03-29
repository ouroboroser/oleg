import re
from tokens_types import persons, wishes, rooms, subject_process, act, subject_additional_option

class Lexer:
    def get_command(self, command):
        return command.split()

    def get_tokens(self, divided_command, tokens):
        for word in divided_command:
            if word in persons:
                tokens.append({'person': word})
            elif word in wishes:
                tokens.append({'wish': word})
            elif word in rooms:
                tokens.append({'room type': word})
            elif word in subject_process:
                tokens.append({'subject process': word})
            elif word in subject_additional_option:
                tokens.append({'subject additional option': word})
            elif word in act:
                tokens.append({'action': word})
            elif word in '*-/+%=':
                tokens.append({'operator': word})
            elif re.match(".[0-9]", word):
                tokens.append({'value': word})