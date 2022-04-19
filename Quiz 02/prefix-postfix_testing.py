from stack import Stack
import re

# this is handy for checking if a token is an operand
# ie, if token not in OP_PREC then it is an operand
OP_PREC ={"(":1,
         "+": 2,
         "-": 2,
         "*": 3,
         "/": 3,
         ")": 4}



def tokens_from_string(expression):
    """
    Split postfix string into tokens.
    Tokens should be integer values.
    Returns a list of tokens, as strings.
    For example:
    '2 3 +' => ['2', '3', '+']
    '2 + 3 * 4' => ['2', '+', '3', '*', '4']
    Don't worry about how this works
    """
    token_list = re.findall(r'(\d+|\*|\+|\/|\-|\)|\(|\^)', expression)
    return token_list
def prefix_to_postfix(prefix_expression):
    """Converts a prefix expression to postfix
    >>> prefix_to_postfix('* - a b c')
    'a b - c *'
    >>> prefix_to_postfix('* - a - b c d')
    'a b c - - d *'
    """
    tokens = tokens_from_string(prefix_expression)
    output = ''
    stack = Stack()
    # Complete this function for extra fun :)
    # ---start student section---
    LEFT_DONE = 'left done'
    
    for token in tokens:
        if token in OP_PREC:
            stack.push(token)
        else:
            print(token)
            output += token + " "
            
            while (not stack.is_empty()) and (LEFT_DONE == stack.peek()):
                discard = stack.pop()
                print(discard)
                operator = stack.pop()
                print(operator)
                output += operator + " "
            
            stack.push(LEFT_DONE)
    
    return output.strip()
    # ===end student sectio

print(prefix_to_postfix('* - a b c'))