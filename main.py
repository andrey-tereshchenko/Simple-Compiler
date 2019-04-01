from lexer import *

with open('example.txt', 'r') as myfile:
    text = myfile.read()
lexer = Lexer(text)
tokens = lexer.all_tokens()

print("\nLexer analyze:\n")
for token in tokens:
    print('type: {:30}  value: {:20}  line : {}     column: {}'.format(token.type, token.value, token.line, token.column))
