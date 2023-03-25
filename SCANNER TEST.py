import ply.lex as lex

# Define the list of token names
tokens = (
    'IDCONT',
    'LETRA',
    'DIGITO',
    'VALENCIA',
    'TIPO',
    'ENLACE',
    'FIN_DE_LINEA'
    

)

# Define the regular expression for each token
t_FIN_DE_LINEA=r'\;|\:'
t_ENLACE=r'\;|\:=|\='

# Define a regular expression 
def t_IDCONT(t):
    r'{t_LETRA}({t_LETRA}|{t_DIGITO})+'
    return t 

def t_TIPO(t):
    r'modelo'
    return t
def t_VALENCIA(t):
    r'[1-9]'#Any digit from 0-9
    t.value = int(t.value)
    return t
def t_DIGITO(t):
    r'\d'#Any digit from 0-9
    t.value =int(t.value)
    return t

def t_LETRA(t):
    r'[a-zA-Z]'
    t.value=str(t.value)
    return t



# Define a rule to handle whitespace
t_ignore = ' \t\n'

# Definir las reglas de produccion


# Define a function to handle errors
def t_error(t):
    print(f"Error: Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test the lexer
Raw = input('WRITE:' )
lexer.input(Raw)
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)
