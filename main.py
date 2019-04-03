from lexer import *


def main():
    filename = 'test/test_whileloop.pas'
    token_list = Lexer(filename).scan()
    print(token_list)


main()
