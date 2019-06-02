import subprocess as sbpr
import re
import sys
from time import time
from tokenizer import tokenize

begin_date = '2018-05-01 00:00:00'
end_date = '2018-11-01 00:00:00'

gt1 = time()
t1 = time()

with open('generated_data/test.commit', 'w') as ouf:
    sbpr.run(['git', 'log', '--no-merges', '--after=' + begin_date, '--before=' + end_date], 
         stdout=ouf,
         cwd='../intellij-community')

t2 = time()

print('commits are written in {:.3f} s'.format(t2 - t1))

t1 = time()

with open('generated_data/test.msg', 'w') as ouf:
    sbpr.run(['git', 'log', '--no-merges', '--after=' + begin_date, '--before=' + end_date, '--pretty=tformat:%s'], 
         stdout=ouf,
         cwd='../intellij-community')

t2 = time()

print('messages are written in {:.3f} s'.format(t2 - t1))

t1 = time()

with open('generated_data/test.diff.log', 'w') as ouf:
    sbpr.run(['git', 'log', '-p', '--no-merges', '--after=' + begin_date, '--before=' + end_date, '--pretty=tformat:>>>terminal<<<'], 
             stdout=ouf,
             cwd='../intellij-community')

t2 = time()

print('diffs are written in {:.3f} s'.format(t2 - t1))

t1 = time()

diff_lines = []
with open('generated_data/test.diff.log', 'r', errors='ignore') as inf:
    for line in inf:
        diff_lines.append(line)

print(len(diff_lines))

diff_lines = diff_lines[1:]
diff_lines.append('>>>terminal<<<')

t2 = time()

print('diffs are loaded in {:.3f} s'.format(t2 - t1))

t1 = time()

with open('generated_data/test.diff', 'w') as ouf:
    buffer = []
    time_cnt = 0
    for line in diff_lines:
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

t2 = time()
gt2 = time()

print('diffs are tokenized in {:.3f} s'.format(t2 - t1))

print('total in {:.3f} s'.format(gt2 - gt1))
