def valid_parentheses(string):
    item_of_parentheses = {")": "(", "}": "{", "]": "["}
    item_stack = {"(": ")", "{": "}", "[": "]"}
    item_list = []
    for item in string:
        if item in item_of_parentheses.keys():
            if item == ')':
                if item_of_parentheses[item] not in item_stack.values():
                    return False
            elif item == '}':
                if item_of_parentheses[item] not in item_stack.values():
                    return False
            elif item == ']':
                if item_of_parentheses[item] not in item_stack.values():
                    return False
            else:
                item_list.append(item)
        elif item in item_stack.keys():
            item.pop()

    for item in item_of_parentheses.keys():
        if item_of_parentheses[item] != item_stack[item]:
            return False


    return True

string = "(){}[]"
print(valid_parentheses(string))
