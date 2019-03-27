from lexer import *

with open('example.txt', 'r') as myfile:
    text = myfile.read()
lexer = Lexer(text)
tokens = lexer.all_tokens()

for token in tokens:
    print('type: {} ---- value: {} ---- line : {} ---- column: {}'.format(token.type, token.value, token.line, token.column))
