import ply.lex as lex

# Define the list of token names
tokens = [
    'LETRA',
    'DIGITO',
    'VALENCIA',
    'TIPO',
    'ENLACE',
    'FIN_DE_LINEA',
        
        
    'DECLARACION_DE_VARIABLE',
    'ID',
    'IDCONT',
    
    
    'OPERACION_CON_MODELO',
    'OPERACION',
    'GRAFICAR',
    'PROPIEDADES_FISICAS',
    

    'SENTENCIA',
    'SENTENCIAS',

    
    'DEFINICION_DEL_MODELO',
    'MODELO_MOLECULAR',
    'ELEMENTO_QUIMICO',
    'ELEMENTO',
    
    'CADENA_MOLECULAR',
    'CADENA_ATOMICA',
    'GRUPO_FUNCIONAL',
    'GRUPO_FUNCIONAL_SUPERIOR',
    'GRUPO_FUNCIONAL_INFERIOR',
    
    
    'COMPUESTO',
    'COMPUESTOS',
    'MODELO_GRUPO_FUNCIONAL'
]

# Define the regular expression for each token
t_FIN_DE_LINEA=r'\;|\:'
t_ENLACE=r'\;|\:=|\='

'''t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SPACE= r'\  '''

''' Define a regular expression for the DIGITO token 
needs to be ordered in a specific way'''
def t_TIPO(t):
    r'modelo'
    return t
def t_VALENCIA(t):
    r'[1-9]'#Any digit from 0-9
    t.value = int(t.value)
    return t
def t_DIGITO(t):
    r'\d'#Any digit from 0-9
    t.value = int(t.value)
    return t

def t_LETRA(t):
    r'[a-zA-Z]'
    t.value = str(t.value)
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
for tok in lexer:
    print(tok)