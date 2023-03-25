import ply.lex as lex
from ply.lex import Token
import re
# Define the list of token names
tokens = (
    'ID',
    'IDCONT',
    'LETRA',
    'DIGITO',
    'VALENCIA',
    'TIPO',
    'ENLACE',
    'FIN_DE_LINEA',
    'ELEMENTO_QUIMICO'
    'DECLARACION_DE_VARIABLE',
    'OPERACION_CON_MODELO',
    'OPERACION',
    'GRAFICAR',
    'PROPIEDADES_FISICAS',
    'SENTENCIA',
    'SENTENCIAS',
    'DEFINICION_DEL_MODELO',
    'MODELO_MOLECULAR',
    'ELEMENTO',
    'CADENA_MOLECULAR',
    'CADENA_ATOMICA',
    'GRUPO_FUNCIONAL',
    'GRUPO_FUNCIONAL_SUPERIOR',
    'GRUPO_FUNCIONAL_INFERIOR',
    'COMPUESTO',
    'COMPUESTOS',
    'MODELO_GRUPO_FUNCIONAL'
)

# Define the regular expression for each token
t_FIN_DE_LINEA=r'\;|\:'
t_ENLACE=r'\;|:=|\='

# Define a regular expression 
t_LETRA= r'\w+'
t_DIGITO=r'\d+'#Any digit from 0-9
t_ELEMENTO_QUIMICO= r'H|Li|Na|K|Rb|Cs|Fr|Be|Mg|Ca|Sr|Ba|Ra|Sc|Y|Ti|Zr|Hf|Db|V|Nb|Ta|Jl|Cr|Mo|W|Rf|Mn|Tc|Re|Bh|Fe|Ru|Os|Hn|Co|Rh|Ir|Mt|Ni|Pd|Pt|Cu|Ag|Au|Zn|Cd|Hg|B|Al|Ga|ln|Tl|C|Si|Ge|Sn|Pb|N|P|As|Sb|Bi|O|S|Se|Te|Po|F|Cl|Br|I|At|He|Ne|Ar|Kr|Xe|Rn'
t_TIPO= r'modelo'
t_OPERACION=r'graficar2d|graficar3d|pesomolecular'
t_VALENCIA= r'[1-9]'#Any digit from 0-9
t_IDCONT = t_LETRA + r'|' + r'(' + t_LETRA + r')' + t_LETRA + r'|' + t_DIGITO + r'|' + r'(' + t_DIGITO + r')' + t_LETRA 
t_ID = t_LETRA + r'|' + r'(' + t_LETRA + r')' + t_IDCONT

    

# Define a rule to handle whitespace
t_ignore = ' \t\n'

# Definir las reglas de produccion
t_ELEMENTO= t_ELEMENTO_QUIMICO + r'|' + t_ELEMENTO_QUIMICO + r'(' + t_VALENCIA + r')'
t_COMPUESTO=r'{t_ELEMENTO_QUIMICO} | {t_ELEMENTO_QUIMICO (t_VALENCIA)} | {t_ELEMENTO (t_GRUPO_FUNCIONAL)} | {t_ELEMENTO (t_GRUPO_FUNCIONAL)(t_ENLACE)} |{t_ELEMENTO (t_ENLACE)}'

t_COMPUESTOS= t_COMPUESTO + r'('+ t_COMPUESTOS +r')'+ r'|'+ t_COMPUESTO


t_GRUPO_FUNCIONAL=r'{t_GRUPO_FUNCIONAL_INFERIOR(t_GRUPO_FUNCIONAL_SUPERIOR)} | {t_GRUPO_FUNCIONAL_SUPERIOR(t_GRUPO_FUNCIONAL_INFERIOR)} | ({t_MODELO_GRUPO_FUNCIONAL}) | [{t_MODELO_GRUPO_FUNCIONAL}]'

t_MODELO_MOLECULAR= t_ELEMENTO_QUIMICO + r'|' + t_ELEMENTO_QUIMICO + r'(' + t_VALENCIA + r')' + r'|' + t_ELEMENTO + r'(' + t_GRUPO_FUNCIONAL + r')' + r'|' + t_COMPUESTO + r'(' + t_GRUPO_FUNCIONAL+r')'+ r'|'+ t_COMPUESTO+ r'(' + t_ELEMENTO + r')' +r'('+ t_GRUPO_FUNCIONAL + r')'+ r'|'+ t_COMPUESTO + r'(' + t_COMPUESTO + r')' + r'(' + t_COMPUESTOS + r')'
 
t_MODELO_GRUPO_FUNCIONAL=t_ENLACE + (t_MODELO_MOLECULAR) | {t_ELEMENTO_QUIMICO} | {t_ELEMENTO_QUIMICO (t_VALENCIA)} | {t_ELEMENTO(t_GRUPO_FUNCIONAL)} | {t_COMPUESTO(t_ELEMENTO)} | {t_COMPUESTO(t_ELEMENTO)(t_GRUPO_FUNCIONAL)} | {t_COMPUESTO(t_COMPUESTO)(t_COMPUESTOS)}'

t_GRUPO_FUNCIAL_INFERIOR= r'[' + t_MODELO_GRUPO_FUNCIONAL + r']'

t_GRUPO_FUNCIONAL_SUPERIOR= r'(' + t_MODELO_GRUPO_FUNCIONAL + r')'

















t_SENTENCIA= r'defina' + r'(' + t_ID + r')' + r'como' + r'(' + t_TIPO + r'|' + t_ID + r')' + r'=' + r'('+ t_MODELO_MOLECULAR + r'|' {t_OPERACION}) ({ID})'

t_SENTENCIAS (t):
    t_SENTENCIA (t_FIN_DE_LINEA)(t_SENTENCIAS) | t_SENTENCIA(t_FIN_DE_LINEA)






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
    print(f"Matched TOKEN: {tok.type}: {tok.value}")
