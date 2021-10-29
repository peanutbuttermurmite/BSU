#!/bin/bash
printf "#Below is the data gathered from the powerpointcalc.Data is in the format:Power Level:Number of Star Powers:Amount of Power Points\n" >> bsusave1.py
read -p "Enter the directory of the saved file: " share
cat $share >> bsusave1.py