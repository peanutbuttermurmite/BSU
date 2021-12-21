#!/bin/bash
echo "----> Zipping up"
zip -r bsusave.zip bsusave.py
mv bsusave.zip bsusave.bsu
rm bsusave.py
echo "----> File saved"
