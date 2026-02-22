#! /bin/bash

if [ "$#" -ne 2 ]; then
	echo "Usage: $0 [file_name] [word]"
	exit 1
fi

FILE=$1
WORD=$2

COUNT=$(grep -o "$WORD" "FILE" | wc -l)
echo "The word '$word' appears $COUNT times in $FILE."
