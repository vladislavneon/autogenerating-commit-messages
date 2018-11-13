import re
import sys

def tokenize(line):
    line = re.sub(r'(\w)(?=[^a-zA-Z0-9_ ])', r'\1 ', line)
    line = re.sub(r'([^a-zA-Z0-9_ ])(?=\w)', r'\1 ', line)
    line = re.sub(r'([^a-zA-Z0-9_ ])(?=[^a-zA-Z0-9_ ])', r'\1 ', line)
    line = ' '.join(line.split())
    return line

dataset='intellij_data_limit200'

with open('{dataset:}/test.msg'.format(dataset=dataset), 'r') as inf:
    lines = list(inf)

lines = list(map(tokenize, lines))

with open('{dataset:}/test.msg'.format(dataset=dataset), 'w') as ouf:
    for line in lines:
        ouf.write(line + '\n')

with open('{dataset:}/train.msg'.format(dataset=dataset), 'r') as inf:
    lines = list(inf)

lines = list(map(tokenize, lines))

with open('{dataset:}/train.msg'.format(dataset=dataset), 'w') as ouf:
    for line in lines:
        ouf.write(line + '\n')