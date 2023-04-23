import ply.lex as lex
import ply.yacc as yacc
from prettytable import PrettyTable
import re
# Define the list of token names
tokens = ('ID', 'PALABRAS_RESERVADAS', 'INICIO', 'DEFINA', 'COMO', 'FIN')


def t_PALABRAS_RESERVADAS(t):
    r'(inicio|defina|como|fin)'
    if t.value == 'inicio':
        t.type = 'INICIO'
    elif t.value == 'fin':
        t.type = 'FIN'
    return t




# Define the regular expression for each token
t_ID= r'[a-zA-Z][a-zA-Z0-9_]*'

# Define a function to handle errors
def t_error(t):
     print(f"Error: Illegal character '{t.value[0]}'")
     t.lexer.skip(1)
     
# Define a rule to handle whitespace
t_ignore = ' \t\n'

# Build the lexer
lexer = lex.lex()



# # Test the lexer
with open ('error_cases.txt','r') as file:
     i = file.read()

lexer.input(i)
for tok in lexer:
     print(tok)

parsed_tokens = []

# Definir las reglas de produccion
start = 'S'


#S -> inicio sentencias fin (calls sentencia for the middle content)
def p_S(p):
    '''S : INICIO ID FIN'''
     # Extract the types of the symbols from the slice
    symbol_types = [symbol.type for symbol in p.slice[1:]]

    # Convert the list of types to a string
    symbol_types_str = ' '.join(symbol_types)
    parsed_tokens.append((p.slice[0].type, symbol_types_str))



# Error rule for syntax errors
def p_error(p):
    # raise SyntaxError(f"Syntax error at line {p.lineno}, position {p.lexpos}: Unexpected token {p.value}")
    if p:
            print("Syntax error at line %d, column %d: Unexpected token %s" % (p.lineno, p.lexpos, p.value))
    else:
        print("Syntax error: Unexpected end of input")





# Build the parser
parser = yacc.yacc(debug=True)

# Test the Parser
with open ('error_cases.txt','r') as file:
     i = file.read()

parser.parse(i)
# Build the table
x = PrettyTable()
x.field_names = ["Rule", "Symbol 1"]
for prod in parsed_tokens:
    x.add_row(prod)

print(x)
while True:
    try:
       s = i
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    exit()
