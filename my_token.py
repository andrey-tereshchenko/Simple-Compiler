from enum import Enum


class TokenTypes(Enum):
    identifier = 'identifier'
    number = 'number'
    eof = 'eof'
    plus = '+'
    minus = '-'
    times = '*'
    div = '/'
    and_operator = 'and'
    or_operator = 'or'
    not_operator = '!'
    equal = '=='
    eq_oper = '='
    not_equal = '!='
    lt = '<'
    rt = '>'
    lt_equal = '<='
    rt_equal = '>='
    dot = '.'
    integer = 'integer'
    string = 'string'
    boolean = 'boolean'
    user = 'user'
    film = 'film'
    actor = 'actor'
    genre = 'genre'
    if_i = 'if'
    else_i = 'else'
    while_i = 'while'
    for_i = 'for'
    return_i = 'return'
    l_parent = '('
    r_parent = ')'
    comma = ','
    semi = ';'
    l_brace = '{'
    r_brace = '}'


class Token:

    def __init__(self, type, value, line, column):
        self.type = type
        self.value = value
        self.line = line
        self.column = column


