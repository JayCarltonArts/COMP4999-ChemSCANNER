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
    

)

# Define the regular expression for each token
t_FIN_DE_LINEA=r'\;|\:'
t_ENLACE=r'\;|:=|\='

# Define a regular expression 
def t_ID(t):
    r'{LETRA}({LETRA}|{DIGITO}({t_IDCONT}))*'
    t.value = str(t.value)
    return t
def t_IDCONT(t):
    r'{LETRA}({LETRA}(?P<idcont>{t_IDCONT})|{DIGITO}(?P<idcont>{t_IDCONT}))*'
    t.value = str(t.value)
    return t
def t_TIPO(t):
    r'modelo'
    return t
def t_ELEMENTO_QUIMICO(t):
    r'H|Li|Na|K|Rb|Cs|Fr|Be|Mg|Ca|Sr|Ba|Ra|Sc|Y|Ti|Zr|Hf|Db|V|Nb|Ta|Jl|Cr|Mo|W|Rf|Mn|Tc|Re|Bh|Fe|Ru|Os|Hn|Co|Rh|Ir|Mt|Ni|Pd|Pt|Cu|Ag|Au|Zn|Cd|Hg|B|Al|Ga|ln|Tl|C|Si|Ge|Sn|Pb|N|P|As|Sb|Bi|O|S|Se|Te|Po|F|Cl|Br|I|At|He|Ne|Ar|Kr|Xe|Rn'
    t.value=str(t.value)
    return t
def t_DIGITO(t):
    r'\d'#Any digit from 0-9
    t.value =int(t.value)
    return t
def t_LETRA(t):
    r'[a-zA-Z]'
    t.value=str(t.value)
    return t

def t_VALENCIA(t):
    r'[1-9]'#Any digit from 0-9
    t.value = int(t.value)
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
    if tok.type == "ID":
        print(f"Matched TOKEN: {tok.type}: {tok.value}")
