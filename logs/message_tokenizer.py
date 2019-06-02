import re
import sys

def parse_tag(msg):
    m = re.match(r'(\[.+?\])(.*)', msg)
    if m:
        return m.group(1).lower(), m.group(2)
    # m = re.match(r'([A-Z]+?)-\d+?\D(.*)', msg)
    # if m:
    #     return m.group(1).lower(), m.group(2)
    m = re.match(r'([A-Za-z]+?):(.*)', msg)
    if m and len(m.group(1)) < 10:
        return '[{}]'.format(m.group(1).lower()), m.group(2)
    return '', msg

def handle_tags(line):
    tag, rest = parse_tag(line)
    issue_tags = re.findall(r'[^\n ]??([A-Z]+)-(?:CR-)?\d+[^ ]?', rest)
    issue_tags = set(map(str.lower, issue_tags))
    issue_tags = ' '.join(map((lambda s: '{{{}}}'.format(s)), issue_tags))
    rest = re.sub(r'[^\n ]??([A-Z]+)-(?:CR-)?\d+[^ ]?', r'', rest)
    return tag, issue_tags, rest


def tokenize_msg(line):
    tag, issue_tags, rest = handle_tags(line)
    res = []
    if tag:
        res.append(tag)
    if issue_tags:
        res.append(issue_tags)
    res.append(tokenize(rest))
    return ' '.join(res)

def tokenize(line):
    line = re.sub(r'(\w)(?=[^a-zA-Z0-9_ ])', r'\1 ', line)
    line = re.sub(r'([^a-zA-Z0-9_ ])(?=\w)', r'\1 ', line)
    line = re.sub(r'([^a-zA-Z0-9_ ])(?=[^a-zA-Z0-9_ ])', r'\1 ', line)
    line = ' '.join(line.split())
    return line

dataset='generated_data'

with open('{dataset:}/test.msg'.format(dataset=dataset), 'r') as inf:
    lines = list(inf)

lines = list(map(tokenize_msg, lines))

with open('{dataset:}/test2.msg'.format(dataset=dataset), 'w') as ouf:
    for line in lines:
        ouf.write(line + '\n')

with open('{dataset:}/train.msg'.format(dataset=dataset), 'r') as inf:
    lines = list(inf)

lines = list(map(tokenize_msg, lines))

with open('{dataset:}/train2.msg'.format(dataset=dataset), 'w') as ouf:
    for line in lines:
        ouf.write(line + '\n')