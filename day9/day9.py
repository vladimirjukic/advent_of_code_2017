def count_groups(data):

    group_counter = 0
    bracket_counter = 0
    is_garbage = False
    i = 0
    while i < len(data):

        if data[i] == "!":
            i += 1
        elif data[i] == "<":
            is_garbage = True
        elif data[i] == ">":
            is_garbage = False
        elif data[i] == "{" and not is_garbage:
            bracket_counter += 1
        elif data[i] == "}" and not is_garbage:
            group_counter += bracket_counter
            bracket_counter -= 1

        i += 1

    print "Groups:,", group_counter

def count_garbage(data):

    bracket_counter = 0
    garbage_list = list()
    i = 0
    while i < len(data):

        if data[i] == "<" and bracket_counter == 0:
            i += 1
            bracket_counter += 1
            continue
        elif data[i] == "!" and bracket_counter > 0:
            i += 2
            continue
        elif data[i] == ">":
            bracket_counter -= 1;

        if bracket_counter > 0:
            garbage_list.append(data[i])

        i += 1

    print "Garbage:,", len(garbage_list)

f = open('input.txt', 'r')
content = f.read()
f.close()

count_groups(content)
count_garbage(content)