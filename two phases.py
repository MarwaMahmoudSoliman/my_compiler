#!/usr/bin/env python
# coding: utf-8

# In[9]:


import re

# Token patterns using regular expressions
patterns = [
    ('Keyword', r'(if|int|else|switch|typedef|union|unsigned|short|signed|void|long|register|sizeof|static|volatile|while|auto|break|case|char|const|continue|default|do|double|enum|extern|return|struct|float|for|goto)'),
    ('Operator', r'=|\+|-|\*|/|%'),
    ('Special_Symbol', r';'),
    ('Constant', r'\d+'),
    ('Identifier', r'[a-zA-Z_]\w*'),
]

# Tokenize function
def tokenize(code, patterns):
    tokens = []
    while code:
        found_match = False
        for token_name, pattern in patterns:
            regex = re.compile(r'\A(' + pattern + r')')  # Anchor pattern to the start of the code
            match = regex.match(code)
            if match:
                value = match.group(1)
                tokens.append((token_name, value))
                code = code[len(value):].lstrip()
                found_match = True
                break  # Break the loop to start matching patterns again from the beginning
        if not found_match:
            raise ValueError(f"Invalid token at: {code}")
    return tokens

# Sample code
sample_code = "int x = 10;"
sample_tokens = tokenize(sample_code, patterns)
print(sample_tokens)

# Syntax analysis and parse tree
def parse(tokens):
    if (len(tokens) == 5 and 
        tokens[0][0] == 'Keyword' and 
        tokens[1][0] == 'Identifier' and 
        tokens[2][0] == 'Operator' and 
        tokens[3][0] == 'Constant' and 
        tokens[4][0] == 'Special_Symbol'):
        
        parse_tree = {
            'Declaration': {
                'keyward': tokens[0][1],
                'identifier': tokens[1][1],
                'Assignment': {
                    'Operator': tokens[2][1],
                    'number': tokens[3][1]
                }
            }
        }
        return 'Valid Syntax: Declaration of int variable', parse_tree
    else:
        return 'Invalid Syntax', None

# Parse tokens and generate parse tree
result, tree = parse(sample_tokens)
print(result)
if tree:
    print("Parse Tree:", tree)


# In[ ]:




