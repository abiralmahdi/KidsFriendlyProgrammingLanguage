from parser import parser  # Import the parser built in point 2
from compiler import Compiler

# Test input
input_code = 'x = 3 + 4 * 2'

# Parse the input code
ast = parser.parse(input_code)

# Compile the AST to Python code
compiler = Compiler()
compiler.compile(ast)
output_code = compiler.get_output_code()

# Print or save the compiled Python code
print("Compiled Code:")
print(output_code)

