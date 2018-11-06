# #!/usr/bin/env bash

cd ../intellij-community
git log --no-merges -p --after="$1" --pretty=tformat:">>>terminal<<<" > ../logs/test.diff.log
cd ../logs
python3 tokenizer.py test
