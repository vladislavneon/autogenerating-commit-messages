# #!/usr/bin/env bash

cd ../intellij-community
datefrom="2018-07-01 00:00:00"
git log --no-merges --after="$datefrom" > ../logs/test.commit
git log --no-merges --after="$datefrom" --pretty=tformat:"%H" > ../logs/test.hash
