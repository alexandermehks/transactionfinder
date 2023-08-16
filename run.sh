#!/bin/sh

touch concat.txt

cat files/* > concat.txt

python3 find.py concat.txt

rm concat.txt


