import ply.yacc as yacc
from lexer import tokens  # Import tokens from your lexer

# Define grammar rules
def p_program(p):
    '''program : program statement
               | statement'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_statement(p):
    'statement : expression SEMICOLON'
    p[0] = p[1]


def p_expression_assign(p):
    'expression : IDENTIFIER EQUALS expression'
    p[0] = ('assign', p[1], p[3])

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    p[0] = ('binop', p[2], p[1], p[3])

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = ('number', p[1])

def p_expression_identifier(p):
    'expression : IDENTIFIER'
    p[0] = ('var', p[1])

def p_expression_list(p):
    'expression : LBRACKET arguments RBRACKET'
    p[0] = ('list', p[2])

def p_arguments(p):
    '''arguments : expression
                 | arguments COMMA expression
                 | empty'''
    if len(p) == 2 and p[1] is not None:
        p[0] = [p[1]]
    elif len(p) == 2:  # Handle the empty case
        p[0] = []
    else:
        p[0] = p[1] + [p[3]]


def p_expression_string(p):
    'expression : STRING'
    p[0] = ('string', p[1])


def p_expression_function_call(p):
    'expression : IDENTIFIER LPAREN arguments RPAREN'
    p[0] = ('function_call', p[1], p[3])

def p_empty(p):
    'empty :'
    p[0] = None

# Error rule for syntax errors
def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}' on line {p.lineno}")
    else:
        print("Syntax error at EOF")



# Build the parser
parser = yacc.yacc(start='program')

