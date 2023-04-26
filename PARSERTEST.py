import ply.yacc as yacc
from prettytable import PrettyTable
import SCANNERTEST

tokens = ( 
    'ID',
     'VALENCIA',
     'ENLACE',
    'TIPO',
    'ASIGNACION',
     'FIN_DE_LINEA',
     'ELEMENTO_QUIMICO',
    'OPERACION',
    'PARAENTESIS_IZQ',
    'PARAENTESIS_DER',
    'PALABRAS_RESERVADAS',
    'INICIO', 'DEFINA', 'COMO', 'FIN',
     'COR_IZQ',
     'COR_DER'
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
                 | ID ASIGNACION modelo_molecular
                 | OPERACION PARAENTESIS_IZQ ID PARAENTESIS_DER'''
    
    
      # Extract the types of the symbols from the slice
    symbol_types = [symbol.type for symbol in p.slice[1:]]

    # Convert the list of types to a string
    symbol_types_str = ' '.join(symbol_types)
    parsed_tokens.append((p.slice[0].type, symbol_types_str))

#<COMPUESTO>::=	"<ELEMENTO_QUIMICO>	|	<ELEMENTO_QUIMICO>	<VALENCIA>	|	<ELEMENTO>	<GRUPO_FUNCIONAL>	|	<ELEMENTO>	<GRUPO_FUNCIONAL>	<ENLACE>	|	<ELEMENTO>	<ENLACE>
def p_compuesto(p):
    '''compuesto : ELEMENTO_QUIMICO
                 | ELEMENTO_QUIMICO VALENCIA
                 | elemento grupo_funcional
                 | elemento grupo_funcional ENLACE
                 | elemento ENLACE'''
      # Extract the types of the symbols from the slice
    symbol_types = [symbol.type for symbol in p.slice[1:]]

    # Convert the list of types to a string
    symbol_types_str = ' '.join(symbol_types)
    parsed_tokens.append((p.slice[0].type, symbol_types_str))


#<COMPUESTOS>::=	<COMPUESTO>	<COMPUESTOS>	|	<COMPUESTO>
def p_compuestos(p):
    '''compuestos : compuesto compuestos
                 | compuesto'''
      # Extract the types of the symbols from the slice
    symbol_types = [symbol.type for symbol in p.slice[1:]]

    # Convert the list of types to a string
    symbol_types_str = ' '.join(symbol_types)
    parsed_tokens.append((p.slice[0].type, symbol_types_str))
                 

#<MODELO_MOLECULAR>::=	<ELEMENTO_QUIMICO>	|	<ELEMENTO_QUIMICO>	<VALENCIA>	|	<ELEMENTO>	<GRUPO_FUNCIONAL>	|	<COMPUESTO>	<GRUPO_FUNCIONAL>	|	<COMPUESTO>	<ELEMENTO>	<GRUPO_FUNCIONAL>	|	<COMPUESTO>	<COMPUESTO>	<COMPUESTOS>
def p_modelo_molecular(p):
    '''modelo_molecular : ELEMENTO_QUIMICO
                        | ELEMENTO_QUIMICO VALENCIA
                        | elemento grupo_funcional 
                        | compuesto grupo_funcional
                        | compuesto elemento grupo_funcional
                        | compuesto compuesto compuestos'''
      # Extract the types of the symbols from the slice
    symbol_types = [symbol.type for symbol in p.slice[1:]]

    # Convert the list of types to a string
    symbol_types_str = ' '.join(symbol_types)
    parsed_tokens.append((p.slice[0].type, symbol_types_str))



#<GRUPO_FUNCIONAL>::=	<GRUPO_FUNCIONAL_INFERIOR>	<GRUPO_FUNCIONAL_SUPERIOR>	|	<GRUPO_FUNCIONAL_SUPERIOR>	<GRUPO_FUNCIONAL_INFERIOR>	|	"("	<MODELO_GRUPO_FUNCIONAL>	")"	|	"["	<MODELO_GRUPO_FUNCIONAL>	"]"
def p_grupo_funcional(p):
    '''grupo_funcional : grupo_funcional_inferior grupo_funcional_superior
                        | grupo_funcional_superior grupo_funcional_inferior
                        | grupo_funcional_superior
                        | grupo_funcional_inferior'''
      # Extract the types of the symbols from the slice
    symbol_types = [symbol.type for symbol in p.slice[1:]]

    # Convert the list of types to a string
    symbol_types_str = ' '.join(symbol_types)
    parsed_tokens.append((p.slice[0].type, symbol_types_str))



#<GRUPO_FUNCIONAL_SUPERIOR>::=	"("	<MODELO_GRUPO_FUNCIONAL>	")"

def p_grupo_funcional_superior(p):
    '''grupo_funcional_superior : PARAENTESIS_IZQ modelo_grupo_funcional PARAENTESIS_DER'''
      # Extract the types of the symbols from the slice
    symbol_types = [symbol.type for symbol in p.slice[1:]]

    # Convert the list of types to a string
    symbol_types_str = ' '.join(symbol_types)
    parsed_tokens.append((p.slice[0].type, symbol_types_str))



#<GRUPO_FUNCIONAL_INFERIOR>::=	"["	<MODELO_GRUPO_FUNCIONAL>	"]"

def p_grupo_funcional_inferior(p):
    '''grupo_funcional_inferior : COR_IZQ modelo_grupo_funcional COR_DER'''
      # Extract the types of the symbols from the slice
    symbol_types = [symbol.type for symbol in p.slice[1:]]

    # Convert the list of types to a string
    symbol_types_str = ' '.join(symbol_types)
    parsed_tokens.append((p.slice[0].type, symbol_types_str))



#<MODELO_GRUPO_FUNCIONAL>::=	<ENLACE>	<MODELO_MOLECULAR>	|	<ELEMENTO_QUIMICO>	|	<ELEMENTO_QUIMICO>	<VALENCIA>	|	<ELEMENTO>	<GRUPO_FUNCIONAL>	|	<COMPUESTO>	<ELEMENTO>	|	<COMPUESTO>	<ELEMENTO>	<GRUPO_FUNCIONAL>	|	<COMPUESTO>	<COMPUESTO>	<COMPUESTOS>
def p_modelo_grupo_funcional(p):
    '''modelo_grupo_funcional : ENLACE modelo_molecular
                              | ELEMENTO_QUIMICO
                              | ELEMENTO_QUIMICO VALENCIA
                              | elemento grupo_funcional
                              | compuesto elemento
                              | compuesto elemento grupo_funcional
                              | compuesto compuesto compuestos'''
      # Extract the types of the symbols from the slice
    symbol_types = [symbol.type for symbol in p.slice[1:]]

    # Convert the list of types to a string
    symbol_types_str = ' '.join(symbol_types)
    parsed_tokens.append((p.slice[0].type, symbol_types_str))



#<ELEMENTO>::=	"<ELEMENTO_QUIMICO>	|	<ELEMENTO_QUIMICO>	<VALENCIA>

def p_elemento(p):
    ''' elemento : ELEMENTO_QUIMICO
            | ELEMENTO_QUIMICO VALENCIA '''
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
parser = yacc.yacc(debug=False)

# Test the Parser
with open ('error_cases.txt','r') as file:
    i = file.read()

parser.parse(i)

# Write the table to the terminal


    # Build the table
x = PrettyTable()
x.field_names = ["Izquierda", "Derecha"]
for prod in parsed_tokens:
    x.add_row(prod)

    
print(str(x))
    