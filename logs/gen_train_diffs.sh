# #!/usr/bin/env bash

cd ../intellij-community
git log --no-merges -p --after="$1" --before="$2" --pretty=tformat:">>>terminal<<<" > ../logs/train17-18.diff.log
cd ../logs
python3 tokenizer.py train17-18
