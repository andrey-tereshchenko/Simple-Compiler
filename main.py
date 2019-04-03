from lexer import *
from parser import Parser


def main():
    filename = 'test/test_whileloop.pas'
    token_list = Lexer(filename).scan()
    instruction_list = Parser(token_list).start_parser()
    print(instruction_list)


main()
