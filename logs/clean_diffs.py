with open('test.msg', 'r') as inf:
    messages = list(inf)

with open('test.diff', 'r') as inf:
    diffs = list(inf)

#print(len(list(filter(lambda s: s == '\n', diffs))))

with open('test.msg.clean', 'w') as msg_file, \
     open('test.diff.clean', 'w') as diff_file:
    n = len(messages)
    for i in range(n):
        if diffs[i] != '\n':
            msg_file.write(messages[i])
            diff_file.write(diffs[i])

with open('train.msg', 'r') as inf:
    messages = list(inf)

with open('train.diff', 'r') as inf:
    diffs = list(inf)

print(len(list(filter(lambda s: s == '\n', diffs))))

with open('train.msg.clean', 'w') as msg_file, \
     open('train.diff.clean', 'w') as diff_file:
    n = len(messages)
    for i in range(n):
        if diffs[i] != '\n':
            msg_file.write(messages[i])
            diff_file.write(diffs[i])

