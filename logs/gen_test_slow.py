import subprocess as sbpr

begin_date = '2018-07-01 00:00:00'

with open('test.commit', 'w') as ouf:
    sbpr.run(['git', 'log', '--no-merges', '--after=' + begin_date], 
         stdout=ouf,
         cwd='../intellij-community', 
         text=True)

print('commits are written')

with open('test.hash', 'w') as ouf:
    sbpr.run(['git', 'log', '--no-merges', '--after=' + begin_date, '--pretty=tformat:%H'], 
         stdout=ouf,
         cwd='../intellij-community', 
         text=True)

print('hashes are written')

with open('test.hash', 'r') as hash_file, \
     open('test.msg', 'w') as msg_file, \
     open('test.diff', 'w') as diff_file:
    cnt = 0
    for commit_hash in hash_file:
        commit_message = \
            sbpr.run(['git', 'log', '-1', '--pretty=tformat:%s', commit_hash.strip()], 
                     cwd='../intellij-community', capture_output=True, text=True).stdout.strip()
        # try:
        #     commit_diff = \
        #         sbpr.run(['git', 'diff', '80bc0826680df3664c21b6fa2a95d8a7164093cc'], 
        #                  cwd='../intellij-community', capture_output=True, text=True).stdout.strip().split('\n')
        # except UnicodeDecodeError:
        #     commit_diff = ['', '', 'UnicodeError']
        msg_file.write(commit_message + '\n')
        #diff_file.write(commit_diff[2] + '\n')
        cnt += 1
        print(cnt)
