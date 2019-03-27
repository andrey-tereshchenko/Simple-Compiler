import re

from my_token import TokenTypes

arithmetic_operators = [TokenTypes.plus.value, TokenTypes.minus.value, TokenTypes.div.value, TokenTypes.times.value,
                        TokenTypes.dot.value]

compare_operators = [TokenTypes.lt.value, TokenTypes.rt.value, TokenTypes.rt_equal.value, TokenTypes.lt_equal.value,
                     TokenTypes.not_equal.value,
                     TokenTypes.eq_oper.value]
logic_operator = [TokenTypes.and_operator.value, TokenTypes.not_operator.value, TokenTypes.or_operator.value]
reserved_identifier = [TokenTypes.integer, TokenTypes.string, TokenTypes.if_i,
                       TokenTypes.else_i, TokenTypes.while_i,
                       TokenTypes.return_i, TokenTypes.film, TokenTypes.genre, TokenTypes.actor,
                       TokenTypes.user, TokenTypes.for_i]
punctuation_chars = ';,'
operators = list()


def is_compare_operator(char):
    return char in compare_operators


def is_arithmetic_operator(char):
    return char in arithmetic_operators


def is_reserved_identifier(identifier):
    return identifier in [i.value for i in reserved_identifier]


def get_reserved_identifier_by_value(value):
    for idn in reserved_identifier:
        if idn.value == value:
            return idn


def is_operator(char):
    return char in arithmetic_operators or char in compare_operators


def is_alpha_or_(char):
    return char.isalpha() or char == '_'


def is_number(char):
    return char.isdigit()


def is_string(character):
    return character == '"'


def is_arithmetic_operator(char):
    return char in arithmetic_operators


def is_parenthesis(char):
    return char == '(' or char == ')'


def is_whitespace_or_newline(char):
    return char == ' ' or char == '\n'


def is_bracket(char):
    return char == '{' or char == '}'


def is_punctuation(char):
    return char in punctuation_chars
