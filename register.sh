#!/bin/bash
printf "----> Zipping up"
zip -r bsusave.zip bsusave.py
mv bsusave.zip bsusave.bsu
printf "----> File saved"
