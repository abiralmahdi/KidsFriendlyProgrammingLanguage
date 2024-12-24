# main.py
from parser import parser
from compiler import Compiler

# Sample input code for testing
input_code = '''
x = calculate_mean([5, 3, 9, 3, 7, 8, 5, 3]);
y = calculate_median([2, 3, 4, 5]);

plot_histogram([1,2,3,4,5]);
plot_bar_chart(["A", "B", "C"], [10, 15, 7]);
plot_box_plot([[7, 8, 5, 3], [6, 9, 3, 4]], labels=["Group A", "Group B"]);
plot_scatter_plot([1, 2, 3, 4], [10, 20, 25, 30], title="Sample Scatter Plot", xlabel="Time", ylabel="Value");

a = choose(8,5);
b = permute(7,4);
f = 8!;
abir = 4+33;
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
