import re
import sys

def tokenize_line(line):
    line = re.sub(r'(\w)(?=[^a-zA-Z0-9_ ])', r'\1 ', line)
    line = re.sub(r'([^a-zA-Z0-9_ ])(?=\w)', r'\1 ', line)
    line = re.sub(r'([^a-zA-Z0-9_ ])(?=[^a-zA-Z0-9_ ])', r'\1 ', line)
    tokens = line.split()
    line = ' '.join(tokens)
    return line, len(tokens)

def tokenize(buffer):
    too_long_diff_threshold = 100
    too_long_line_threshold = 10000
    if (len(buffer) > too_long_diff_threshold):
        return '\n'
    res = ''
    tokens = 0
    for line in buffer:
        if (re.match(r'diff --git', line) is not None):
            continue
        if (re.match(r'index \w{12}\.\.\w{12} \d{6}', line) is not None):
            continue
        line = re.sub(r'@@.*?@@', r'', line)
        line = re.sub(r'---', r'mmm', line)
        line = re.sub(r'\+\+\+', r'ppp', line)
        line, token_cnt = tokenize_line(line)
        tokens += token_cnt
        if (line != ''):
            res += line
            res += ' <nl> '
        if (tokens > too_long_line_threshold):
            return '\n'
    res += '\n'
    return res
