from syntacticalAnalyzer.node import Node, treeToString
from tokens_types import persons, wishes, preposition, act,subject_process, subject_additional_option, articles, rooms
from syntacticalAnalyzer.analyzer_helper import add, locations

result = []

class syntacticalAnalyzer:
    def get_sentence(self, sentence):
        diveded = sentence.split()
        return  diveded

    def createSentenceTree(self, words):
        root = Node('sentence')

        for word in words:
            type = 'persons'
            if word in persons:
                root.left = Node(word)
                add(result, type, word, locations['persons'])
                break
            else:
                error = 'syntax error. missing noun'
                root.left = Node(error)
                break

        for word in words:
            type = 'wishes'
            if word in wishes:
                root.right = Node(word)
                add(result, type, word, locations['wishes'])
                break
            else:
                error = 'syntax error. missing verb'
                root.right = Node(error)

        preposition_helper = False

        for word in words:
            changed = True
            if word in preposition:
                if preposition_helper == False:
                    root.right.left = Node(word)
                    words.remove(word)
                    preposition_helper = changed
                else:
                    root.right.right = Node(word)
                    words.remove(word)

        for word in words:
            type = 'act'
            if word in act:
                root.right.left.left = Node(word)
                add(result, type, word, locations['act'])
                words.remove(word)

        for word in words:
            if word in act:
                root.right.left.left.left = Node(word)
                break
            else:
                error = 'maybe you have forgotten proposition or made a mistake'
                root.right.left.left.left = Node(error)

        for word in words:
            type = 'execution object'
            if word in subject_process:
                root.right.left.left.left.left = Node(word)
                add(result, type, word, locations['execution object'])
                break
            else:
                error = 'syntax error. execution object'
                root.right.left.left.left.left = Node(error)


        for word in words:
            type = 'execution object optional'
            if word in subject_additional_option:
                root.right.left.left.left.left.left = Node(word)
                add(result, type, word, locations['execution object optional'])

        for word in words:
            type = 'articles'
            if word in articles:
                root.right.right.left = Node(word)
                add(result, type, word, locations['articles'])
                break
            else:
                error = 'syntax error. missing article'
                root.right.right.left = Node(error)

        for word in words:
            type = 'rooms'
            if word in rooms:
                root.right.right.left.left = Node(word)
                add(result, type, word, locations['rooms'])
            else:
                error = 'syntax error. missing room type'
                root.right.right.left.left = Node(error)

        string = []
        treeToString(root, string)
        print(''.join(string))

        syntax_error = False

        string = ' '.join(string)
        string = string.translate({ord(i): None for i in '()'})
        string = string.split()

        for item in string:
            if item == 'syntax':
                syntax_error = True

        return syntax_error