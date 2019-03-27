from character_util import *
from my_token import Token


class Lexer:
    def __init__(self, input):
        self.input = input
        self.position = 0
        self.line = 0
        self.column = 0

    def skip_whitespace_and_new_lines(self):
        while self.position < len(self.input) and self.input[self.position] in (' ', '\n'):
            if self.input[self.position] == '\n':
                self.line += 1
                self.column = 0
            else:
                self.column += 1
            self.position += 1

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
        if is_parenthesis(character):
            return self.recognize_parenthesis(character)
        if is_bracket(character):
            return self.recognize_bracket(character)
        if is_punctuation(character):
            return self.recognize_punctuation(character)
        if is_string(character):
            return self.recognize_string()

    def recognize_identifier(self):
        identifier = ''
        while self.position < len(self.input):
            character = self.input[self.position]
            if not (is_alpha_or_(character) or is_number(character)):
                break
            identifier += character
            self.position += 1
            self.column += 1
        if is_reserved_identifier(identifier):
            type_i = get_reserved_identifier_by_value(identifier)
            return Token(type_i, identifier, self.line, self.column)
        else:
            return Token(TokenTypes.identifier, identifier, self.line, self.column)

    def recognize_number(self):
        number = ''
        while self.position < len(self.input):
            character = self.input[self.position]
            if not (is_number(character)):
                break
            number += character
            self.position += 1
            self.column += 1
        return Token(TokenTypes.number, number, self.line, self.column)

    def recognize_string(self):
        r = re.match(r'".*"', self.input[self.position:])
        self.position += r.end()
        self.column += r.end()
        string = r.group()
        return Token(TokenTypes.string, string, self.line, self.column)

    def recognize_operator(self):
        character = self.input[self.position]
        if is_compare_operator(character):
            return self.recognize_compare_operator()
        if is_arithmetic_operator(character):
            return self.recognize_arithmetic_operator()

    def recognize_compare_operator(self):
        character = self.input[self.position]
        lookahead_index = self.position + 1
        if lookahead_index < len(self.input):
            lookahead = self.input[lookahead_index]
        else:
            lookahead = None
        is_lookahead_equal_symbol = lookahead == '='
        if is_lookahead_equal_symbol:
            self.position += 1
            self.column += 1

        self.position += 1
        self.column += 1
        if character == '>':
            if is_lookahead_equal_symbol:
                return Token(TokenTypes.rt_equal, '>=', self.line, self.column)
            else:
                return Token(TokenTypes.rt, '>', self.line, self.column)
        elif character == '<':
            if is_lookahead_equal_symbol:
                return Token(TokenTypes.lt_equal, '<=', self.line, self.column)
            else:
                return Token(TokenTypes.lt, '<', self.line, self.column)
        elif character == '=':
            if is_lookahead_equal_symbol:
                return Token(TokenTypes.equal, '==', self.line, self.column)
            else:
                return Token(TokenTypes.eq_oper, '=', self.line, self.column)
        elif character == '!':
            if is_lookahead_equal_symbol:
                return Token(TokenTypes.not_equal, '!=', self.line, self.column)
            else:
                return Token(TokenTypes.not_operator, '!', self.line, self.column)

    def recognize_arithmetic_operator(self):
        character = self.input[self.position]
        self.position += 1
        self.column += 1
        if character == '+':
            return Token(TokenTypes.plus, character, self.line, self.column)
        elif character == '-':
            return Token(TokenTypes.minus, character, self.line, self.column)
        elif character == '*':
            return Token(TokenTypes.times, character, self.line, self.column)
        elif character == '/':
            return Token(TokenTypes.div, character, self.line, self.column)
        elif character == '.':
            return Token(TokenTypes.dot, character, self.line, self.column)

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
