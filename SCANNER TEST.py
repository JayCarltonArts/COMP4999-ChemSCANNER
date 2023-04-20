import ply.lex as lex
import ply.yacc as yacc
from ply.lex import Token
import re
# Define the list of token names
tokens = ( 
    'ID',
    'VALENCIA',
    'ENLACE',
    'TIPO',
    'ASIGNACION',
    'FIN_DE_LINEA',
    'ELEMENTO_QUIMICO'
    'OPERACION'
    'PARAENTESIS_IZQ',
    'PARAENTESIS_DER',
    'PALABRAS_RESERVADAS',
    'COR_IZQ',
    'COR_DER'
)




# Define a regular expression
 
def t_ASIGNACION(t):
    r':='
    return t
def t_TIPO(t):
    r'modelo'
    return t

def t_PALABRAS_RESERVADAS(t):
    r'(inicio|defina|como|fin)'
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
t_COR_IZQ=r'\['
t_COR_DER=r'\]'




# Definir las reglas de produccion

#S -> inicio sentencias fin (calls sentencia for the mIDdle content)
def p_S(p):
    '''S : PALABRAS_RESERVADAS sentencias PALABRAS_RESERVADAS'''
    print(p[0].slice)
    
    

#sentencias -> sentencia FIN_DE_LINEA sentencias (continues the code) | sentencia FIN_DE_LINEA (last statement)
def p_sentencias(p):
    '''sentencias : sentencia FIN_DE_LINEA sentencias	
                  | sentencia FIN_DE_LINEA'''
 
#sentencia -> defina ID como modelo (declaracion de variable) |ID ASIGNACION modelo_molecular(assigns a value to a variable by calling ASIGNACION) 
# | OPERACION (ID) [function operation]
def p_sentencia(p):
    '''sentencia : PALABRAS_RESERVADAS ID PALABRAS_RESERVADAS TIPO
                 | ID ASIGNACION modelo_molecular
                 | OPERACION PARAENTESIS_IZQ ID PARAENTESIS_DER'''
    
    


#<COMPUESTO>::=	"<ELEMENTO_QUIMICO>	|	<ELEMENTO_QUIMICO>	<VALENCIA>	|	<ELEMENTO>	<GRUPO_FUNCIONAL>	|	<ELEMENTO>	<GRUPO_FUNCIONAL>	<ENLACE>	|	<ELEMENTO>	<ENLACE>
def p_compuesto(p):
    '''compuesto : ELEMENTO_QUIMICO
                 | ELEMENTO_QUIMICO VALENCIA
                 | elemento grupo_funcional
                 | elemento grupo_funcional ENLACE
                 | elemento ENLACE'''

#<COMPUESTOS>::=	<COMPUESTO>	<COMPUESTOS>	|	<COMPUESTO>
def p_compuestos(p):
    '''compuestos : compuesto compuestos
                 | compuesto'''
                 

#<MODELO_MOLECULAR>::=	<ELEMENTO_QUIMICO>	|	<ELEMENTO_QUIMICO>	<VALENCIA>	|	<ELEMENTO>	<GRUPO_FUNCIONAL>	|	<COMPUESTO>	<GRUPO_FUNCIONAL>	|	<COMPUESTO>	<ELEMENTO>	<GRUPO_FUNCIONAL>	|	<COMPUESTO>	<COMPUESTO>	<COMPUESTOS>
def p_modelo_molecular(p):
    '''modelo_molecular : ELEMENTO_QUIMICO
                        | ELEMENTO_QUIMICO VALENCIA
                        | elemento grupo_funcional 
                        | compuesto grupo_funcional
                        | compuesto elemento grupo_funcional
                        | compuesto compuesto compuestos'''

#<GRUPO_FUNCIONAL>::=	<GRUPO_FUNCIONAL_INFERIOR>	<GRUPO_FUNCIONAL_SUPERIOR>	|	<GRUPO_FUNCIONAL_SUPERIOR>	<GRUPO_FUNCIONAL_INFERIOR>	|	"("	<MODELO_GRUPO_FUNCIONAL>	")"	|	"["	<MODELO_GRUPO_FUNCIONAL>	"]"
def p_grupo_funcional(p):
    '''grupo_funcional : grupo_funcional_inferior grupo_funcional_superior
                        | grupo_funcional_superior grupo_funcional_inferior
                        | grupo_funcional_superior
                        | grupo_funcional_inferior'''

#<GRUPO_FUNCIONAL_SUPERIOR>::=	"("	<MODELO_GRUPO_FUNCIONAL>	")"

def p_grupo_funcional_superior(p):
    '''grupo_funcional_superior : PARAENTESIS_IZQ modelo_grupo_funcional PARAENTESIS_DER'''

#<GRUPO_FUNCIONAL_INFERIOR>::=	"["	<MODELO_GRUPO_FUNCIONAL>	"]"

def p_grupo_funcional_inferior(p):
    '''grupo_funcional_inferior : COR_IZQ modelo_grupo_funcional COR_DER'''

#<MODELO_GRUPO_FUNCIONAL>::=	<ENLACE>	<MODELO_MOLECULAR>	|	<ELEMENTO_QUIMICO>	|	<ELEMENTO_QUIMICO>	<VALENCIA>	|	<ELEMENTO>	<GRUPO_FUNCIONAL>	|	<COMPUESTO>	<ELEMENTO>	|	<COMPUESTO>	<ELEMENTO>	<GRUPO_FUNCIONAL>	|	<COMPUESTO>	<COMPUESTO>	<COMPUESTOS>
def p_modelo_grupo_funcional(p):
    '''modelo_grupo_funcional : ENLACE modelo_molecular
                              | ELEMENTO_QUIMICO
                              | ELEMENTO_QUIMICO VALENCIA
                              | elemento grupo_funcional
                              | compuesto elemento
                              | compuesto elemento grupo_funcional
                              | compuesto compuesto compuestos'''

#<MODELO_GRUPO_FUNCIONAL>::=	<ENLACE>	<MODELO_MOLECULAR>	|	<ELEMENTO_QUIMICO>	|	<ELEMENTO_QUIMICO>	<VALENCIA>	|	<ELEMENTO>	<GRUPO_FUNCIONAL>	|	<COMPUESTO>	<ELEMENTO>	|	<COMPUESTO>	<ELEMENTO>	<GRUPO_FUNCIONAL>	|	<COMPUESTO>	<COMPUESTO>	<COMPUESTOS>

def p_elemento(p):
    ''' elemento : ELEMENTO_QUIMICO
            | ELEMENTO_QUIMICO VALENCIA '''
    

# Define a function to handle errors
def t_error(t):
     print(f"Error: Illegal character 't.value[0]'")
     t.lexer.skip(1)
# Define a rule to handle whitespace
t_ignore = ' \t\n'

# Error rule for syntax errors
def p_error(p):
    raise SyntaxError(f"Syntax error at line {p.lineno}, position {p.lexpos}: Unexpected token {p.value}")
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
       s = i
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
