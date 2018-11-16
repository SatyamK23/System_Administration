#!/bin/bash
echo "Converting filename from upper case to lower case."
for f in *;
	do mv -- "$f" "$(tr [:upper:] [:lower:] <<< "$f")";
done
