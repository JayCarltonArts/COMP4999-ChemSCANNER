import ply.yacc as yacc
import ply.lex as lex
from prettytable import PrettyTable
import SCANNERTEST

tokens = ( 
    'ID',
    # 'VALENCIA',
    # 'ENLACE',
    'TIPO',
    'ASIGNACION',
     'FIN_DE_LINEA',
    # 'ELEMENTO_QUIMICO',
    'OPERACION',
    'PARAENTESIS_IZQ',
    'PARAENTESIS_DER',
    'PALABRAS_RESERVADAS',
    'INICIO', 'DEFINA', 'COMO', 'FIN'
#     'COR_IZQ',
#     'COR_DER'
 )

parsed_tokens = []

# Define an empty stack to track parser state



# Definir las reglas de produccion
start = 'S'


#S -> inicio sentencias fin (calls sentencia for the middle content)
def p_S(p):
    '''S : INICIO sentencias FIN'''
    
     # Extract the types of the symbols from the slice
    symbol_types = [symbol.type for symbol in p.slice[1:]]

    # Convert the list of types to a string
    symbol_types_str = ' '.join(symbol_types)
    parsed_tokens.append((p.slice[0].type, symbol_types_str))

#sentencias -> sentencia FIN_DE_LINEA sentencias (continues the code) | sentencia FIN_DE_LINEA (last statement)
def p_sentencias(p):
    '''sentencias : sentencia FIN_DE_LINEA sentencias	
                  | sentencia FIN_DE_LINEA'''
                  
    
      # Extract the types of the symbols from the slice
    symbol_types = [symbol.type for symbol in p.slice[1:]]

    # Convert the list of types to a string
    symbol_types_str = ' '.join(symbol_types)
    parsed_tokens.append((p.slice[0].type, symbol_types_str))


#sentencia -> defina ID como modelo (declaracion de variable) |ID ASIGNACION modelo_molecular(assigns a value to a variable by calling ASIGNACION) 
# | OPERACION (ID) [function operation]
def p_sentencia(p):
    '''sentencia : DEFINA ID COMO TIPO
                 | ID ASIGNACION ID
                 | OPERACION PARAENTESIS_IZQ ID PARAENTESIS_DER'''
                 
    
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
        parser.errok()
    else:
        print("Syntax error: Unexpected end of input")





# Build the parser
parser = yacc.yacc(debug=True)

# Test the Parser
with open ('error_cases.txt','r') as file:
     i = file.read()

parser.parse(i)

# Write the table to the file

with open("parserout", "w") as outfile:


    # Build the table
    x = PrettyTable()
    x.field_names = ["Pila", "Entrada"]
    for prod in parsed_tokens:
        x.add_row(prod)

    
    outfile.write(str(x))