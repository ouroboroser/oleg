from semanticAnalyzer.token_relations import rooms_relations, subject_relations

class semanticAnalyzer:
    def room_to_object(self, tokens):

        room_token = 'room type'
        for token in tokens:
            if room_token in token:
                room_result = token[room_token]

        subject_process_token = 'subject process'
        for token in tokens:
            if subject_process_token in token:
                subject_process_result = token[subject_process_token]


        #print('res1: ', room_result)
        #print('res2: ', subject_process_result)

        res = {}

        for r in rooms_relations:
            if subject_process_result in r.values() and room_result in r.keys():
                res = r

        if not res:
            res = 'semantic error: {subject_process} does not exist in the {room}'.format(subject_process = subject_process_result, room = room_result)
            #print(res)

        return res


    def option_to_subject(self, tokens):
        subject_process_token = 'subject process'
        for token in tokens:
            if subject_process_token in token:
                subject_process_result = token[subject_process_token]

        subject_additional_option_token = 'subject additional option'
        subject_additional_option_result = None

        for token in tokens:
            if subject_additional_option_token in token:
                subject_additional_option_result = token[subject_additional_option_token]
                #print('RESULT: ', subject_additional_option_result)

        #print('subject process result:', subject_process_result)
        #print('subject additional option result:', subject_additional_option_result)

        res = {}

        if subject_additional_option_result == None:
            res = 'you have not specified what exactly you want'
        else:
            for r in subject_relations:
                if subject_process_result in r.keys() and subject_additional_option_result in r.values():
                    res = r

        #if not res:
        #    print('semantic error: {subject_process} does not exist in the {room}'.format(subject_process = subject_process_result, room = room_result))

        #print(res)
        return res