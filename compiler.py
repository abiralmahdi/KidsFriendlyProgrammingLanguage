# compiler.py
class Compiler:
    def __init__(self):
        self.output_code = []

    def compile(self, node):
        print(f"Compiling node: {node}")  # Debug line
        if node[0] == 'assign':
            var_name = node[1]
            value = self.compile(node[2])
            self.output_code.append(f"{var_name} = {value}")

        elif node[0] == 'binop':
            left = self.compile(node[2])
            right = self.compile(node[3])
            operator = node[1]
            return f"({left} {operator} {right})"

        elif node[0] == 'number':
            return str(node[1])

        elif node[0] == 'var':
            return node[1]
        
        elif node[0] == 'list':
            return f"[{', '.join([self.compile(item) for item in node[1]])}]"

        elif node[0] == 'function_call':
            func_name = node[1]
            args = ', '.join([self.compile(arg) for arg in node[2]])
            return f"{func_name}({args})"
        
        if node is None:
            raise ValueError("Unexpected None node during compilation.")


        return None

    def get_output_code(self):
        return '\n'.join(self.output_code)
