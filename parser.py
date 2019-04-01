from collections import deque

from lexer import Lexer
from my_token import TokenTypes

with open('example.txt', 'r') as myfile:
    text = myfile.read()
lexer = Lexer(text)
tokens = lexer.all_tokens()


class Expression:
    def __init__(self, token, left=None, right=None):
        self.token = token
        self.left = left
        self.right = right

    def display(self):
        lines, _, _, _ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.token.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.token.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.token.value
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.token.value
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


def search_expressions(tokens):
    expressions = list()
    expression = list()
    start = False
    for token in tokens:
        if start and token.type == TokenTypes.semi:
            start = False
            expressions.append(expression)
            expression = list()
        if start:
            expression.append(token)
        if token.type == TokenTypes.eq_oper:
            start = True
    return expressions


def search_priority_operator_index(expression):
    priority_dev = 0
    operators = list()
    operator_max_p = -100000
    operator_max_p_index = 0
    i = 0
    for token in expression:
        if token.type == TokenTypes.l_parent:
            priority_dev -= 100
        if token.type == TokenTypes.r_parent:
            priority_dev += 100
        if token.type == TokenTypes.plus or token == TokenTypes.minus:
            value = 3 + priority_dev
            operators.append((token.type, i, value))
        if token.type == TokenTypes.times or token.type == TokenTypes.div:
            value = 2 + priority_dev
            operators.append((token.type, i, value))
        i += 1
    for op in operators:
        if op[2] >= operator_max_p:
            operator_max_p = op[2]
            operator_max_p_index = op[1]
    return operator_max_p_index


def delete_parent(expression):
    if expression[0].type == TokenTypes.l_parent and expression[-1].type == TokenTypes.r_parent:
        return expression[1:-1]


def is_equal_parent_num(expression):
    left = 0
    right = 0
    for token in expression:
        if token.type == TokenTypes.l_parent:
            left += 1
        if token.type == TokenTypes.r_parent:
            right += 1
    return left - right == 0


def parse_ariphmetic_expression(expression):
    index = search_priority_operator_index(expression)
    token = expression[index]
    left = expression[:index]
    right = expression[index + 1:]

    if not (is_equal_parent_num(left) and is_equal_parent_num(right)):
        expression = delete_parent(expression)
        left = expression[:index - 1]
        right = expression[index:]

    if len(left) != 1:
        left_exp = parse_ariphmetic_expression(left)
    else:
        left_exp = Expression(left[0])
    if len(right) != 1:
        right_exp = parse_ariphmetic_expression(right)
    else:
        right_exp = Expression(right[0])
    exp = Expression(token, left_exp, right_exp)
    return exp


expression = search_expressions(tokens)[0]
exp = parse_ariphmetic_expression(expression)
exp.display()
