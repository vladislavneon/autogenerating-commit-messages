import subprocess as sbpr

#res = sbpr.run(['git', 'log', '-1', '--pretty=tformat:%s', 'c2139af5c4d2b633bb7b6a4b5e0e07c73e5663d4'], 
#                cwd='../intellij-community', capture_output=True, text=True)
res = sbpr.run(['git', 'diff', '80bc0826680df3664c21b6fa2a95d8a7164093cc'], 
                cwd='../intellij-community', capture_output=True, text=True)
line = res.stdout.strip().split('\n')
print(line[0])
print(line[1])
print(line[2])
