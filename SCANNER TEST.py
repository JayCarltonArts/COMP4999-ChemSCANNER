import ply.lex as lex
import ply.yacc as yacc
from ply.lex import Token
import re
# Define the list of token names
tokens = ( 'ID',
#    'IDCONT',
    'VALENCIA',
    'ENLACE',
    'TIPO',
    'ASIGNACION',
    'FIN_DE_LINEA',
    'ELEMENTO_QUIMICO',
    # 'DECLARACION_DE_VARIABLE',
    # 'OPERACION_CON_MODELO',
    'OPERACION',
    # 'GRAFICAR',
    # 'PROPIEDADES_FISICAS',
    # 'SENTENCIA',
    # 'SENTENCIAS',
    # 'DEFINICION_DEL_MODELO',
    # 'MODELO_MOLECULAR',
    # 'ELEMENTO',
    # 'CADENA_MOLECULAR',
    # 'CADENA_ATOMICA',
     'GRUPO_FUNCIONAL',
    # 'GRUPO_FUNCIONAL_SUPERIOR',
    # 'GRUPO_FUNCIONAL_INFERIOR',
    # 'COMPUESTO',
     'COMPUESTOS',
    # 'MODELO_GRUPO_FUNCIONAL'
    'PARAENTESIS_IZQ',
    'PARAENTESIS_DER',
    'PALABRAS_RESERVADAS'
)




# Define a regular expression
 
def t_ASIGNACION(t):
    r':='
    return t
def t_TIPO(t):
    r'modelo'
    return t
def t_PALABRAS_RESERVADAS(t):
    r'inicio|defina|como|fin'
    return t

def t_ELEMENTO_QUIMICO(t):
    r'Ag|Al|Ar|As|At|Au|Ba|Be|Bh|Bi|Br|Ca|Cd|Cl|Co|Cr|Cs|Cu|Db|Fe|Fr|Ga|Ge|He|Hf|Hg|Hn|Ir|Jl|Kr|Li|ln|Mg|Mn|Mo|Mt|Na|Nb|Ne|Ni|Os|Pb|Pd|Po|Pt|Ra|Rb|Re|Rf|Rh|Rn|Ru|Sb|Sc|Se|Si|Sn|Sr|Ta|Tc|Te|Ti|Tl|Xe|Zn|Zr|B|C|F|H|I|K|N|O|P|S|V|W|Y'
    return t

def t_OPERACION(t):
    r'graficar2d|graficar3d|pesomolecular'
    return t
def t_VALENCIA(t):
    r'[1-9]'
    return t



# Define the regular expression for each token
t_FIN_DE_LINEA=r'\;|\:'
t_ID= r'[a-zA-Z][a-zA-Z0-9_]*'
t_ENLACE=r'\-|\:\:|\:|\='
t_PARAENTESIS_IZQ= r'\('
t_PARAENTESIS_DER= r'\)'




# Definir las reglas de produccion

def p_S(p):
    '''S : PALABRAS_RESERVADAS SENTENCIAS PALABRAS_RESERVADAS'''

def p_SENTENCIAS(p):
    '''SENTENCIAS : SENTENCIA FIN_DE_LINEA SENTENCIAS	
                  | SENTENCIA FIN_DE_LINEA'''

def p_SENTENCIA(p):
    '''SENTENCIA : PALABRAS_RESERVADAS variable PALABRAS_RESERVADAS TIPO
                 | ASIGNACION
                 | OPERACION PARAENTESIS_IZQ variable PARAENTESIS_DER'''

def p_ASIGNACION(p):
    '''variable : MODELO_MOLECULAR'''   
    p[0] = p[1] 

def p_COMPUESTO(p):
    '''COMPUESTO : ELEMENTO_QUIMICO'''

def p_MODELO_MOLECULAR(p):
    '''MODELO_MOLECULAR : ELEMENTO_QUIMICO
                        | ELEMENTO_QUIMICO VALENCIA
                        | ELEMENTO GRUPO_FUNCIONAL 
                        | COMPUESTO GRUPO_FUNCIONAL
                        | COMPUESTO ELEMENTO GRUPO_FUNCIONAL
                        | COMPUESTO COMPUESTO COMPUESTOS'''

def p_variable(p):
    '''variable : ID'''

def p_ELEMENTO(p):
    ''' ELEMENTO : ELEMENTO_QUIMICO
            | ELEMENTO_QUIMICO VALENCIA '''

def p_DECLARACION_DE_VARIABLE(p):
    '''variable : PALABRAS_RESERVADAS variable PALABRAS_RESERVADAS TIPO FIN_DE_LINEA'''
    

    
'''t_IDCONT = r'\w+|(\w+)\w+|\d+|(\d+)\w+'




t_GRUPO_FUNCIONAL_INFERIOR= r'\[' + t_MODELO_GRUPO_FUNCIONAL + r'\]'

t_GRUPO_FUNCIONAL_SUPERIOR= r'\(' + t_MODELO_GRUPO_FUNCIONAL + r'\)'

t_GRUPO_FUNCIONAL=t_GRUPO_FUNCIONAL_INFERIOR+r'('+t_GRUPO_FUNCIONAL_SUPERIOR+ r')'  + r'|' + t_GRUPO_FUNCIONAL_SUPERIOR+r'('+t_GRUPO_FUNCIONAL_INFERIOR+r')' +r'|'+ r'('+t_MODELO_GRUPO_FUNCIONAL+r')'+ r'|' +r'['+t_MODELO_GRUPO_FUNCIONAL+r']'


t_COMPUESTO= t_ELEMENTO_QUIMICO+ r'|' +t_ELEMENTO_QUIMICO +r'('+t_VALENCIA+ r')' + r'|'+ t_ELEMENTO +r'('+t_GRUPO_FUNCIONAL+ r')' + r'|' +t_ELEMENTO +r'('+t_GRUPO_FUNCIONAL+r')'+r'('+t_ENLACE+r')'+ r'|'+t_ELEMENTO +r'('+t_ENLACE+r')'

t_COMPUESTOS= t_COMPUESTO + r'+'+ r'|' + t_COMPUESTO

t_MODELO_MOLECULAR= t_ELEMENTO_QUIMICO + r'|' + t_ELEMENTO_QUIMICO + r'(' + t_VALENCIA + r')' + r'|' + t_ELEMENTO + r'(' + t_GRUPO_FUNCIONAL + r')' + r'|' + t_COMPUESTO + r'(' + t_GRUPO_FUNCIONAL+r')'+ r'|'+ t_COMPUESTO+ r'(' + t_ELEMENTO + r')' +r'('+ t_GRUPO_FUNCIONAL + r')'+ r'|'+ t_COMPUESTO + r'(' + t_COMPUESTO + r')' + r'(' + t_COMPUESTOS + r')'

t_MODELO_GRUPO_FUNCIONAL=t_ENLACE + r'('+t_MODELO_MOLECULAR+r')'+ r'|' +t_ELEMENTO_QUIMICO +r'|'+ t_ELEMENTO_QUIMICO +r'('+t_VALENCIA+r')'+ r'|'+ t_ELEMENTO+r'('+t_GRUPO_FUNCIONAL+r')'+ r'|' +t_COMPUESTO+r'('+t_ELEMENTO+r')'+ r'|' +t_COMPUESTO+r'('+t_ELEMENTO+r')'+r'('+t_GRUPO_FUNCIONAL+r')' +r'|'+ t_COMPUESTO+r'('+t_COMPUESTO+r')'+r'('+t_COMPUESTOS+r')'


t_SENTENCIA= r'defina' + r'(' + t_ID + r')' + r'como' + r'(' + t_TIPO + r'|' + t_ID + r')' + r'=' + r'('+ t_MODELO_MOLECULAR + r'|' +t_OPERACION+r')'+ r'('+t_ID+r')'


t_SENTENCIAS=t_SENTENCIA + r'(' + t_FIN_DE_LINEA+r')+'+ r'|' +t_SENTENCIA+r'('+t_FIN_DE_LINEA+r')' '''

# Define a function to handle errors
def t_error(t):
     print(f"Error: Illegal character 't.value[0]'")
     t.lexer.skip(1)
# Define a rule to handle whitespace
t_ignore = ' \t\n'

# Error rule for syntax errors
def p_error(p):
    raise SyntaxError(f"Syntax error at line {p.lineno}, position {p.lexpos}: Unexpected token {p.value}")
    
# Build the lexer
lexer = lex.lex()

# Build the parser
parser = yacc.yacc(debug=True)

# # Test the lexer
with open ('error_cases.txt','r') as file:
     i = file.read()

lexer.input(i)
for tok in lexer:
     print(tok)


while True:
    try:
       with open ('error_cases.txt','r') as file:
            i = file.read()
    except EOFError:
       break
    if not i: continue
    result = parser.parse(i)
    print(result)
