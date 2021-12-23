#!/bin/bash
echo "----> Zipping up"
zip -r bsusave.zip bsusave.py settings.py
mv bsusave.zip bsusave.bsu
rm settings.py bsusave.py
echo "----> File saved"
