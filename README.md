# C Compiler Project

This repository contains the development of a C compiler, focusing on the initial stages of the compilation process. Currently, the project encompasses the implementation of a scanner and parser, laying the groundwork for further development.


To run this project, execute the following command:

```sh
python3 scanner.py input.c
```

the output would be look like this
```sh
Token(type=TokenType.SINGLE_LINE_COMMENT, literal='This is a single-line comment')
Token(type=TokenType.PREPROCESSOR, literal='#include')
Token(type=TokenType.HEADER, literal='stdio.h')
Token(type=TokenType.GREATER_THAN, literal='>')
Token(type=TokenType.MULTI_LINE_COMMENT, literal='* This is a multi-line comment
 * that spans multiple lines.')
Token(type=TokenType.INT, literal='int')
Token(type=TokenType.IDENTIFIER, literal='main')
Token(type=TokenType.LPAREN, literal='(')
Token(type=TokenType.RPAREN, literal=')')
Token(type=TokenType.LBRACE, literal='{')
Token(type=TokenType.INT, literal='int')
Token(type=TokenType.IDENTIFIER, literal='a')
Token(type=TokenType.ASSIGN, literal='=')
Token(type=TokenType.NUMBER, literal='5')
Token(type=TokenType.SEMICOLON, literal=';')
Token(type=TokenType.SINGLE_LINE_COMMENT, literal='Another single-line comment')
Token(type=TokenType.FLOAT, literal='float')
Token(type=TokenType.IDENTIFIER, literal='b')
Token(type=TokenType.ASSIGN, literal='=')
Token(type=TokenType.NUMBER, literal='3.14')
Token(type=TokenType.SEMICOLON, literal=';')
Token(type=TokenType.FLOAT, literal='float')
Token(type=TokenType.IDENTIFIER, literal='c')
Token(type=TokenType.ASSIGN, literal='=')
Token(type=TokenType.IDENTIFIER, literal='a')
Token(type=TokenType.PLUS, literal='+')
Token(type=TokenType.IDENTIFIER, literal='b')
Token(type=TokenType.SEMICOLON, literal=';')
Token(type=TokenType.MULTI_LINE_COMMENT, literal='This is another multi-line comment')
Token(type=TokenType.INT, literal='int')
Token(type=TokenType.IDENTIFIER, literal='x')
Token(type=TokenType.ASSIGN, literal='=')
Token(type=TokenType.NUMBER, literal='5')
Token(type=TokenType.SEMICOLON, literal=';')
Token(type=TokenType.IF, literal='if')
Token(type=TokenType.LPAREN, literal='(')
Token(type=TokenType.IDENTIFIER, literal='x')
Token(type=TokenType.GREATER_THAN, literal='>')
Token(type=TokenType.NUMBER, literal='0')
Token(type=TokenType.RPAREN, literal=')')
Token(type=TokenType.LBRACE, literal='{')
Token(type=TokenType.RETURN, literal='return')
Token(type=TokenType.NUMBER, literal='1')
Token(type=TokenType.SEMICOLON, literal=';')
Token(type=TokenType.RBRACE, literal='}')
Token(type=TokenType.ELSE, literal='else')
Token(type=TokenType.LBRACE, literal='{')
Token(type=TokenType.RETURN, literal='return')
Token(type=TokenType.NUMBER, literal='0')
Token(type=TokenType.SEMICOLON, literal=';')
Token(type=TokenType.RBRACE, literal='}')
Token(type=TokenType.RBRACE, literal='}')
```
