# contraints: less than 1000 strings
# less than 1000 in length
expression = '{[(})]}'


def is_matched(expression):
    stack = []
    pairs = {'{': '}', '[': ']', '(': ')'}
    for c in expression:
        if c in pairs:
            stack.append(pairs[c])
        elif stack and c == stack[-1]:
            stack.pop()
        else:
            return False
    return not stack

print is_matched(expression)