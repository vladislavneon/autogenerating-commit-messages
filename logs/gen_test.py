import subprocess as sbpr
import re
import sys
from time import time
from tokenizer import tokenize

begin_date = '2018-07-01 00:00:00'

gt1 = time()
t1 = time()

with open('test.commit', 'w') as ouf:
    sbpr.run(['git', 'log', '--no-merges', '--after=' + begin_date], 
         stdout=ouf,
         cwd='../intellij-community', 
         text=True)

t2 = time()

print('commits are written in {:.3f} s'.format(t2 - t1))

t1 = time()

with open('test.msg', 'w') as ouf:
    sbpr.run(['git', 'log', '--no-merges', '--after=' + begin_date, '--pretty=tformat:%s'], 
         stdout=ouf,
         cwd='../intellij-community', 
         text=True)

t2 = time()

print('messages are written in {:.3f} s'.format(t2 - t1))

t1 = time()

with open('test.diff.log', 'w') as ouf:
    sbpr.run(['git', 'log', '-p', '--no-merges', '--after=' + begin_date, '--pretty=tformat:>>>terminal<<<'], 
             stdout=ouf,
             cwd='../intellij-community',
             text=True)

t2 = time()

print('diffs are written in {:.3f} s'.format(t2 - t1))

t1 = time()

diff_lines = []
with open('test.diff.log', 'r', errors='ignore') as inf:
    for line in inf:
        diff_lines.append(line)

print(len(diff_lines))

diff_lines = diff_lines[1:]
diff_lines.append('>>>terminal<<<')

t2 = time()

print('diffs are loaded in {:.3f} s'.format(t2 - t1))

t1 = time()

with open('test.diff', 'w') as ouf:
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

# with open('test.hash', 'r') as hash_file, \
#      open('test.msg', 'w') as msg_file, \
#      open('test.diff', 'w') as diff_file:
#     cnt = 0
#     for commit_hash in hash_file:
#         commit_message = \
#             sbpr.run(['git', 'log', '-1', '--pretty=tformat:%s', commit_hash.strip()], 
#                      cwd='../intellij-community', capture_output=True, text=True).stdout.strip()
#         # try:
#         #     commit_diff = \
#         #         sbpr.run(['git', 'diff', '80bc0826680df3664c21b6fa2a95d8a7164093cc'], 
#         #                  cwd='../intellij-community', capture_output=True, text=True).stdout.strip().split('\n')
#         # except UnicodeDecodeError:
#         #     commit_diff = ['', '', 'UnicodeError']
#         msg_file.write(commit_message + '\n')
#         #diff_file.write(commit_diff[2] + '\n')
#         cnt += 1
#         print(cnt)
