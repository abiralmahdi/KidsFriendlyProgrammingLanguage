class Compiler:
    def __init__(self):
        self.output_code = []
        self.called_functions = set()

    def compile(self, node):
        if node[0] == 'assign':
            # Handle variable assignments
            var_name = node[1]
            value = self.compile(node[2])  # Compile the right-hand side value
            self.output_code.append(f"{var_name} = {value}")
            return var_name  # Return the variable name for use in function calls or further operations

        elif node[0] == 'binop':
            # Handle binary operations
            left = self.compile(node[2])
            right = self.compile(node[3])
            operator = node[1]
            return f"({left} {operator} {right})"

        elif node[0] == 'number':
            # Handle numbers
            return str(node[1])

        elif node[0] == 'var':
            # Handle variable references
            return node[1]

        elif node[0] == 'function_call':
            # Handle function calls
            func_name = node[1]
            args = ', '.join([self.compile(arg) for arg in node[2]])

            # Avoid duplicating function calls in output
            if func_name not in self.called_functions:
                self.output_code.append(f"{func_name}({args})")  # Only add function calls once
                self.called_functions.add(func_name)
            return f"{func_name}({args})"  # Ensure function calls return a valid string

        elif node[0] == 'string':
            # Handle string literals
            return node[1]

        elif node[0] == 'list':
            # Handle list literals
            return f"[{', '.join([self.compile(item) for item in node[1]])}]"

        return None

    def get_output_code(self):
        return '\n'.join(self.output_code)
