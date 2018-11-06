import re
import sys

def tokenize(buffer):
    too_long_diff_threshold = 100
    if (len(buffer) > too_long_diff_threshold):
        return '\n'
    res = ''
    for line in buffer:
        if (re.match(r'diff --git', line) is not None):
            continue
        if (re.match(r'index \w{12}\.\.\w{12} \d{6}', line) is not None):
            continue
        line = re.sub(r'@@.*?@@', r'', line)
        line = re.sub(r'---', r'mmm', line)
        line = re.sub(r'\+\+\+', r'ppp', line)
        line = re.sub(r'(\w)(?=[^a-zA-Z0-9_ ])', r'\1 ', line)
        line = re.sub(r'([^a-zA-Z0-9_ ])(?=\w)', r'\1 ', line)
        line = re.sub(r'([^a-zA-Z0-9_ ])(?=[^a-zA-Z0-9_ ])', r'\1 ', line)
        line = ' '.join(line.split())
        if (line != ''):
            res += line
            res += ' <nl> '
    res += '\n'
    return res


def main():
    dataset = sys.argv[1]
    with open(dataset + '.diff.log', 'r', errors='ignore') as inf, open(dataset + '.diff', 'w') as ouf:
        buffer = []
        time_cnt = 0
        ln = 1
        for line in inf:
            if ln == 1:
                ln += 1
                continue
            line = line.strip()
            if (line == '>>>terminal<<<'):
                output_line = tokenize(buffer)
                buffer = []
                ouf.write(output_line)
                time_cnt += 1
                if time_cnt % 100 == 0:
                    print(time_cnt)
            else:
                buffer.append(line)
            ln += 1
        output_line = tokenize(buffer)
        buffer = []
        ouf.write(output_line)
