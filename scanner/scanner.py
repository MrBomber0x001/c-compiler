from enum import Enum
import os

class TokenType(Enum):
    # Keywords
    INT = "INT"
    FLOAT = "FLOAT"
    DOUBLE = "DOUBLE"
    CHAR = "CHAR"
    VOID = "VOID"
    IF = "IF"
    ELSE = "ELSE"
    WHILE = "WHILE"
    FOR = "FOR"
    RETURN = "RETURN"

    # Operators
    PLUS = "PLUS"
    MINUS = "MINUS"
    MULTIPLY = "MULTIPLY"
    DIVIDE = "DIVIDE"
    ASSIGN = "ASSIGN"
    EQUAL = "EQUAL"
    NOT_EQUAL = "NOT_EQUAL"
    LESS_THAN = "LESS_THAN"
    GREATER_THAN = "GREATER_THAN"
    LESS_THAN_EQUAL = "LESS_THAN_EQUAL"
    GREATER_THAN_EQUAL = "GREATER_THAN_EQUAL"

    # Delimiters
    SEMICOLON = "SEMICOLON"
    COMMA = "COMMA"
    LPAREN = "LPAREN"
    RPAREN = "RPAREN"
    LBRACE = "LBRACE"
    RBRACE = "RBRACE"
    LBRACKET = "LBRACKET"
    RBRACKET = "RBRACKET"

    # Literals
    IDENTIFIER = "IDENTIFIER"
    NUMBER = "NUMBER"
    STRING = "STRING"

    # Comments
    SINGLE_LINE_COMMENT = "SINGLE_LINE_COMMENT"
    MULTI_LINE_COMMENT = "MULTI_LINE_COMMENT"

    # Built-in
    INCLUDE = "INCLUDE"
    HEADER = "HEADER"
    PREPROCESSOR = "PREPROCESSOR"
    CHAR_LITERAL = "CHAR_LITERAL"

    # Special
    EOF = "EOF"
class Token:
    def __init__(self, type, literal):
        self.type = type
        self.literal = literal

    def __repr__(self):
        return f"Token(type={self.type}, literal='{self.literal}')"

class Scanner:
    def __init__(self, input):
        self.input = input
        self.position = 0
        self.read_position = 0
        self.ch = ''
        self.read_char()

    def read_char(self):
        if self.read_position >= len(self.input):
            self.ch = '\0'  # EOF
        else:
            self.ch = self.input[self.read_position]
        self.position = self.read_position
        self.read_position += 1

    def read_char_literal(self):
        self.read_char()  # Skip opening quote
        char = self.ch
        self.read_char()  # Read the character
        if self.ch == "'":  # Skip closing quote
            self.read_char()
        return char

    def peek_char(self):
        if self.read_position >= len(self.input):
            return '\0'
        else:
            return self.input[self.read_position]

    def skip_whitespace(self):
        while self.ch in [' ', '\t', '\n', '\r']:
            self.read_char()

    def read_single_line_comment(self):
        # Skip the '//' characters
        self.read_char()
        self.read_char()
        start = self.position
        while self.ch != '\n' and self.ch != '\0':
            self.read_char()
        return self.input[start:self.position].strip()

    def read_multi_line_comment(self):
        self.read_char()  # Skip /
        self.read_char()  # Skip *
        start = self.position
        while not (self.ch == '*' and self.peek_char() == '/') and self.ch != '\0':
            self.read_char()
        if self.ch == '*' and self.peek_char() == '/':
            comment = self.input[start:self.position].strip()
            self.read_char()  # Skip *
            self.read_char()  # Skip /
            return comment
        return self.input[start:self.position].strip()

    def read_identifier(self):
        start = self.position
        while self.is_letter(self.ch) or self.is_digit(self.ch):
            self.read_char()
        return self.input[start:self.position]

    def read_number(self):
        start = self.position
        while self.is_digit(self.ch):
            self.read_char()
        if self.ch == '.' and self.is_digit(self.peek_char()):
            self.read_char()
            while self.is_digit(self.ch):
                self.read_char()
        return self.input[start:self.position]

    def read_string(self):
        start = self.position + 1
        while True:
            self.read_char()
            if self.ch == '"' or self.ch == '\0':
                break
        return self.input[start:self.position]
    
    def read_header(self):
        # Skip the initial '<'
        self.read_char()
        start = self.position
        while self.ch != '>' and self.ch != '\0':
            self.read_char()
        return self.input[start:self.position]

    def is_letter(self, ch):
        return 'a' <= ch <= 'z' or 'A' <= ch <= 'Z' or ch == '_'

    def is_digit(self, ch):
        return '0' <= ch <= '9'

    def lookup_keyword(self, identifier):
        keywords = {
            'int': TokenType.INT,
            'float': TokenType.FLOAT,
            'double': TokenType.DOUBLE,
            'char': TokenType.CHAR,
            'void': TokenType.VOID,
            'if': TokenType.IF,
            'else': TokenType.ELSE,
            'while': TokenType.WHILE,
            'for': TokenType.FOR,
            'return': TokenType.RETURN,
        }
        return keywords.get(identifier)

    def next_token(self):
        self.skip_whitespace()

        if self.ch == '/' and self.peek_char() == '/':
            return Token(TokenType.SINGLE_LINE_COMMENT, self.read_single_line_comment())
        elif self.ch == '/' and self.peek_char() == '*':
            return Token(TokenType.MULTI_LINE_COMMENT, self.read_multi_line_comment())
        elif self.ch == '#':
            self.read_char()
            return Token(TokenType.PREPROCESSOR, '#' + self.read_identifier())
        elif self.ch == '<' and self.peek_char() != '=':
            return Token(TokenType.HEADER, self.read_header())
        elif self.ch == "'":
            return Token(TokenType.CHAR_LITERAL, self.read_char_literal())

        token = None
        
        if self.ch == '=':
            if self.peek_char() == '=':
                ch = self.ch
                self.read_char()
                token = Token(TokenType.EQUAL, ch + self.ch)
            else:
                token = Token(TokenType.ASSIGN, self.ch)
        elif self.ch == '+':
            token = Token(TokenType.PLUS, self.ch)
        elif self.ch == '-':
            token = Token(TokenType.MINUS, self.ch)
        elif self.ch == '*':
            token = Token(TokenType.MULTIPLY, self.ch)
        elif self.ch == '/':
            token = Token(TokenType.DIVIDE, self.ch)
        elif self.ch == '<':
            if self.peek_char() == '=':
                ch = self.ch
                self.read_char()
                token = Token(TokenType.LESS_THAN_EQUAL, ch + self.ch)
            else:
                token = Token(TokenType.LESS_THAN, self.ch)
        elif self.ch == '>':
            if self.peek_char() == '=':
                ch = self.ch
                self.read_char()
                token = Token(TokenType.GREATER_THAN_EQUAL, ch + self.ch)
            else:
                token = Token(TokenType.GREATER_THAN, self.ch)
        elif self.ch == ';':
            token = Token(TokenType.SEMICOLON, self.ch)
        elif self.ch == ',':
            token = Token(TokenType.COMMA, self.ch)
        elif self.ch == '(':
            token = Token(TokenType.LPAREN, self.ch)
        elif self.ch == ')':
            token = Token(TokenType.RPAREN, self.ch)
        elif self.ch == '{':
            token = Token(TokenType.LBRACE, self.ch)
        elif self.ch == '}':
            token = Token(TokenType.RBRACE, self.ch)
        elif self.ch == '\0':
            token = Token(TokenType.EOF, '')
        else:
            if self.is_letter(self.ch):
                identifier = self.read_identifier()
                keyword_type = self.lookup_keyword(identifier)
                if keyword_type:
                    return Token(keyword_type, identifier)
                return Token(TokenType.IDENTIFIER, identifier)
            elif self.is_digit(self.ch):
                return Token(TokenType.NUMBER, self.read_number())
            else:
                token = Token(TokenType.EOF, self.ch)

        self.read_char()
        return token

def main():
    file_path = os.path.join(os.path.dirname(__file__), 'input.c')

    with open(file_path, 'r') as file:
        data = file.read()

    scanner = Scanner(data)

    token = scanner.next_token()
    while token.type != TokenType.EOF:
        print(token)
        token = scanner.next_token()

if __name__ == "__main__":
    main()