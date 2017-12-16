class Part:

    def __init__(self, name, value=0):
        self.name = name
        self.value = value
        self.highest_value = 0

    def get_value(self):
        if self.highest_value < self.value:
            self.highest_value = self.value
        return self.value

    def set_value(self, value):
        self.value = value

    def get_highest_value(self):
        return self.highest_value

def get_variable(operations_list, variable):
    for element in operations_list:
        if element.name == variable:
            return element
    return None

def logical_operation_table(variable, number, operation):
    if operation == ">":
        return int(variable.value) > int(number)
    elif operation == "<":
        return int(variable.value) < int(number)
    elif operation == "<=":
        return int(variable.value) <= int(number)
    elif operation == ">=":
        return int(variable.value) >= int(number)
    elif operation == "==":
        return int(variable.value) == int(number)
    elif operation == "!=":
        return int(variable.value) != int(number)

def mathematical_operation_table(variable, number, operation):
    if operation == "inc":
        current_value = variable.get_value()
        current_value += int(number)
        variable.set_value(current_value)
    else:
        current_value = variable.get_value()
        current_value -= int(number)
        variable.set_value(current_value)

def eval_condition(condition, variables_list):
        parts = condition.split()
        variable = get_variable(variables_list, parts[0])
        if variable is None:
            variable = Part(parts[0], 0)
            variables_list.append(variable)
        operator = parts[1]
        number = parts[2]

        return logical_operation_table(variable, number, operator)

def condition_register(data):
    variables_list = list()
    for line in data.splitlines():
        operation, condition = line.split('if')
        if eval_condition(condition, variables_list):
            operation = operation.split()
            variable = get_variable(variables_list, operation[0])
            if variable is None:
                variable = Part(operation[0], 0)
                variables_list.append(variable)
            operator = operation[1]
            number = operation[2]

            mathematical_operation_table(variable, number, operator)

    largest_value_register = 0
    highest_value = 0
    for variable in variables_list:
        if largest_value_register < variable.get_value():
            largest_value_register = variable.get_value()
        if highest_value < variable.get_highest_value():
            highest_value = variable.get_highest_value()

    print "Part one, highest value in register:", largest_value_register
    print "Part two, highest value:", highest_value

f = open('input.txt', 'r')
content = f.read()
f.close()

condition_register(content)