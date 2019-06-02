with open('generated_data/test.msg', 'r') as inf:
    messages = list(inf)

with open('generated_data/test.diff', 'r') as inf:
    diffs = list(inf)

print(len(list(filter(lambda s: s == '\n', diffs))))

with open('generated_data/test.msg', 'w') as msg_file, \
     open('generated_data/test.diff', 'w') as diff_file:
    n = len(messages)
    for i in range(n):
        if diffs[i] != '\n':
            msg_file.write(messages[i])
            diff_file.write(diffs[i])

with open('generated_data/train.msg', 'r') as inf:
    messages = list(inf)

with open('generated_data/train.diff', 'r') as inf:
    diffs = list(inf)

print(len(list(filter(lambda s: s == '\n', diffs))))

with open('generated_data/train.msg', 'w') as msg_file, \
     open('generated_data/train.diff', 'w') as diff_file:
    n = len(messages)
    for i in range(n):
        if diffs[i] != '\n':
            msg_file.write(messages[i])
            diff_file.write(diffs[i])

