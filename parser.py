import ply.yacc as yacc
from lexer import tokens  # Import tokens from your lexer

# Define grammar rules
def p_statement_assign(p):
    'statement : IDENTIFIER EQUALS expression'
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

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

# Test the parser
result = parser.parse('x = 3 + 4 * 2')
print(result)
