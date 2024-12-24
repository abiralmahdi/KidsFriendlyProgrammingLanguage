# main.py
from parser import parser
from compiler import Compiler
from lexer import lexer
from pprint import pprint

def read_custom_file(filename):
    if filename.endswith('.stk'):
        with open(filename, 'r') as file:
            code = file.read()
        return code
    else:
        raise ValueError("Invalid file extension. Please use a '.stk' file.")

input_code = read_custom_file("myCode.stk")

# lexer.input(input_code)
# for token in lexer:
#     print(token)

# Parse the input code
ast = parser.parse(input_code)

if ast is None:
    print("Error: Parsing failed. Please check the input code and parser implementation.")
else:
    print("Parsing successful. Proceeding with compilation.")
    compiler = Compiler()

    pprint(ast)

    for node in ast:  # Iterate over the parsed list of statements
        compiler.compile(node)

    output_code = compiler.get_output_code()
    output_code = "from core_functions import *\nfrom visualizations import *\n\n" + output_code

    print("Compiled Code:")
    print(output_code)

    with open('output.py', 'w') as f:
        f.write(output_code)

    exec(output_code)
