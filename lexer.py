import ply.lex as lex

reserved = {
    'repeat': 'REPEAT',
    'from': 'FROM',
    'to': 'TO',
    'do': 'DO',
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'end': 'END'
}

tokens = list(reserved.values()) + [
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'IDENTIFIER',
    'EQUALS',
    'LBRACKET',
    'RBRACKET',
    'COMMA',
    'STRING',
    'SEMICOLON',
    'COLON',
    'GT',
    'LT'
]

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQUALS = r'='
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COMMA = r','
t_STRING = r'\"([^\\\"]|\\.)*\"'
t_SEMICOLON = r';'
t_REPEAT = r'repeat'
t_IF = r'if'
t_THEN = r'then'
t_ELSE = r'else'
# t_END = r'end'
t_FROM = r'from'
t_TO = r'to'
t_COLON = r'\:'
t_DO = r'do'
t_GT = r'\>'
t_LT = r'\<'


def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')  # Check for reserved words
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignoring spaces and tabs
t_ignore = ' \t'

# def t_END(t):
#     r'end'
#     print(f"Token END: {t.value} at line {t.lineno}")
#     return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}")
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

