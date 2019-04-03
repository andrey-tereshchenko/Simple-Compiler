# Compiler
Compiler written in python without external dependencies

# BNF
```
program = "program", identifier, ";", block, ".";
functions = {"function", identifier, "(", var_dec, ")", ";", block};
block = [functions], ["var", var_dec], [statements];
var_dec = (identifier, {,",", identifier}, ":", type, ";")+
statements = "begin", statement, {";", statement}, "end";
statement = attribution | statements | print | if | while;
attribution = identifier, "=", (expression | read);
print = "print", "(", expression, ")";
read = "read", "(", ")";
if = "if", rel_expression, "then", statement, ["else" statement"];
while = "while", rel_expression, "do", statement;
rel_expression = expression, {comp, expression};
expression = term, { ("+"|"-"|"or"), term, };
term = factor, { ("*" | "/" | "and"), factor };
factor = ("+" | "-" | "not"), (factor | number | boolean | ("(" expression ")") | identifier | func_call);
func_call = identifier, "(", [expression, {",", expression}], ")";
identifier = letter, {letter | digit | "_" };
comp = ">" | "<" | "==" | "!=";
number = digit+;
boolean = "true" | "false";
type = "int" | "boolean";
letter = [a-zA-Z];
digit = [0-9];
```
# Lexical Analyzer
The main task of lexical analysis is to read input characters in the code and produce tokens.

Lexical analyzer scans the entire source code of the program. It identifies each token one by one. 
Scanners are usually implemented to produce tokens only when requested by a parser. Here is how this works:
![Alt Text](https://www.guru99.com/images/1/020819_1105_LexicalAnal1.png)
1. "Get next token" is a command which is sent from the parser to the lexical analyzer.
1. On receiving this command, the lexical analyzer scans the input until it finds the next token.
1. It returns the token to Parser.

Lexical Analyzer skips whitespaces and comments while creating these tokens. If any error
is present, then Lexical analyzer will correlate that error with the source file and line number.
# Parser
The parser is a compiler component that breaks down data into smaller elements for easy translation into another language. The parser accepts 
input data in the form of a sequence of tokens or program instructions and usually builds the data structure in the form
of a parse tree or an abstract syntax tree.
# Simulator

# Examples
## if

## for

## while

## array 

## procedure
