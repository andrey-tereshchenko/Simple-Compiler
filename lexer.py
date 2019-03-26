from token import TokenTypes, Token
from character_util import *


class Lexer:
    def __init__(self, input):
        self.input = input
        self.position = 0
        self.line = 0
        self.column = 0

    def skip_whitespace_and_new_lines(self):
        while self.position < len(self.input) and self.input[self.position] in (' ', '\n'):
            self.position += 1
            if self.input[self.position] == '\n':
                self.line += 1
                self.column = 0
            else:
                self.column += 1

    def all_tokens(self):
        tokens = list()
        current_token = self.next_token()
        while current_token.type != TokenTypes.eof:
            tokens.append(current_token)
            current_token = self.next_token()
        return tokens

    def next_token(self):
        if self.position >= len(self.input):
            return Token(TokenTypes.eof, '', self.line, self.column)

        self.skip_whitespace_and_new_lines()

        character = self.input[self.position]

        if is_alpha_or_(character):
            return self.recognize_identifier()
        if is_operator(character):
            return self.recognize_operator()
        if is_number(character):
            return self.recognize_number()
        if is_parenthesis():
            return self.recognize_parenthesis(character)
        if is_bracket(character):
            return self.recognize_bracket(character)
        if is_punctuation(character):
            return self.recognize_punctuation(character)

    def recognize_identifier(self):
        identifier = ''
        while self.position < len(self.input):
            character = self.input[self.position]
            if not (is_alpha_or_(character) or is_number(character)):
                break
            identifier += character
            self.position += 1
            self.column += 1
        return Token(TokenTypes.identifier, identifier, self.line, self.column)

    def recognize_number(self):
        print(1)

    def recognize_string(self):
        print(1)

    def recognize_operator(self):
        print(1)

    def recognize_parenthesis(self, char):
        self.position += 1
        self.column += 1
        if char == '(':
            return Token(TokenTypes.l_parent, char, self.line, self.column)
        else:
            return Token(TokenTypes.r_parent, char, self.line, self.column)

    def recognize_punctuation(self, char):
        self.position += 1
        self.column += 1
        if char == ';':
            return Token(TokenTypes.semi, char, self.line, self.column)
        else:
            return Token(TokenTypes.comma, char, self.line, self.column)

    def recognize_bracket(self, char):
        self.position += 1
        self.column += 1
        if char == '{':
            return Token(TokenTypes.l_brace, char, self.line, self.column)
        else:
            return Token(TokenTypes.r_brace, char, self.line, self.column)
