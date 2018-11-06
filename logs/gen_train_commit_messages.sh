# #!/usr/bin/env bash

cd ../intellij-community
datefrom="2017-07-01 00:00:00"
dateto="2018-07-01 00:00:00"
git log --no-merges --after="$datefrom" --before="$dateto" > ../logs/train.commit
git log --no-merges --after="$datefrom" --before="$dateto" --pretty=tformat:"%H" > ../logs/train.hash
