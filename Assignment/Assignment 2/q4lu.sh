#!bin/bash

#find . -type f -name '*.*'
#Lower to Upper Filename Conversion
echo "Converting filename from lower case to upper case."
for f in *;
do mv -- "$f" "$(tr [:lower:] [:upper:] <<< "$f")";
done
