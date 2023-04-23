import ply.lex as lex
import ply.yacc as yacc
from prettytable import PrettyTable
import re

# Define the list of token names
tokens = ('ID', 'PALABRAS_RESERVADAS', 'INICIO', 'DEFINA', 'COMO', 'FIN')

# Define a regular expression
def t_PALABRAS_RESERVADAS(t):
    r'(inicio|defina|como|fin)'
    if t.value == 'inicio':
        t.type = 'INICIO'
    elif t.value == 'fin':
        t.type = 'FIN'
    elif t.value == 'defina':
        t.type = 'DEFINA'
    elif t.value == 'como':
        t.type = 'COMO'
    return t

# Define a function to handle errors
def t_error(t):
     print(f"Error: Illegal character '{t.value[0]}'")
     t.lexer.skip(1)

# Define a rule to handle whitespace
t_ignore = ' \t\n'

# Build the lexer
lexer = lex.lex()

# Define the parser
def p_S(p):
    '''S : INICIO ID FIN'''
    p[0] = (p[1], p[2], p[3])

def p_error(p):
    if p:
        print("Syntax error at line %d, column %d: Unexpected token %s" % (p.lineno, p.lexpos, p.value))
    else:
        print("Syntax error: Unexpected end of input")

parser = yacc.yacc()

# Read input from file
with open('error_cases.txt', 'r') as file:
    input_str = file.read()

# Parse the input
parsed_tokens = []
parser.parse(input_str)

# Build the table
x = PrettyTable()
x.field_names = ["Rule", "Symbol 1", "Symbol 2", "Symbol 3"]
for prod in parsed_tokens:
    x.add_row(prod)

# Print the table
print(x)
