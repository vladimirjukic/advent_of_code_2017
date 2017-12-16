class Node:
    def __init__(self, name, weight, children):
        self.name = name
        self.weight = weight
        self.children = children

def create_nodes(data):
    lines = data.splitlines()
    nodes = list()
    for i in range(0, len(lines)):
        row = lines[i].split(" ")
        row[1] = row[1].replace("(","")
        row[1] = row[1].replace(")","")
        children = lines[i].split(" -> ")
        child = None
        if len(children) > 1:
            child = children[1]
        nodes.append(Node(row[0], int(row[1]), child))

    return nodes

def get_node(current, nodes):
    for node in nodes:
        if node.name == current:
            return node

    return None

def find_root_program(data):
    nodes = create_nodes(data)
    root = None
    for node in nodes:
        count = data.count(node.name)
        if count == 1:
            root = node
    return root

def child_weight(child, nodes):
    if child.children is None:
        return child.weight

    weight = 0
    for sub_child in child.children.split(", "):
        weight += child_weight(get_node(sub_child, nodes), nodes)
    return weight + child.weight

def is_single_weight_occurrence(weights, element):
    return weights.count(element) == 1

def get_weight_multiple_occurrences(weights):
    for weight in weights:
        if weights.count(weight) > 1:
            return weight
    return None

def count_program_weight_balance(node, nodes, multiple_occurence_weight, single_occurence_weight):
    if node.children is not None:
        all_weights = list()
        for current_child in node.children.split(", "):
            all_weights.append(child_weight(get_node(current_child, nodes), nodes))

        for i in range(0, len(all_weights)):
            if is_single_weight_occurrence(all_weights, all_weights[i]):
                return count_program_weight_balance(get_node((node.children.split(", "))[i], nodes), nodes,
                                                    get_weight_multiple_occurrences(all_weights), all_weights[i])

    return node.weight - (single_occurence_weight - multiple_occurence_weight)

def balance_program(data):
    return count_program_weight_balance(find_root_program(data), create_nodes(data), 0, 0)

f = open('input.txt', 'r')
content = f.read()
f.close()

print "Part one:", find_root_program(content).name
print "Part two:", balance_program(content)