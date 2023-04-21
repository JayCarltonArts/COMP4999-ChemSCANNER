import ply.lex as lex
import ply.yacc as yacc
# from ply.lex import Token
import re
# Define the list of token names
tokens = ( 'ID',
    'PALABRAS_RESERVADAS',
    'INICIO',
    'FIN'
)




# Define a regular expression
 
# def t_ASIGNACION(t):
#     r':='
#     return t
# def t_TIPO(t):
#     r'modelo'
#     return t

def t_PALABRAS_RESERVADAS(t):
    r'(inicio|defina|como|fin)'
    if t.value == 'inicio':
        t.type = 'INICIO'
    elif t.value == 'fin':
        t.type = 'FIN'
    return t

# def t_ELEMENTO_QUIMICO(t):
#     r'Ag|Al|Ar|As|At|Au|Ba|Be|Bh|Bi|Br|Ca|Cd|Cl|Co|Cr|Cs|Cu|Db|Fe|Fr|Ga|Ge|He|Hf|Hg|Hn|Ir|Jl|Kr|Li|ln|Mg|Mn|Mo|Mt|Na|Nb|Ne|Ni|Os|Pb|Pd|Po|Pt|Ra|Rb|Re|Rf|Rh|Rn|Ru|Sb|Sc|Se|Si|Sn|Sr|Ta|Tc|Te|Ti|Tl|Xe|Zn|Zr|B|C|F|H|I|K|N|O|P|S|V|W|Y'
#     return t

# def t_OPERACION(t):
#     r'graficar2d|graficar3d|pesomolecular'
#     return t
# def t_VALENCIA(t):
#     r'[1-9]'
#     return t



# Define the regular expression for each token
# t_FIN_DE_LINEA=r'\;|\:'
t_ID= r'[a-zA-Z][a-zA-Z0-9_]*'
# t_ENLACE=r'\-|\:\:|\:|\='
# t_PARAENTESIS_IZQ= r'\('
# t_PARAENTESIS_DER= r'\)'
# t_COR_IZQ=r'\['
# t_COR_DER=r'\]'





# Define a function to handle errors
def t_error(t):
     print(f"Error: Illegal character 't.value[0]'")
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
    
    parsed_tokens.append((p.slice[0].type, p.slice[1].type, p.slice[2].type, p.slice[3].type))


    
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
print("Production Table:")
print("  \t\tRule\t\t\t\t\t\t\t\t\t")
print("-------------------------------------------------------------------------------------------------------------------")
for prod in parsed_tokens:
    print(f"  {prod[0]}-->{prod[1]},{prod[2]},{prod[3]}")

while True:
    try:
       s = i
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    exit()
