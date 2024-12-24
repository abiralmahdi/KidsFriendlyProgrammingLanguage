class Compiler:
    def __init__(self):
        self.output_code = []

    def compile(self, node, **kwargs):
        if node is None:
            return ''
        if node[0] == 'assign':
            var_name = node[1]
            value = self.compile(node[2])
            if kwargs.get('mode', 'default') != "nested":
                self.output_code.append(f"{var_name} = {value}")
            return f"{var_name} = {value}" 

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
            
            if kwargs.get('mode', 'default') != "nested":
                self.output_code.append(f"{func_name}({args})")  # Only add function calls once

            return f"{func_name}({args})"  # Ensure function calls return a valid string

        elif node[0] == 'repeat':
            # Handle the repeat loop
            loop_var = node[1]
            start = self.compile(node[2])
            ending = self.compile(node[3])
            body = '\n    '.join([self.compile(statement, mode="nested") for statement in node[4]])  # Loop body
            self.output_code.append(f"for {loop_var} in range({start}, {ending} + 1):\n    {body}")
            return f"for {loop_var} in range({start}, {ending} + 1):\n    {body}"

        
        elif node[0] == 'if_statement':
            # Handle the if statement
            condition = self.compile(node[1])
            body = '\n    '.join([self.compile(statement, mode="nested") for statement in node[2]])
            if kwargs.get('mode', 'default') != "nested":
                self.output_code.append(f"if {condition}:\n    {body}")
            return f"if {condition}:\n        {body}"
        
        elif node[0] == 'if_else_statement':
            # Handle the if-else statement
            condition = self.compile(node[1])
            if_body = '\n    '.join([self.compile(statement, mode="nested") for statement in node[2]])
            else_body = '\n    '.join([self.compile(statement, mode="nested") for statement in node[3]])
            if kwargs.get('mode', 'default') != "nested":
                self.output_code.append(f"if {condition}:\n    {if_body}\nelse:\n    {else_body}")
            return f"if {condition}:\n    {if_body}\nelse:\n    {else_body}"


        elif node[0] == 'string':
            # Handle string literals
            return node[1]

        elif node[0] == 'list':
            # Handle list literals
            return f"[{', '.join([self.compile(item) for item in node[1]])}]"

        return None

    def get_output_code(self):
        return '\n'.join(self.output_code)
