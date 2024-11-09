class Compiler:
    def __init__(self):
        self.output_code = []

    def compile(self, node):
        if node[0] == 'assign':
            # Node structure: ('assign', variable, expression)
            var_name = node[1]
            value = self.compile(node[2])
            self.output_code.append(f"{var_name} = {value}")

        elif node[0] == 'binop':
            # Node structure: ('binop', operator, left, right)
            left = self.compile(node[2])
            right = self.compile(node[3])
            operator = node[1]
            return f"({left} {operator} {right})"

        elif node[0] == 'number':
            # Node structure: ('number', value)
            return str(node[1])

        elif node[0] == 'var':
            # Node structure: ('var', name)
            return node[1]

        return None

    def get_output_code(self):
        return '\n'.join(self.output_code)
