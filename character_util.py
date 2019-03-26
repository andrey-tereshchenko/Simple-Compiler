from token import TokenTypes

arithmetic_operators = [TokenTypes.plus, TokenTypes.minus, TokenTypes.div, TokenTypes.times]

compare_operators = [TokenTypes.lt, TokenTypes.rt, TokenTypes.rt_equal, TokenTypes.lt_equal, TokenTypes.not_equal,
                     TokenTypes.eq_oper]
reserved_identifier = [TokenTypes.integer, TokenTypes.string, TokenTypes.if_i, TokenTypes.else_i, TokenTypes.while_i,
                       TokenTypes.return_i, TokenTypes.film, TokenTypes.genre, TokenTypes.actor, TokenTypes.user,
                       TokenTypes.for_i]
punctuation_chars = ';,'
operators = list()


def is_reserved_identifier(identifier):
    return identifier in reserved_identifier


def is_operator(char):
    return char in arithmetic_operators or char in compare_operators


def is_alpha_or_(char):
    return char.isalpha() or char == '_'


def is_number(char):
    return char.isdigit()


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
