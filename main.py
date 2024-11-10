# main.py
from parser import parser
from compiler import Compiler

# Sample input code for testing
input_code = '''
x = calculate_mean([5, 3, 9, 3, 7, 8, 5, 3]);
y = calculate_median([2, 3, 4, 5]);
'''

# Parse the input code
ast = parser.parse(input_code)

if ast is None:
    print("Error: Parsing failed. Please check the input code and parser implementation.")
else:
    print("Parsing successful. Proceeding with compilation.")
    compiler = Compiler()

    for node in ast:  # Iterate over the parsed list of statements
        compiler.compile(node)

    output_code = compiler.get_output_code()
    output_code = "from core_functions import *\nfrom visualizations import *\n\n" + output_code

    print("Compiled Code:")
    print(output_code)

    with open('output.py', 'w') as f:
        f.write(output_code)

    exec(output_code)
